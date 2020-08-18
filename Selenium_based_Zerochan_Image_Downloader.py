from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time, codecs, requests, os, wget
from os import path

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

def downloader():
    driver.quit()
    f = open('links.txt', 'r+')

    a = f.readlines()

    for link in a:
        #print(line) # Comment after testing
        fileDownload = link.rstrip('\n') # Remove the endline to download images
        wget.download(fileDownload, downloadPath) # Download images using wget

    f.truncate(0)
    f.close()
    print('\nThank you!')
    print('Going to main...')
    time.sleep(5)
    main()

def taker(): # Search the page for downloadable images
    print("Searching " + str(maxPageCount) + " pages.")
    print('Fetching links...this may take a while.')

    f = open('links.txt', 'w+') # Temporary storage for links
    link_take = soup2.find_all('a', href=True) # Find all download links

    for i in link_take:
        text = i['href'] # Separate the ones needed
        #print(text) # Comment after testing
        if 'https://static.zerochan.net/' in text:
            #print(text) # Comment after testing
            f.write(text + '\n') # And store into file 

    x = 1

    while True:
        if x >= maxPageCount: # Check if max pages is reached
            f.close()
            downloader()
        else:
            #print(x) # Comment after testing
            nextPage = driver.find_element_by_class_name('pagination')
            movePage = nextPage.find_element_by_partial_link_text('Next')
            movePage.send_keys(Keys.RETURN)

            time.sleep(10) # 10 second delay before getting links to make sure everything is loaded
                           # Necessary for Selenium 
            content = driver.page_source
            soup = bs(content, 'html.parser')
            link = soup.find_all('a', href=True)

            for i in link:
                text = i['href']
                #print(text) # Comment after testing
                if 'https://static.zerochan.net/' in text:
                    #print(text) # Comment after testing
                    f.write(text + '\n') # And store into file 

            x = x + 1

    f.close()

def searcher(int):
    log = int
    global soup2, maxPageCount

    if log == 1:
        driver.get('https://www.zerochan.net/')
    else:
        pass

    search = driver.find_element_by_name('q')
    search.send_keys(dirName)
    search.send_keys(Keys.RETURN)

    time.sleep(10) # 10 second delay before getting links to make sure everything is loaded
                   # Necessary for Selenium 
    content = driver.page_source
    soup = bs(content, 'html.parser')
    soup2 = soup
    #print(soup.prettify()) # Comment after testing

    linkPage = soup.find('p', class_='pagination').getText()

    s1 = linkPage.replace('\n\tpage 1 of ', '')
    if 'Next' in s1:
        if 'Last' in s1:
            s2 = s1.replace('\tNext »\n','').replace('Last\n', '')
        else:
            s2 = s1.replace('\tNext »\n','')
    pcount = s2

    print('Max pages found: ' + str(pcount) + ' pages.')
    pages = input('How many pages to search? ')
    maxPageCount = pages

    taker()

def login(): # Login to Zerochan
    username = input('Username: ')
    password = input('Password: ')

    driver.get('https://www.zerochan.net/login?ref=%2F')
    uname = driver.find_element_by_name('name')
    uname.send_keys(username) # Change into your own username
    pword = driver.find_element_by_name('password')
    pword.send_keys(password) # Change into your own password
    pword.send_keys(Keys.RETURN)

    searcher(0)


def dir(): # Make a new directory where to download
    set_address = path.expanduser('~\\Desktop\\') + search_name # Makes a new directory in Desktop

    global downloadPath
    downloadPath = set_address

    if not path.isdir(set_address): # Check if folder exists, else make a new one
        os.mkdir(set_address)

    #print(set_address) # Comment after testing
    
    logCheck = input('Do you wish to login? (Y/N) ')

    if logCheck == 'Y' or logCheck == 'y':
        login()
        log = true
    elif logCheck == 'N' or logCheck == 'n':
        searcher(1)
    else:
        dir()

def main():
    os.system('CLS')
    print("Selenium-based Zerochan Image Downloader v1")
    global dirName
    dirName = input("Name: ")

    global search_name
    search_name = dirName

    dir()

main()
