"""Convert the six-week course repo into Carpentries Workbench episodes.
Usage: python scripts/convert_from_course.py SOURCE_REPO LESSON_REPO"""
import os, posixpath, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wb_meta import WEEKS, TIME, SECTIONS, OPTIONAL, BRIDGES, PRACTICE, PRACTICE_Q

SRC, DST = sys.argv[1], sys.argv[2]
W = os.path.join(SRC, 'weeks')
EP = os.path.join(DST, 'episodes')
LE = os.path.join(DST, 'learners')

# ---------------------------------------------------------------- names
def sec_file(s, slug): return f"{s.replace('.', '-')}-{slug}.md"

TARGET = {}   # source path (relative to SRC, posix) -> (folder, filename)
for s, m in SECTIONS.items():
    TARGET['weeks/' + m['src']] = ('episodes', sec_file(s, m['slug']))
for s, m in OPTIONAL.items():
    TARGET['weeks/' + m['src']] = ('learners', sec_file(s, m['slug']))
for w in WEEKS:
    TARGET[f'weeks/week-{w}/README.md'] = ('episodes', f'week-{w}-overview.md')
    TARGET[f'weeks/week-{w}/bridge.md'] = ('episodes', f'week-{w}-bridge.md')
    TARGET[f'weeks/week-{w}/practice/README.md'] = ('episodes', f'week-{w}-practice.md')
TARGET['weeks/week-5/practice/mini_project/README.md'] = ('episodes', 'week-5-practice.md')
for w, m in PRACTICE.items():
    for f in m['files']:
        TARGET[f'weeks/week-{w}/practice/{f}'] = ('episodes', f'files/week-{w}/{f}')

# ---------------------------------------------------------------- text helpers
FENCE = {'py': 'python', 'python': 'python', 'pycon': 'python', 'text': 'output',
         'sh': 'bash', 'shell': 'bash', 'bash': 'bash'}


def fences(t):
    return re.sub(r'^(\s*)```(\w+)\s*$', lambda m: m.group(1) + '```' + FENCE.get(m.group(2), m.group(2)), t, flags=re.M)


def links(t, src_rel, here):
    """Rewrite relative links in text from source file src_rel for a page in folder `here`."""
    base = posixpath.dirname(src_rel)

    def fix(m):
        label, url = m.group(1), m.group(2)
        if re.match(r'^(https?:|mailto:|#)', url):
            return m.group(0)
        path, _, frag = url.partition('#')
        target = posixpath.normpath(posixpath.join(base, path))
        if target.startswith('assets/data/'):
            return f'[{label}](data/{target[len("assets/data/"):]})'
        if target.startswith('assets/files/'):
            return f'[{label}](files/{target[len("assets/files/"):]})'
        if target in ('assets/data', 'assets/data/', 'assets/files', 'assets/files/'):
            return f'[{label}](data/course-data.zip)'   # web hosts do not list folders
        code = re.match(r'weeks/week-\d/lessons/(\d\.\d)_code(/.*)?$', target)
        if code:
            return f'[{label}](files/code/{code.group(1)}{code.group(2) or "/"})'
        if target in TARGET:
            folder, name = TARGET[target]
            rel = name if folder == here or name.startswith('files/') else f'../{folder}/{name}'
            return f'[{label}]({rel}{"#" + frag if frag else ""})'
        if target.endswith('README.md') and target.count('/') <= 1:
            return f'[{label}](index.md)' if here == 'episodes' else f'[{label}](../index.md)'
        print('  unmapped link in', src_rel, '->', url)
        return m.group(0)
    return re.sub(r'(?<!!)\[([^\]]*)\]\(([^)\s]+)\)', fix, t)


def placeholders(t):
    t = re.sub(r'`assets/images/week-\d/([\w.-]+\.png)`', r'`episodes/fig/\1`', t)
    return re.sub(r'\(\.\./\.\./\.\./assets/images/week-\d/([\w.-]+\.png)\)', r'(fig/\1)', t)


def drop_nav(t):
    t = re.sub(r'^\[<< Back to[^\n]*\n?', '', t, flags=re.M)
    t = re.sub(r'^\[Back to[^\n]*\n?', '', t, flags=re.M)
    return t


