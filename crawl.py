import requests
from bs4 import BeautifulSoup


def sendRequest(URL):
    response = requests.get(URL)
    if response.status_code != 200:
        return "There was a problem"
    else:
        return response


def extractLinks(response):
    soup = BeautifulSoup(response.content, 'lxml')
    links = soup.find_all('a', href=True)
    links = cleanList(links)
    return links


def cleanList(links):
    linkList = []
    for link in links:
        linkList.append(link['href'])

    needToRemove = []
    for i in linkList:
        if i[:4] != 'http':
            needToRemove.append(i)
    for i in needToRemove:
        linkList.remove(i)
    return linkList


def crawler(URL):
    response = sendRequest(URL)
    links = extractLinks(response)

    visitedLinks = {"Sample", }
    for i in links:
        if i not in visitedLinks:
            print("Your Crawler crawling at:", i)
            try:
                crawlerResponse = sendRequest(i)
                crawlerlinks = extractLinks(crawlerResponse)
                links.extend(crawlerlinks)
                visitedLinks.add(i)
            except Exception as e:
                print(f"Cannot Connect to {i}:",e)

if __name__ == "__main__":
    # URL = "https://aimicrodegree.org/"
    # URL = "https://edunetfoundation.org/"
    URL = "https://www.thehindu.com/news/national/faridabad-police-forms-sit-to-probe-al-falah-universitys-activities/article70305959.ece"

    crawler(URL)