import pyperclip as pc 
from bs4 import BeautifulSoup as BS
import requests


url = "http://thebasscast.com"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
soup = BS(page.content, 'html.parser')
# print(soup.prettify())
print("If Bruce Contributes type 1 if Hot bite type 2")
decide = str(input())
if decide == '1':
    decide = "tdi_359"
    man = 1
elif decide == '2':
    decide = "tdi_362"
    man = 1
elif decide == '3':
    decide = "tdi_345"
    man = 1
# elif decide == '3':
    # decide = "tdi_345"
elif decide == '4':
    decide = "tdi_13"
    man = 1
else:
    print('paste link')
    man = 2
    HotBiteLink = input()
    HotBiteLink = str(HotBiteLink)
    
if man == 1:
    HotBite=soup.find("div", {"id": decide})
    HotBite=HotBite.find_all("a")
    print(HotBite[0].attrs['href'])
    HotBiteLink = HotBite[0].attrs['href']
else:
    pass
    
page = requests.get(HotBiteLink, headers=headers)
soup = BS(page.content, 'html.parser')
image=soup.find("div", {"class":"td-post-featured-image"})
image=image.find_all("a")
image=image[0].attrs['href']
print(image)

Title=soup.find("h1", {"class":"entry-title"})
Title=Title.get_text()
print(Title)

try:
    BodyText = soup.find('div',{'class':"td-post-content tagdiv-type"})
    BodyText = BodyText.find_all('p')
    BodyText = BodyText[0].get_text()
    BodyText = BodyText
    BodyText = BodyText[:250] + '...'
    BodyText = str(BodyText)
    print(BodyText)
except:
    BodyText = 'Check'

#%% Image Copy cell - DONE
PreImageSource = '<h1 class="null" style="text-align: center;"><img data-file-id="5586937" height="667" src='
PostImageSource = 'style="border: 0px initial ; width: 500px; height: 666px; margin: 0px;" width="500" /></h1>'
print('Paste the Image URL')
Image = '"' + image +'"'

FullImgLn=PreImageSource + Image + PostImageSource

#%% Header Cell - DONE
PreHeader = '<h1 class="null" style="text-align: center;"><u><strong><span style="font-size:26px"><span style="color:#624126">'
PostHeader = '</span></span></strong></u></h1>'
print('Paste the Header')
Header = Title

FullHeader=PreHeader + Header + PostHeader


#%% Text Cell
PreText = '<h2 class="null" style="text-align: center;"><span style="font-size:18px"><span style="color:#624126">'
PostText = '</span></span></h2>'
print('Paste your body text')
FullText = PreText + BodyText + PostText

#%% Hyperlink Cell - Done
PreHyper = '<h1 class="null" style="text-align: center;"><span style="font-size:18px"><a href='
PostHyper = ' target="_blank">CLICK HERE TO VIEW</a></span></h1>'
print('Paste Page Link')
Hyper = '"' + HotBiteLink +'"'

FullHyper  = PreHyper + Hyper + PostHyper

#%%
FinalHTML= FullImgLn + '\n' + FullHeader + '\n' + FullText + '\n' + FullHyper

pc.copy(FinalHTML)

