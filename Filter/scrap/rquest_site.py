import json
import time
import requests
from bs4 import BeautifulSoup
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
  html_page = res.content
  soup = BeautifulSoup(html_page, 'html.parser')
  text = soup.find_all(text=True)
  output = ''
  blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
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

  output_list =  output.split()
  return output_list
  for i in output_list:
    print(len(output_list)) 
  with open("demofile3.txt", "w", encoding='utf-8') as f : 
    f.write(str(output.split()))
#keyword = "معدل السكر الطبيعي"
def lst_url (keyword):
  api_token = "e2b7c177ec596d6041b8ef4ae20995e4afea8f6c"
  headers = {
     'X-API-KEY': api_token,
     'Content-Type': 'application/json'}   
  titre1 = keyword

  pl = playload(titre1,"eg","ar" ,autocorrect=True)
  
  list_of_article_keyword = request_organic(pl.get(),headers)
  site_number = len(list_of_article_keyword)
  return list_of_article_keyword
#list_of_article_keyword = lst_url (keyword)
#for n in list_of_article_keyword : 
    #print("-------------------------------------")
    #print(n)
    #print("-------------------------------------")
#url = list_of_article_keyword[0]
#
'''basic_word_list = ["معدل السكر","معدل السكر الطبيعي حسب العمر","معدل السكر الطبيعي للصائم","السكر التراكمي الطبيعي","جدول السكر التراكمي الطبيعي","معدل السكر الطبيعي في سن الخمسين"]
full_list = [] 
for key in basic_word_list : 
  _list= [key]
  for url in list_of_article_keyword:
    words = get_site_word(url)
    print(len(words))
    list_key = key.split()

    counter = 0
    debut = 0
    end = len(list_key)
    while debut < len(words):
      if words[debut] == list_key[0]:
        for i in range(end) : 
          if words[debut] == list_key[i]:
            debut = debut+1
          else:
            counter = counter - 1
            break
        counter = counter + 1
      debut=debut+1
    print(counter)
    
    _list.append(counter)
  #print(_list)
  full_list.append(_list)

print(full_list)
with open("demofile3.txt", "w", encoding='utf-8') as f : 
    f.write(str(full_list))'''