# Import dependencies
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

news_url = 'https://redplanetscience.com/'
image_url = 'https://spaceimages-mars.com'
table_url = 'https://galaxyfacts-mars.com'
hemi_url = 'https://marshemispheres.com'


def Scrape():
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    response = requests.get(news_url)
    soup = bs(response.text, 'html.parser')
    title = soup.find('div',class_='content_title')
    para = soup.find('div',class_='article_teaser_body')
    # return title
    # return para

    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(image_url)
    html = browser.html
    soup = bs(html,'html.parser')
    browser.links.find_by_partial_text('FULL IMAGE').click()
    html = browser.html
    soup = bs(html,'html.parser')
    featured_image_url = url + soup.find('img',class_='fancybox-image')['src']
    # return featured_image_url
    browser.quit()

    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(table_url)
    html = browser.html
    soup = bs(html,'html.parser')
    fact_table = soup.find('table',class_='table table-striped')
    fact_table_df = pd.read_html(str(fact_table))[0]
    # return fact_table_df
    browser.quit()

    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(hemi_url)
    mars_dict = []
    for x in range(4):
        html = browser.html
        soup = bs(html,'html.parser')
        hemi_name = soup.find_all('h3')[x].text
        browser.links.find_by_partial_text(hemi_name).click()
        html = browser.html
        soup = bs(html,'html.parser')
        hemi_image = url + "/" + soup.find('li').a['href']
        # return hemi_name
        # return hemi_image
        mars_dict.append({"title" : hemi_name, "img_url" : hemi_image})
        browser.back()
    browser.quit()

    mars_data = {'news title': title,
                    'news paragraph': para,
                    'featured image url':featured_image_url,
                    'fact table': fact_table_df,
                    'hemispheres': mars_dict
        }
    return mars_data
    print(mars_data)