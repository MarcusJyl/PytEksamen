from bs4 import BeautifulSoup
import re
import requests
import model

def getInfos(bird):
    url = "https://www.allaboutbirds.org/guide/" + bird
    print(bird)
    # result = requests.get(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    c = result.content
    soup = BeautifulSoup(c)

    str1 = ""
    listen = []
    # print(soup)
    article = soup.find("ul", {"class":"LH-menu"}).find_all('span', {"class":"text-label"})
    for element in article:
        str1 = ""
        element = ''.join(element.findAll(text = True))
        elementList = re.findall('[A-Z][^A-Z]*', element)
        i = 0
        for ele in elementList:
            i += 1
            if(i>1):
                str1 += ele
            else:
                str1 += ele + ": " 
                  
        listen.append(str1)
        
    return listen

def getPicture(bird):
    url = "https://www.allaboutbirds.org/guide/" + bird
    # result = requests.get(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    result = requests.get(url, headers=headers)
    c = result.content
    soup = BeautifulSoup(c)
    pictures = soup.find("ul",{"class":"hero-menu"}).find_all('img')
    #print(pictures[0])
    picture = pictures[0]
    #print(type(picture))
    pic_urls = picture.get('data-interchange')
    pic_url = re.findall('[h]\S*jpg', pic_urls)[0]
    #print(pic_url)
    return pic_url

def getArticle(bird):
    url = "https://www.allaboutbirds.org/guide/" + bird
    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c)

    article_text = ''
    article = soup.find("div", {"class":"speciesInfoCard float clearfix"}).findAll('p')
    for element in article:
        article_text += '\n' + ''.join(element.findAll(text = True))
        
    article_text += '\n\nCool facts \n'
    article2 = soup.find("div", {"class":"accordion-content"}).findAll('li')
    for element in article2:
        article_text += '\n' + ''.join(element.findAll(text = True)) + "\n"
    return article_text

def processBirdName(bird_path):
    bird = model.run_example(bird_path)
    bird2 = bird[0].replace(" ", "_")
    bird3 = bird2.replace("'","")
    bird3 = re.sub(r'(\_\(.*?\))', '', bird3)
    bird4 = bird3.replace(" ","")
    return (bird4, bird[1])

def modelFinal(path):
    bird = processBirdName(path)
    print(bird)
    info = getInfos(bird[0])
    picture = getPicture(bird[0])
    article = getArticle(bird[0])

    return (bird[0], info, article, bird[1])


