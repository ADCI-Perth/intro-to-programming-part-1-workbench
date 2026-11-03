---
title: 'Instructor Notes'
---

## About this course

- Six weeks, **hard cap of 6 hours per week** (36 hours in total). Weeks 4 to 6 come in under 6 hours on purpose; the spare time is a buffer.
- Complete beginners, mostly working adults: people in office jobs who want to change career or move into programming or computing. Assume no programming or technical background and no maths beyond everyday arithmetic. Weeks 1 to 3 lean on video; Weeks 4 to 6 shift towards independent problem solving.
- Videos are third-party YouTube content: mainly the Telusko *Python for Beginners (Full Course)* playlist (labelled **T#n**), plus a few short videos from other channels (labelled **[Channel]**). Check every link before each intake.
- Editor: **PyCharm** (free core). VS Code is the fallback if the PyCharm licence ever changes.

## Weekly structure

Each week is one episode. Inside it are the week overview, the core sections, a 30-minute **Concepts Bridge** and a **practice task**, each a level-2 heading so they show as sub-items in the menu. The overview's time plan is the source of truth for timings; the `teaching` and `exercises` minutes on each episode are estimates based on it.

| Week | Watch | Read & practise | Bridge | Build | Total |
|---|---|---|---|---|---|
| 1 | 1 h 22 m | 2 h 4 m | 30 m | 2 h | 5 h 56 m |
| 2 | 59 m | 2 h 31 m | 30 m | 2 h | 6 h |
| 3 | 1 h 22 m | 2 h 8 m | 30 m | 2 h | 6 h |
| 4 | 53 m | 2 h | 30 m | 2 h | 5 h 23 m |
| 5 | 1 h 24 m | 1 h 40 m | 30 m | 2 h | 5 h 34 m |
| 6 | 49 m | 1 h | 30 m | 3 h | 5 h 19 m |

## Practice tasks

- The tasks are **practice only and are not marked**. Assessment has not been designed yet; do not add graded tasks, weightings or exams to this lesson until it is.
- Every task has starter code, a model solution and pytest tests in its files list.
- Weeks 5 and 6 share one mini project (a library-loan manager). The `Book` and `Library` interface must stay identical between the two weeks.

## Teaching tips

- Course code only uses ideas already taught. Where a later idea is unavoidable (for example `if __name__ == "__main__":` or `import` before Week 6), the notes tell learners to leave it as is and say which week explains it. Keep to this when you edit examples.
- Set outputs (`{...}`) can print in a different order on each run. The notes say so; reassure learners who see a different order.
- Outputs that depend on the clock (Section 5.3) or on live websites (Sections 6.2 and 6.3) will differ from the notes.

## Before publishing outside ADCI

- The lesson sections were adapted from an open-source *30 Days of Python* repository that has **no licence file**, so reuse rights are unclear. Check this before publishing the site publicly or confirming the `license` in `config.yaml`.
- The lesson uses The Carpentries Workbench for layout only; it is not a Carpentries lesson. The `carpentry: 'adci'` setting avoids Carpentries branding, and the ADCI logo comes from ADCI's fork of the theme (`varnish: 'ADCI-Perth/varnish'` in `config.yaml`; see `branding/`).
- Replace the placeholder `contact` email in `config.yaml`.