def strip_section_header(t):
    """Remove title, week line, back link and Contents list from a lesson section."""
    lines = t.split('\n')
    out, i = [], 0
    # skip until the end of the Contents list
    while i < len(lines) and not lines[i].startswith('## Contents'):
        i += 1
    i += 1
    while i < len(lines) and (lines[i].strip() == '' or lines[i].lstrip().startswith('- [')):
        i += 1
    body = '\n'.join(lines[i:])
    body = re.sub(r'^# Section [\d.]+\s*\n', '', body, flags=re.M)   # stray H1s
    return body


def challenges(t):
    """Wrap the exercises section in Workbench challenge blocks."""
    m = re.search(r'^## (?:💻 )?Exercises[^\n]*\n', t, flags=re.M)
    if not m:
        return t
    head, ex = t[:m.start()], t[m.end():]
    parts = re.split(r'^### (Exercises?:? ?Level \d|Level \d)[^\n]*\n', ex, flags=re.M)
    blocks = []
    if len(parts) == 1:
        blocks.append(('Exercises', parts[0]))
    else:
        if parts[0].strip():
            blocks.append(('Exercises', parts[0]))
        for k in range(1, len(parts), 2):
            name = re.sub(r'^Exercises?:? ?', '', parts[k]).strip()
            blocks.append((f'Exercises: {name}', parts[k + 1]))
    out = head.rstrip() + '\n\n'
    for title, body in blocks:
        out += f'::::::::::::::::::::::::::::::::::::: challenge\n\n## {title}\n\n{body.strip()}\n\n::::::::::::::::::::::::::::::::::::::::::::::::\n\n'
    return out


