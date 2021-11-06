#!/usr/bin/env python
# coding: utf-8
# In[14]:

import pandas as pd

# In[1]:

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# In[2]:

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# In[3]:

# Visit the Quotes to Scrape site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# In[4]:

# Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# In[5]:

slide_elem.find('div', clsas_='content_title')

# In[6]:

# use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# In[7]:

news_title_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_title_p

# ## Featured Images

# In[8]:

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# In[9]:

# find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# In[11]:

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# In[12]:

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# In[13]:

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# In[15]:

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# In[16]:

df.to_html()

# In[17]:

browser.quit()