from flask import Flask
from selenium import webdriver
from pdb import set_trace as bp


app = Flask(__name__)


# Main Page
@app.route('/')
def greeting():
    greeting = ("Hello! Thank you for checking out my wiki-searcher! <br> "
                "Please add a subdomain to the URL to search, <br> "
                "either in the address bar above (if on a browser), "
                "or using a cURL like utility to send a GET request.")
    return greeting


# Routing for subdomains and query
@app.route('/', subdomain='<query>')
def dynamic_query(query):
    # Instantiate variables for use in building the dictionary to return.
    dictionary = {}
    links = []

    # Start the Chrome webdriver
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)

    # Grab query string from GET request subdomain, convert to lowercase, and then capitalize the first letter to
    # be correct format for Wikipedia search.
    query_string = query.lower().capitalize()

    # GET request to Wikipedia with search query in URL.
    driver.get("https://en.wikipedia.org/wiki/%s" % query_string)

    # If Wikipedia returns multiple entries for the query, there is an <a> tag at the bottom of the page
    # with the title of "Help:Disambiguation." Check for this to know if we hit a page with multiple
    # entries or not.
    multiple_entries = driver.find_elements_by_xpath(
        "//a[@title='Help:Disambiguation']")

    # If that <a> tag is not present, put the current URL in the "links" list and set as the dictionary key "links"
    if not multiple_entries:
        links = driver.current_url
        dictionary["links"] = links

    # If that <a> tag is present, grab the hrefs for all the entries for the wikipedia search and build the dictionary with them.
    else:
        # Grab all <a> tag elements that are a descendant of the <div> with the class of "mw-parser-output"
        all_link_els = driver.find_elements_by_xpath(
            "//div[@class='mw-parser-output']/descendant::a")

        # Get the href attribute from each of the elements in the all_link_els list.
        all_links = [el.get_attribute('href') for el in all_link_els]

        # List of substrings to use to eleminate unwanted hrefs in the all_links list.
        exclusion_list = [
            "Disambig",
            "Special:WhatLinksHere",
            "%s" % query_string + "#",
            "wiktionary"
        ]

        # Create a list of links from all_links excluding the links that contain any of the substrings in exclusion_list.
        links = [
            link for link in all_links if not any(
                string in link for string in exclusion_list
            )
        ]

        dictionary["links"] = links

    # Close the window and quite the webdriver instance.
    driver.quit()

    # Return the built up dictionary.
    return dictionary


if __name__ == "__main__":
    website_url = 'wiki-search.com:5000'
    app.config['SERVER_NAME'] = website_url
    app.run()
