#!/usr/bin/env python
# coding: utf-8



import pandas as pd




from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager




# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)





# Visit the Quotes to Scrape site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)





# Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')





slide_elem.find('div', clsas_='content_title')





# use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title




news_title_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_title_p


# ## Featured Images




# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)





# find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()




# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[91]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel





# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url




df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df




df.to_html()





browser.quit()





def mars_news(browser):
    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)
    
    # Convert the browser html to a soup objext and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    # Add try/except for error handling
    try:
    
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first <a> tag and save it as 'news_title'

        slide_elem.find('div', class_='content_title')
    
        news_title = slide_elem.find('div', class_='content_title').get_text()
    
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None
    
    return news_title, news_p





def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    
    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()
    
    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    # Add try/except for error handling
    try: 
        # Find the relative image url
        image_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    
    except AttributeError:
        return None
    
    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url




def mars_facts():
    # Add try/except for error handling
    try:
        # use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()





# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager





# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)




# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)





# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')





slide_elem.find('div', class_='content_title')





# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title





# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p




# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)





# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()





# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup





# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel





# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url




df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()





df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df





df.to_html()





# 1. Use browser to visit the URL 
url2 = 'https://marshemispheres.com/'

browser.visit(url2)




# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Get a list of the hemispheres
links = browser.find_by_css('a.product-item img')

# Next, loop through those links, click the link, find the sample anchor, return the href
for i in range(len(links)):
    hemispheres = {}

    # We have to find the elements on each loop to avoid a stale element exception
    browser.find_by_css('a.product-item img')[i].click()

    # Next, we find the Sample image anchor tag and extract the href
    sample_elem = browser.links.find_by_text('Sample').first

    hemispheres['img_url'] = sample_elem['href']

    # Get Hemisphere title
    hemispheres['title'] = browser.find_by_css('h2.title').text

    # Append hemisphere object to list
    hemisphere_image_urls.append(hemispheres)

    # Finally, we navigate backwards
    browser.back()


# 4. Print the list that holds the dictionary of each image url and title.
print(hemisphere_image_urls)





# 5. Quit the browser
browser.quit()

