import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://methstreams.com/get-nflstreams/live').read()

soup = bs.BeautifulSoup(source,'lxml')

# title of the page
#print(soup.title)

# get attributes:
#print(soup.title.name)

# get values:
#print(soup.title.string)

# beginning navigation:
#print(soup.title.parent.name)

# getting specific values:
#print(soup.p)

for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

#print(soup.get_text())

print('run successful')

# to run in python3 - exec(open('/Users/matillionuser/Desktop/python/ucf_scraper.py').read())
# to run in terminal - python3 ucf_scraper.py