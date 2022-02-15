#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[9]:


url = 'https://pumpolymp.com'


# In[10]:


links = []

website= requests.get(url)
website_text = website.text
soup = BeautifulSoup(website_text)


# In[11]:


for link in soup.find_all('a'):
    links.append(link.get('href'))
    
for link in links:
    print(links)
    
print(len(links))


# In[15]:


from bs4 import BeautifulSoup
import requests
import re
  
  
# function to extract html document from given url
def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
      
    # response will be provided in JSON format
    return response.text
  
    
# assign required credentials
# assign URL
url_to_scrape = "https://pumpolymp.com"


  
# create document
html_document = getHTMLdocument(url_to_scrape)
#print(test_to_scrape)
  
# create soap object
soup = BeautifulSoup(html_document, 'html.parser')
  
  
# find all the anchor tags with "href" 
# attribute starting with "https://"
for link in soup.find_all('a', 
                          attrs={'href': re.compile("^https://")}):
    # display the actual urls
    print(link.get('href')) 
print(len(link.get('href')))


# In[12]:


file = open("/Users/syedaliraza/Downloads/Scam_data.txt")
#print(file.read())
x= file.read()
#print(x)
def Find(x):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,x)      
    return [q[0] for q in url]
      
# Driver Code

print("Urls: ", Find(x))
print(len(Find(x)))
#print(x)
ls = Find(x)
#print(ls)
matches = []
 
for match in ls:
    if "https://t.me/" in match:
        matches.append(match)
print(matches)
print(len(matches))


# In[17]:


file = open("/Users/syedaliraza/Downloads/Scam_data.txt")
#print(file.read())
x= file.read()
#print(x)
def Find(x):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,x)      
    return [q[0] for q in url]
      
# Driver Code

print("Urls: ", Find(x))
print(len(Find(x)))
#print(x)
ls = Find(x)
#print(ls)
matches = []
 
for match in ls:
    if "https://t.me/" in match:
        matches.append(match)
print(matches)
print(len(matches))


# In[16]:


matches[1]


# In[ ]:


file = open("/Users/syedaliraza/Downloads/Scam_data.txt")
#print(file.read())
x= file.read()
#print(x)
def Find(x):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,x)      
    return [q[0] for q in url]
      
# Driver Code

print("Urls: ", Find(x))
print(len(Find(x)))
#print(x)
ls = Find(x)
#print(ls)
matches = []
 
for match in ls:
    if "https://t.me/" in match:
        matches.append(match)
print(matches)
print(len(matches))


# In[ ]:


import pickle

matcheslist = matches1.append(matches2)

with open('filename.pickle', 'wb') as handle:
    pickle.dump(matcheslist, handle, protocol=pickle.HIGHEST_PROTOCOL)

