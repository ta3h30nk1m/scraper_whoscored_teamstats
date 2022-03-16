Whoscored Scraper - Scraping team statistics (developed in Windows)

This is a scraper to collect data from whoscored.com, a football data site, by using selenium module.

Mainly looked up and copied from https://github.com/joseramon-arias/scraper-whoscored

First thing you should know is that there is a easier way to do scraping by using `requests` module in Python, 
but certain sites, like this whoscored.com, prevent and block the access for security reasons. 

`selenium` module actually open up the browser and scrap data from the browser page, 
so, it actually looks like user(person) accessing the website, avoiding the blockade. 

By this program, I scraped team statistics and its standings in different seasons. 

Here is some instructions how to use this scraper:

1. Download `selenium` module and appropriate driver for you by following instructions in 
    http://selenium-python.readthedocs.io/installation.html

2. Use pip to install these modules: unidecode, bs4
    `pip install unidecode`
    `pip install bs4`

3. Change PATH variables in `selenium_func.py` file to match your environment
    (`helper_functions.py` file contains functions that used often)

4. Change Paths and run accordingly (Read comments in each file for detail instruction):
    `get_detail_urls.py` --> `get_more_detail_urls.py` --> `get_stats.py` 

5. Done! You have created csv file that contains statistics from whoscored.com