def bridge_blocks(t):
    """Turn 'Activity' + following 'Model answer' sections into a challenge with a solution."""
    m = re.search(r'^## (Activity[^\n]*)\n(.*?)^## (Model answers?[^\n]*)\n(.*?)(?=^## |\Z)', t, flags=re.M | re.S)
    if not m:
        return t
    block = (f'::::::::::::::::::::::::::::::::::::: challenge\n\n## {m.group(1)}\n\n{m.group(2).strip()}\n\n'
             f':::::::::::::::: solution\n\n## {m.group(3)}\n\n{m.group(4).strip()}\n\n:::::::::::::::::::::::::\n'
             f'::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
    return t[:m.start()] + block + t[m.end():]


def drop_day_column(t):
    """Remove a leading 'Day' column from markdown tables (source-day numbers must not show)."""
    out, in_day_table = [], False
    for line in t.split('\n'):
        if re.match(r'^\|\s*Days?\s*\|', line):
            in_day_table = True
        if in_day_table and line.startswith('|'):
            line = '|' + line.split('|', 2)[2]
        elif not line.startswith('|'):
            in_day_table = False
        out.append(line)
    return '\n'.join(out)


def box(kind, items):
    body = '\n'.join(f'- {x}' for x in items)
    return f':::::::::::::::::::::::::::::::::::::: {kind}\n\n{body}\n\n::::::::::::::::::::::::::::::::::::::::::::::::\n'


def page(title, teaching, exercises, q, o, k, body):
    head = f"---\ntitle: '{title}'\nteaching: {teaching}\nexercises: {exercises}\n---\n\n"
    return head + box('questions', q) + '\n' + box('objectives', o) + '\n' + body.strip() + '\n\n' + box('keypoints', k)


def clean(t, src_rel, here):
    return placeholders(links(fences(drop_nav(t)), src_rel, here)).strip() + '\n'


def read(rel):
    with open(os.path.join(SRC, rel), encoding='utf-8') as f:
        return f.read()


def write(folder, name, text):
    path = os.path.join(DST, folder, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


# ---------------------------------------------------------------- build
order = []
for w, theme in WEEKS.items():
    watch, rp, bridge_min, build = TIME[w]
    secs = [s for s in SECTIONS if s.startswith(f'{w}.')]

    # overview
    rel = f'weeks/week-{w}/README.md'
    t = read(rel)
    t = re.sub(r'^# [^\n]*\n', '', t, count=1)
    t = drop_day_column(clean(t, rel, 'episodes'))
    q = [f'What will I learn in Week {w}?', 'How should I spend my time this week?']
    o = [f'Plan your Week {w} study time using the time plan.', 'Find the videos, sections, Concepts Bridge and practice task for the week.']
    k = ['Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.', 'The whole week fits in 6 hours or less.']
    name = f'week-{w}-overview.md'
    write('episodes', name, page(f'Week {w}: {theme}', watch, 0, q, o, k, t))
    order.append(name)

    # sections
    per = rp // len(secs)
    for s in secs:
        m = SECTIONS[s]
        t = strip_section_header(read('weeks/' + m['src']))
        t = challenges(clean(t, 'weeks/' + m['src'], 'episodes'))
        name = sec_file(s, m['slug'])
        write('episodes', name, page(f"{s} {m['title']}", round(per * 0.6), round(per * 0.4), m['q'], m['o'], m['k'], t))
        order.append(name)

    # bridge
    rel = f'weeks/week-{w}/bridge.md'
    t = read(rel)
    t = re.sub(r'^# [^\n]*\n', '', t, count=1)
    t = bridge_blocks(clean(t, rel, 'episodes'))
    b = BRIDGES[w]
    name = f'week-{w}-bridge.md'
    write('episodes', name, page(f"Week {w} Concepts Bridge: {b['title']}", 20, 10, b['q'], b['o'], b['k'], t))
    order.append(name)

    # practice
    pm = PRACTICE[w]
    rel = f'weeks/week-{w}/practice/README.md'
    t = read(rel)
    t = re.sub(r'^# [^\n]*\n', '', t, count=1)
    t = clean(t, rel, 'episodes')
    files = '\n'.join(f'- [{posixpath.basename(f)}](files/week-{w}/{f})' for f in pm['files'])
    dl = (':::::::::::::::::::::::::::::::::::::::: callout\n\n## Files for this task\n\n'
          'Download these files into a folder for this task and open the folder in PyCharm.\n\n'
          f'{files}\n\n:::::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
    t = dl + t
    if 'extra_readme' in pm:
        rel2 = f'weeks/week-{w}/practice/{pm["extra_readme"]}'
        extra = read(rel2)
        extra = re.sub(r'^# ([^\n]*)\n', r'## \1\n', extra, count=1)
        extra = re.sub(r'^(#{2,5}) ', lambda mm: '#' + mm.group(1) + ' ', extra, flags=re.M)
        extra = re.sub(r'^### ', '## ', extra, count=1, flags=re.M)
        t += '\n' + clean(extra, rel2, 'episodes')
    pq, po, pk = PRACTICE_Q[w]
    name = f'week-{w}-practice.md'
    write('episodes', name, page(f"Week {w} {pm['title']}", 0, build, pq, po, pk, t))
    order.append(name)
    for f in pm['files']:
        dst = os.path.join(EP, 'files', f'week-{w}', f)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(os.path.join(W, f'week-{w}', 'practice', f), dst)

# optional sections as learner pages
learner_pages = []
for s, m in OPTIONAL.items():
    t = strip_section_header(read('weeks/' + m['src']))
    t = challenges(clean(t, 'weeks/' + m['src'], 'learners'))
    name = sec_file(s, m['slug'])
    note = (f'::::::::::::::::::::::::::::::::::::: callout\n\n## Optional section\n\n'
            f'This section is optional. It belongs with Week {s[0]}, but nothing in the course depends on it.\n\n'
            '::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
    write('learners', name, f"---\ntitle: '{s} {m['title']} (optional)'\n---\n\n" + note + t)
    learner_pages.append(name)

# lesson code folders (e.g. 6.1_code) -> episodes/files/code/6.1/
for w in WEEKS:
    lessons = os.path.join(W, f'week-{w}', 'lessons')
    for d in os.listdir(lessons):
        if d.endswith('_code'):
            shutil.copytree(os.path.join(lessons, d), os.path.join(EP, 'files', 'code', d[:-5]),
                            ignore=shutil.ignore_patterns('__pycache__'), dirs_exist_ok=True)

# data and example files
for sub in ('data', 'files'):
    src = os.path.join(SRC, 'assets', sub)
    for f in os.listdir(src):
        shutil.copyfile(os.path.join(src, f), os.path.join(EP, sub, f))

# one zip with the data/ and files/ folders, for learners to download in one go
import zipfile
with zipfile.ZipFile(os.path.join(EP, 'data', 'course-data.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
    for sub in ('data', 'files'):
        for f in sorted(os.listdir(os.path.join(SRC, 'assets', sub))):
            z.write(os.path.join(SRC, 'assets', sub, f), f'IntroToProgramming/{sub}/{f}')

with open(os.path.join(DST, '.episode_order'), 'w') as f:
    f.write('\n'.join(order))
with open(os.path.join(DST, '.learner_order'), 'w') as f:
    f.write('\n'.join(learner_pages))
print(len(order), 'episodes,', len(learner_pages), 'optional learner pages')
