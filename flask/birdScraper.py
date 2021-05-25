from bs4 import BeautifulSoup
import re
import requests
import model

def getInfos(bird):
    url = "https://www.allaboutbirds.org/guide/" + bird
    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c)

    str1=""
    article = soup.find("ul", {"class":"LH-menu"}).findAll('span', {"class":"text-label"})
    for element in article:
        element = ''.join(element.findAll(text = True))
        elementList = re.findall('[A-Z][^A-Z]*', element)
        i = 0
        for ele in elementList:
            i += 1
            if(i>1):
                str1 += ele
            else:
                str1 += ele + ": " 
                  
        str1 += "\n"
    
    return str1

def getArticle(bird):
    url = "https://www.allaboutbirds.org/guide/" + bird
    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c)

    article_text = 'Basic description\n'
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
    bird2 = bird.replace(" ", "_")
    bird3 = bird2.replace("'","")
    bird3 = re.sub(r'(\_\(.*?\))', '', bird3)
    bird4 = bird3.replace(" ","")
    return bird4

def modelFinal(path):
    bird = processBirdName(path)
    info = getInfos(bird)
    article = getArticle(bird)

    return bird + " " + info + article

print(modelFinal("/home/jovyan/PytEksamen/VermillionFlycatcher.jpg"))
