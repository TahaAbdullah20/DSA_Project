from bs4 import BeautifulSoup as bs
#import urllib.request as url

add =

for x in range(6):
    file = open("/Users/Taha/PycharmProjects/DSAproject_v_0.1/Violin - Simple English Wikipedia, the free encyclopedia.html")
    soup = bs(file,'html.parser')

    print(soup.get_text())
