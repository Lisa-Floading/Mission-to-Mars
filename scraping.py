#!/usr/bin/env python
# coding: utf-8

# In[34]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[21]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[22]:


#Assign URL for mars NaSA news site and instruct browser to visit it. 
#Search for elements with a specific combination of tag (div) and attribute (list_text)
#Telling browser to wait one second before searching for components in case pages take a while to load 
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[24]:


#Set up the HTML parser 
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[25]:


#Assign title and summary text to variables to be referenced later. 
#Begin scraping 
slide_elem.find('div', class_='content_title')


# In[26]:


# Use the parent element to find the first `a` tag and save it as `news_title`
#Get rid of extraneous HTML 
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[27]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[28]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[29]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[31]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[32]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[33]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[35]:


#Scrape table with Pandas function 
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:




