---
title: '5.2 File Handling'
teaching: 30
exercises: 20
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I save data and read it back later?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Read and write text files with open() and with.
- Read and write JSON and CSV files.

::::::::::::::::::::::::::::::::::::::::::::::::

## File Handling

So far we have seen different Python data types. We usually store our data in different file formats. In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section. First, let us get familiar with handling files with common file format(.txt).

File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use _open()_ built-in function.

```python
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
```

- "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
- "a" - Append - Opens a file for appending, creates the file if it does not exist
- "w" - Write - Opens a file for writing, creates the file if it does not exist
- "x" - Create - Creates the specified file, returns an error if the file exists
- "t" - Text - Default value. Text mode
- "b" - Binary - Binary mode (e.g. images)

### Opening Files for Reading

The default mode of _open_ is reading, so we do not have to specify 'r' or 'rt'. I have created and saved a file named reading_file_example.txt in the files directory. Let us see how it is done:

```python
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'> - the encoding may differ on your computer
f.close()
```

As you can see in the example above, I printed the opened file and it gave  some information about it. Opened file has different reading methods: _read()_, _readline_, _readlines_. An opened file has to be closed with _close()_ method.

- _read()_: read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the *read(number)* method.

```python
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```output
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

Instead of printing all the text, let us print the first 10 characters of the text file.

```python
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```output
<class 'str'>
This is an
```

- _readline()_: read only the first line

```python
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```output
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_: read all the text line by line and returns a list of lines

```python
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```output
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

Another way to get all the lines as a list is using _splitlines()_:

```python
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

After we open a file, we should close it. There is a high tendency of forgetting to close them. There is a new way of opening files using _with_ - closes the files by itself. Let us rewrite the previous example with the _with_ method:

```python
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### Opening Files for Writing and Updating

To write to an existing file, we must add a mode as parameter to the _open()_ function:

- "a" - append - will append to the end of the file, if the file does not exist it creates a new file.
- "w" - write - will overwrite any existing content, if the file does not exist it creates.

The code below creates a new file, if the file does not exist:

```python
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file.\n')
```

Now let us append some text to the end of that file. Running this again adds the line again, because "a" never removes what is already there:

```python
with open('./files/writing_file_example.txt','a') as f:
    f.write('This text has to be appended at the end.\n')

with open('./files/writing_file_example.txt') as f:
    print(f.read())
```

```output
This text will be written in a newly created file.
This text has to be appended at the end.
```

### Deleting Files

To remove a file we use the _os_ module. Modules are explained in Week 6, so for now leave the `import os` line as is.

```python
import os
os.remove('./files/writing_file_example.txt')
```

If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:

```python
import os
if os.path.exists('./files/writing_file_example.txt'):
    os.remove('./files/writing_file_example.txt')
else:
    print('The file does not exist')
# The file does not exist - we already removed it above
```

## File Types

### File with txt Extension

File with _txt_ extension is a very common form of data and we have covered it in the previous section. Let us move to the JSON file

### File with json Extension

JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.

_Example:_

```python
# dictionary
person_dct = {
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": ["Python", "Excel", "SQL"]
}

