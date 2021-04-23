from bs4 import BeautifulSoup
import json
from selenium import webdriver

LAST_SERVICE = "Amazon Sumerian"


def main(url):
    """
    Gets data from a webpage using beautiful soup
    :param url: the URL to get content for
    :return: soup: the content in a BS4 object
    """
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

    driver.get(url)
    products = driver.find_element_by_link_text("Products")
    products.click()
    soup_file = driver.page_source
    driver.quit()

    services = {}

    soup = BeautifulSoup(soup_file, "html.parser")
    for div in soup.select('div[class=m-nav-panel-link]'):
        description = div.find('span')
        if description:
            description_txt = description.get_text()
            title_txt = div.get_text().replace(description_txt, "").strip("\n ")
            services[title_txt] = description_txt
            if LAST_SERVICE in title_txt:
                break

    with open('services.json', 'w') as fp:
        json.dump({"AWS Services": services}, fp, indent=4)


if __name__ == '__main__':
    main('https://aws.amazon.com')

