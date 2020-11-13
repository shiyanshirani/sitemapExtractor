import requests 
from bs4 import BeautifulSoup

def fetch(url):
    req = requests.get(url)  # gets url's data
    xml = req.text  # convert the recieved data to text
    soup = BeautifulSoup(xml, features='html.parser')  # beautifies using Beautifulsoup
    sitemapTags = soup.find_all("loc")  # bs4.method (find_all) to find subchild containing sitemap.xml data
    return [x.text for x in sitemapTags]  # returns a list of all sitemap's data



def newFile(data):
    fh = open('sitemap.xml', 'w')
    for sitemapData in data:
        fh.write(sitemapData)
        fh.write("\n")
    fh.close()


url = "https://writemaps.com/sitemap.xml/" # example url used 

# url_input = input("Enter desired url in the following format (www.abcd.xyz) :")
# url_input = 'https://'+ url_input+'/sitemap.xml'

# exception handling if url fails to respond
try:
    result = fetch(url)
    newFile(result)
except:
    print("Desired URL does not have sitemap.xml embedded")