# JSON: the same data as a string. JSON always uses double quotes
person_json = '{"name": "Jack", "country": "Australia", "city": "Perth", "skills": ["Python", "Excel", "SQL"]}'

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": ["Python", "Excel", "SQL"]
}'''
```

### Changing JSON to Dictionary

To change a JSON to a dictionary, first we import the json module and then we use _loads_ method.

```python
import json
# JSON
person_json = '''{
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": ["Python", "Excel", "SQL"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

```output
<class 'dict'>
{'name': 'Jack', 'country': 'Australia', 'city': 'Perth', 'skills': ['Python', 'Excel', 'SQL']}
Jack
```

### Changing Dictionary to JSON

To change a dictionary to a JSON we use _dumps_ method from the json module.

```python
import json
# python dictionary
person = {
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": ["Python", "Excel", "SQL"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)
```

When you print it, it does not have the quotes, but it is a string. JSON does not have its own type in Python: it is a string.

```output
<class 'str'>
{
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": [
        "Python",
        "Excel",
        "SQL"
    ]
}
```

### Saving as JSON File

We can also save our data as a json file. Let us save it as a json file using the following steps. For writing a json file, we use the json.dump() method, it can take dictionary, output file, ensure_ascii and indent.

```python
import json
# python dictionary
person = {
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": ["Python", "Excel", "SQL"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

In the code above, we use encoding and indentation. Indentation makes the json file easy to read.

### File with csv Extension

CSV stands for comma separated values. CSV is a simple file format used to store tabular data, such as a spreadsheet or database. CSV is a very common data format in data science.

**Example:**

```csv
"name","country","city","skills"
"Jack","Australia","Perth","Python"
```

**Example:**

```python
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a student. He lives in {row[2]}, {row[1]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
```

```output
Column names are :name, country, city, skills
        Jack is a student. He lives in Perth, Australia.
Number of lines:  2
```

### File with xlsx Extension

To read Excel files we need to install the _openpyxl_ package. Installing packages with pip is covered in Week 6, so for now just read this example; it will not run until openpyxl is installed.

```python
import openpyxl
workbook = openpyxl.load_workbook('sample.xlsx')
print(workbook.sheetnames)   # the names of the sheets, e.g. ['Sheet1']
```

### File with xml Extension

XML is another structured data format which looks like HTML. In XML the tags are not predefined. The first line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute.
**Example:XML**

```xml
<?xml version="1.0"?>
<person gender="male">
  <name>Jack</name>
  <country>Australia</country>
  <city>Perth</city>
  <skills>
    <skill>Python</skill>
    <skill>Excel</skill>
    <skill>SQL</skill>
  </skills>
</person>
```

For more information on how to read an XML file check the [documentation](https://docs.python.org/3/library/xml.etree.elementtree.html)

```python
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field:', child.tag)
```

```output
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
```

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 1

1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
   1) Read obama_speech.txt file and count number of lines and words
   2) Read michelle_obama_speech.txt file and count number of lines and words
   3) Read donald_speech.txt file and count number of lines and words
   4) Read melina_trump_speech.txt file and count number of lines and words
2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

   ```output
   # Your output should look like this
   print(most_spoken_languages('./data/countries_data.json', 10))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic'),
   (24, 'Spanish'),
   (9, 'Russian'),
   (9, 'Portuguese'),
   (8, 'Dutch'),
   (7, 'German'),
   (5, 'Chinese'),
   (4, 'Swahili'),
   (4, 'Serbian')]

   # Your output should look like this
   print(most_spoken_languages('./data/countries_data.json', 3))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic')]
   ```

3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

   ```output
   # Your output should look like this
   print(most_populated_countries('./data/countries_data.json', 10))

   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000},
   {'country': 'Indonesia', 'population': 258705000},
   {'country': 'Brazil', 'population': 206135893},
   {'country': 'Pakistan', 'population': 194125062},
   {'country': 'Nigeria', 'population': 186988000},
   {'country': 'Bangladesh', 'population': 161006790},
   {'country': 'Russian Federation', 'population': 146599183},
   {'country': 'Japan', 'population': 126960000}
   ]

   # Your output should look like this

   print(most_populated_countries('./data/countries_data.json', 3))
   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000}
   ]
   ```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 2

1. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
2. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

```output
    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

3. Use the function, find_most_frequent_words to find:
   1) The ten most frequent words used in [Obama's speech](data/obama_speech.txt)
   2) The ten most frequent words used in [Michelle's speech](data/michelle_obama_speech.txt)
   3) The ten most frequent words used in [Trump's speech](data/donald_speech.txt)
   4) The ten most frequent words used in [Melina's speech](data/melina_trump_speech.txt)
4. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of [Michelle's](data/michelle_obama_speech.txt) and [Melina's](data/melina_trump_speech.txt) speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of [stop words](data/stop_words.py) are in the data directory
5. Find the 10 most repeated words in the romeo_and_juliet.txt
6. Read the [hacker news csv](data/hacker_news.csv) file and find out:
   1) Count the number of lines containing python or Python
   2) Count the number lines containing JavaScript, javascript or Javascript
   3) Count the number lines containing Java and not JavaScript

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- Use with open(...) so the file closes itself.
- Mode "w" overwrites, "a" appends, "r" reads.
- json.dump() and json.load() save and load Python data.

::::::::::::::::::::::::::::::::::::::::::::::::
