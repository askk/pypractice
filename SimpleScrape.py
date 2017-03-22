from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse



def scrape_html(url):
    try:
        html = urlopen(url)
        bsObject = BeautifulSoup(html.read(), "html.parser")
        print("url: " + url)
        #print(html.read())
        print(bsObject.h1)
    except IOError as err:
        print("url open error: " + str(err))


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="simple web scrape")
    parse.add_argument("--url", action="store", dest="url", required=True)

    params = parse.parse_args()
    url = params.url

    scrape_html(url)

