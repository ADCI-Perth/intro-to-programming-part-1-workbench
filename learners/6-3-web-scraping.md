---
title: '6.3 Web Scraping (optional)'
---

::::::::::::::::::::::::::::::::::::: callout

## Optional section

This section is optional. It belongs with Week 6, but nothing in the course depends on it.

::::::::::::::::::::::::::::::::::::::::::::::::

## Python Web Scraping

### What is Web Scrapping

The internet is full of huge amount of data which can be used for different purposes. To collect this data we need to know how to scrape data from a website.

Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.

In this section, we will use beautifulsoup and requests package to scrape data. The package version we are using is beautifulsoup 4.

To start scraping websites you need _requests_, _beautifulsoup4_ and a _website_.

```bash
python -m pip install requests
python -m pip install beautifulsoup4
```

To scrape data from websites, basic understanding of HTML tags and CSS selectors is needed. We target content from a website using HTML tags, classes or/and ids.
Let us import the requests and BeautifulSoup module

```python
import requests
from bs4 import BeautifulSoup
```

Let us declare a url variable for the website we are going to scrape. We will use https://quotes.toscrape.com, a website built for people learning web scraping, so it is fine to practise on it.

```python
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

# Let's use the requests get method to fetch the data from url
response = requests.get(url)
# let's check the status
status = response.status_code
print(status) # 200 means the fetching was successful
```

```output
200
```

Using beautifulSoup to parse content from the page

```python
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>Quotes to Scrape</title>
print(soup.title.get_text()) # Quotes to Scrape

# Each quote on the page is inside <div class="quote">
quotes = soup.find_all('div', class_='quote')
print(len(quotes)) # 10 - the number of quotes on the first page

# We can select using id, class or HTML tag, for more information check the beautifulsoup doc
first = quotes[0] # the result is a list, we take the first item
print(first.find('small', class_='author').get_text()) # Albert Einstein
print(first.find('span', class_='text').get_text())    # the text of the quote
```

If you run this code, you can see that we have only extracted the first quote. Getting all the quotes, with their authors and tags, is part of exercise 1.

For reference check the [beautifulsoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

::::::::::::::::::::::::::::::::::::: challenge

## Exercises

1. Scrape all the quotes on https://quotes.toscrape.com (text, author and tags) and store them as a JSON file.
1. Scrape the following website and store the data as json file (url = 'https://www.bu.edu/president/boston-university-facts-stats/'). An example result is in `6.3_code/scrapped_data.json`.
1. Scrape the title and price of every book on the first page of https://books.toscrape.com and change it to a JSON file
1. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

::::::::::::::::::::::::::::::::::::::::::::::::

