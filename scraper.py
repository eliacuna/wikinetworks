"""
Project Name: Wiki Networks

Author: Elijah Acuna - Senior at the University of Arizona

Description: This personal project aims to take the classic "Wiki Racer" problem and implement it
using Graph Networks and Multithreading Parallelization. Upon completion of the algorithm and 
data processing elements of this problem, some graphic representation or the networks will be 
implemented using Jupyer Notebooks and perhaps LaTeX.
Ideally, this project will be able to illustrate edge connections between 3 or more "main pages"
which are chosen by the user and display all shortest path connections between the main pages.
A completed shortest path between two pages is a ladder of pages that are linked in the HTML from 
one Wiki article to another.

Current Checkpoint: Currently, the user is able to input one valid Wikipedia article title and receive
a complete set of all Wikipedia articles linked within that same article.
"""

import urllib.request # import the library we use to open URLs
from bs4 import BeautifulSoup # import beautiful soup for web scraping

def getValidPageNames(p1_links):
    # we only want pages that start with the wiki page link
    valid_parse = '<a href="/wiki/'
    
    # use the 'find_all' function to bring back all instances of the 'a' tag in the HTML
    all_links = p1_links.find_all("a")
    valid_links = []
    page_names = []
    
    for link in all_links:
        if str(link).startswith(valid_parse) and ':' not in str(link) and not str(link).endswith('</a'):
            valid_links += [str(link)]
    
    for link in valid_links:
        article_end = link.find('" ')
        page_names += [link[15:article_end]]
        
    return page_names
    


def main():
    # initialize the list that contains our BFS path
    path = []
    
    # standard URL that precedes article titles
    url = "https://en.wikipedia.org/wiki/"
    # get starting page to input
    page_one = input("Where do you want to begin? ")
    # get ending page to input
    page_two = input("Where do you want to end? ")
    # create working links
    page_one = url + page_one
    page_two = url + page_two

    # open the urls using urllib.request and put the HTML into the variables
    p1_html = urllib.request.urlopen(page_one)

    # parse the HTML from our URL into the BeautifulSoup parse tree format
    p1_links = BeautifulSoup(p1_html, "lxml")
    
    page_names = getValidPageNames(p1_links)
    
    for page in page_names:
        print(page)
        
    
    print("done")
    
main()