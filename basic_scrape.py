from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())

match = soup.title
print(match)

match2 = soup.title.text
print(match2)

match3 = soup.find('div', class_='footer')
print(match3)

article = soup.find('div', class_='article')
print(article)

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)

#find_all returns all the ele in a list format

for article in soup.find_all('div', class_= 'article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()