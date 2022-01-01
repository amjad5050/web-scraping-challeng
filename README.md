# web-scraping-challeng
In this assignment, I have built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines were followed:

Step 1 - Scraping
Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all of scraping and analysis tasks.
NASA Mars News
Scraped the Mars News Site and collected the latest News Title and Paragraph Text. Assigning the text to variables to reference later.
JPL Mars Space Images - Featured Image
Visited the url for the Featured Space Image site here.

Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.

Mars Facts
Visited the Mars Facts webpage here and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

Used Pandas to convert the data to a HTML table string.

Mars Hemispheres
Visited the astrogeology site here to obtain high resolution images for each of Mar's hemispheres.

Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys img_url and title.

Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
Step 2 - MongoDB and Flask Application
Using MongoDB with Flask templating to create a new HTML page that displayed all of the information that was scraped from the URLs above.

Started by converting Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that executes all of scraping code from above and returned one Python dictionary containing all of the scraped data.

Next, created a route called /scrape that import scrape_mars.py script and called scrape function.

Stored the return value in Mongo as a Python dictionary.
Created a root route / query Mongo database and pass the mars data into an HTML template to display the data.

Created a template HTML file called index.html that takes the mars data dictionary and displayed all of the data in the appropriate HTML elements.
