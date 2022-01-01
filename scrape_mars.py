# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # return {"Name": "Amjad", "Age": 45}
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    # Scrape the [Mars News Site](https://redplanetscience.com/)
    # collect the latest News Title and Paragraph Text
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    # convertion
    html = browser.html
    planet_soup = soup(html, 'html.parser')
    # collect the latest News Title and Paragraph Text
    results = planet_soup.find('div', class_='content_title')
    # Assign the text to variables
    body = planet_soup.find('div', class_='article_teaser_body')

    ##featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
    spaceImage = 'https://spaceimages-mars.com'
    browser.visit(spaceImage)
    full_image_button = browser.find_by_tag('button')
    full_image_button.last.click()
    # convertion
    html = browser.html
    spcae_image_soup = soup(html, 'html.parser')
    # featured_image_url
    Image = spcae_image_soup.find('img', class_='fancybox-image')
    featured_image_url = spaceImage+'/'+Image.get('src')

    Mars_url = 'https://galaxyfacts-mars.com'
    Mars_df = pd.read_html(Mars_url)
    Mars_df = Mars_df[0]
    Mars_df.columns = ['Description', 'Mars', 'Earth']
    Mars_df = Mars_df.iloc[1:, ]
    Mars_html = Mars_df.to_html()
    Hemisphere_url = 'https://marshemispheres.com/'
    browser.visit(Hemisphere_url)
    image_links = browser.find_by_css("a.product-item img")
    hemisphere_list = []
    for i in range(len(image_links)):
        browser.find_by_css("a.product-item img")[i].click()
        # links[i].click()
        image_links1 = browser.find_by_text("Sample")
        image_links1 = image_links1.first
        url = image_links1['href']
        title_valles = browser.find_by_css("h2.title")
        sphere_dict = {"title": title_valles.text, "img_url": url}
        hemisphere_list.append(sphere_dict)
        browser.visit(Hemisphere_url)
    browser.quit()
    returned_dict = {"article_title": results.text,
                     "article_body": body.text,
                     "hemispheres": hemisphere_list,
                     "mars_table": Mars_html,
                     "featured_image": featured_image_url
                     }
    return returned_dict

if __name__ == "__main__":
    print("Running the code file and scraping, please be very very patient!")
    return_dict = scrape()
    print("The scrape data are:\n")
    print(return_dict)
