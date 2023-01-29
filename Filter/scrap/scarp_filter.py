import json
import time
import requests
from bs4 import BeautifulSoup
from random import randrange
black_list = ["img","iframe","strong"]
header = ["h1","h2","h3","h4","h5","h6"]
class playload():
  def __init__(self,keyword,country ,language ,autocorrect=True) :
    self.payload = json.dumps({
        "q": keyword,
        "gl": country,
        "hl": language,
        "autocorrect": autocorrect}) 
  def get(self):
    return self.payload
  def set(self,keyword,country ,language ,autocorrect=True):
    self.payload = json.dumps({
        "q": keyword,
        "gl": country,
        "hl": language,
        "autocorrect": autocorrect}) 

def request_organic(payload ,headers):
    url = "https://google.serper.dev/search"
    response = requests.request("POST", url, headers=headers, data=payload)
    #json_object = json.dumps(response.text, indent=4)
    res = json.loads(response.text)
    words = res["organic"]
    Section_keywords = []
    for word in words :
      Section_keywords.append(word["link"])
    return  Section_keywords
def get_site_word(url):
  res = requests.get(url)
  print(url)
  html_page = res.content
  soup = BeautifulSoup(html_page, 'html.parser')
  text = soup.find_all()
  #print([str(tag) for tag in soup.find_all()])
  output = ''
  blacklist = [
    'noscript',
    'header',
    'meta',
    'head', 
    'input',
    'script',
    'style'
    # there may be more elements you don't want, such as "style", etc.
  ]
  for t in text:
      if t.parent.name not in blacklist:
          if t != ''' 
          ''' :
            output += '{} '.format(t)
  output = ''
  for tag in soup.find_all():
    output += '{} '.format(str(tag))
    
  output_list =  output.split()
  with open("demofile3.txt", "w", encoding='utf-8') as f : 
    f.write(output)
  return output_list
  
class article : 
    def __init__(self,url):
      res = requests.get(url)
      self.counter = 0
      html_page = res.content
      self.header_list = []
      self.soup = BeautifulSoup(html_page, 'html.parser')
      try:
        self.article = self.soup.article.findChildren()
      except:
        self.article = self.soup.findChildren()
    def articl(self):
      return self.article
    def add_head(self,head):
        self.header_list.append(head)


class paragraphe ():
    def __init__(self,father,paragraph = ''):
        self.paragraph = paragraph
        self.serial_number = randrange(100000)
        self.father = father
        self.paragraph_object = []
    def add_paragraphe(self,p):
        self.paragraph = self.paragraph +"\n"+p
    def get_paragraph (self):
        return self.paragraph
    def paragraph_object(self):
        self.paragraph_object.append(self.father)
        self.paragraph_object.append(self.paragraph)
        return self.paragraph

class head :
    def __init__(self,txt,type,father = 0,children = []):
        self.type = type
        self.id = randrange(100000)
        self.children = children
        self.father = father
        self.text = txt
        self.para = ''
    def add_child (self,child):
        self.children.append(child)
    def add_txt (self,p):
      self.para = self.para +"\n"+p

#url="https://www.andalusiaegypt.com/%D9%85%D8%B9%D8%AF%D9%84-%D8%A7%D9%84%D8%B3%D9%83%D8%B1-%D8%A7%D9%84%D8%B7%D8%A8%D9%8A%D8%B9%D9%8A"
def getfull(url):
  res = requests.get(url)
  
  html_page = res.content
  soup = BeautifulSoup(html_page, 'html.parser')
  #print(soup.find_all('article'))

  #articl = soup.find_all('article')
  print("--------------scarp_filter-----------------")
  print(url)
  articl_object = article(url)
  articl = articl_object.articl()
  count = 0

  
  p = 0
  while p < len(articl):
      if articl[p].name not in black_list :
        if articl[p].name[0] == "h":
            h_ead = head(articl[p].get_text(),articl[p].name)
            p_aragraphe = paragraphe(h_ead.id)
            p =p+1
            while p < len(articl) and articl[p].name[0] != "h":
                  p_aragraphe.add_paragraphe(articl[p].get_text())
                  p =p+1
            h_ead.add_child(p_aragraphe)
            h_ead.add_txt(p_aragraphe.paragraph)
            articl_object.add_head(h_ead)
      
      if p < len(articl) and articl[p].name[0] != "h":  
         p = p+1
  return articl_object

#url="https://www.andalusiaegypt.com/%D9%85%D8%B9%D8%AF%D9%84-%D8%A7%D9%84%D8%B3%D9%83%D8%B1-%D8%A7%D9%84%D8%B7%D8%A8%D9%8A%D8%B9%D9%8A"

#articl_obj = getfull(url)
#lst = articl_obj.header_list
#he = lst [0]
#print((type(he.children.paragraph)))
'''
for h in lst : 
      print(h.text)
      print(h.type)
      print("---------------------")'''
'''
spaceq = "---------------------"
with open('scarp.txt', 'w',encoding='utf-8') as f:
    for elm in lst:
      
      #f.write(space+"\n")
      counter = 0
      f.write(spaceq+"\n")
      f.write(elm.text+"\n")
      f.write(elm.type + "\n")
      f.write(spaceq+"\n")
      par = elm.children
      f.write(par[0].get_paragraph()+"\n")
      '''    