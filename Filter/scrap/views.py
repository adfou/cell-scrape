from django.http import HttpResponse
from random import randrange
from django.template import loader
from .models import Article,Head
from .scarp_filter import getfull
from .rquest_site import lst_url
from .filter import qayan_9yam
from django.shortcuts import render
from .models import Madjmo3at,fichie,word
import glob, os
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import fichieSerializer
import json
head_number = ["1","2","3","4","5","6","7","8"]
ponc =[',','.',':',';','،','"',"!","؟","."]      
no =['في']
debut = ['ال']
end = ['ي','ى']
def read_qyan(art):
    q_list_next_line = []
    with open(art+'.txt', 'r',encoding='utf-8') as f:
         for line in f:
          q_list_next_line.append(line)
    q_list = []
    for  q in range(len(q_list_next_line)):
       q_list.append(q_list_next_line[q].split("\n")[0])
    j = []
    for l in debut:
      for n in q_list:
        
        j.append( l + n )
        
    for k in j : 
      q_list.append(k)

    mp=[]
    for l in end:
      for n in j:
        
        mp.append( n+l )
    for k in mp : 
      q_list.append(k)
    
    j = []
    for l in end:
      for n in q_list:
        
        j.append( n+l )
    for k in j : 
      q_list.append(k)
    return q_list

def index(request):
    url = Article.objects.all()
    template = loader.get_template('scrap/index.html')
    context = {
        'latest_Article_list': url,
    }
    
    return render(request, 'scrap/index.html', context)
    
def detail(request, paragraph_id):
    return HttpResponse("You're looking at question %s." %  paragraph_id)

def results(request, paragraph_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response %  paragraph_id)

def paragraph_Qayan(request, paragraph_id):
    return HttpResponse("paragraph_Qayan %s." %  paragraph_id)
def result(request):
    return HttpResponse("paragraph_Qayan %s." %  paragraph_id)
''' def vote(request):
    #return HttpResponse("form %s." %  paragraph_id)

    #article = get_object_or_404(Article, pk=0)
    if request.method == "POST":
        print(request.POST["your_name"])
        url = request.POST["your_name"]
        
        #lst = articl_obj.header_list
        
        articl_obj =getfull(list_of_article_keyword[0]).header_list
        print(articl_obj[0].children)
        print("-------------------------")
        return render(request, 'scrap/dsplay.html', {
            'list':articl_obj ,
        })
    lst = lst_url("معدل السكر الطبيعي")
    print(lst)
    print("----------------------------")
    url = lst[0]
    words = getfull(url)
    for i in words.header_list :
        print(i.type)
        print(i.text)
    print(words.header_list )
    '''
'''madj = fichie.objects.all()
    txt = "تجارة"
    for i in madj :
        if i.text_f ==txt:
            
            
            print("----------------------------")
            with open("fares fles/"+txt+'.txt',  'r',encoding="utf8",errors='ignore') as f:
              for line in f:
               mo3a = word()
               #print((line.replace("\n", "")))
               mo3a.text_w = (line.replace("\n", ""))
               mo3a.father = i
               mo3a.save()'''
'''
    data = fichie.objects.all()
    for f in data : 
        pass
        # print(f.text_f)
    #print(data)
    return render(request, 'scrap/form.html', {
            'error_message': "You didn't select a choice.",
        })
   
       # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''
@api_view(['GET', 'POST'])
def head_list(request):
    if request.method == 'GET':
        data = fichie.objects.all()
        print(request.query_params)
        
        key = request.query_params["key"]
        print(key)
        print("fuq")
        lst = lst_url(key)
        print("----------------------------")
        print((lst))
        print("----------------------------") 
        print(len(lst))
        print("-----------url entrer-----------------")
        url = lst[7]
        print(url)
        print("----------------------------")
        words = getfull(url)
        hdrs = words.header_list
        nodes = []
        nodes_q=[]
        father = 0
        links_q = []
        links_9 = []
        nodes_9=[]
        id_ran = 50
        for i in range(len(hdrs)) :
          if hdrs[i].type in ["h1","h2","h3","h4","h5","h6","h7","h8","h9"]:
            id_ran = id_ran+i
            node = {}
            node['id'] = i
            node['label'] = hdrs[i].type + " :"+ hdrs[i].text
            if father == 0 :
              node['level'] = 1
              node["type"] = "1"
              father = 1
            else : 
              node["type"] = "6"
            nodes.append(node)
            print("----------------------------") 
          
            qyan_9 = qayan_9yam(hdrs[i].para)
            
            
            for p in range(len(qyan_9)):
              
              if len(hdrs[i].para) < 4000 and len(qyan_9) > 0 :#len(qyan_9)
                
                qyan = qyan_9[p][0]
                node = {}
                node['id'] = i+id_ran+p
                node['label'] =  qyan
                node["type"] = "3"
                nodes_q.append(node)
                link = {}
                link['source'] = i
                link['target'] = i+id_ran+p 
                link["distance"]= 10
                link['color'] = 'green'
                
                counter = 1
                print("----------------------------") 
                print(len(qyan_9[p]))
                while counter < len(qyan_9[p]) :#len(qyan_9[p])
                  link9 = {}
                  node_9 = {}
                  print("-----------((((((((((-----------------") 
                  if qyan_9[p][counter][0] != 'q':
                    id = i+id_ran+p+counter+randrange(99999)
                    node_9['id'] = id
                    node_9['label'] = qyan_9[p][counter]
                    node_9["type"] = "2"
                    nodes_9.append(node_9)
                    print(id)
                    link9['source'] = i+id_ran+p
                    link9['target'] =  id
                    link9["distance"]= 15
                    link9['color'] = 'green'
                    links_9.append(link9)

                  counter = counter +1
                  links_q.append(link)

              
        
        
        data = {}
        
        print(links_9)
        nodes.reverse()
        
        
        links =[]
        for i in range(len(nodes)):
            
            link = {}
            j = i+1
            while j < len(nodes) :
              if nodes[i]['label'][1] in head_number and nodes[j]['label'][1] in head_number :
                
                if int(nodes[i]['label'][1]) > int(nodes[j]['label'][1]):
                  link['source'] = nodes[j]['id']
                  link['target'] = nodes[i]['id']  
                  link['color'] = '#469CEC'
                  links.append(link)
                  break
              j = j+1
              if j == len(nodes)-1 :
                link['source'] = nodes[j]['id']
                link['target'] = nodes[i]['id']  
                link['color'] = '#469CEC'
                links.append(link)
      
        
        data['nodes'] = nodes + nodes_q +nodes_9     
       
        data['links'] = links + links_q +links_9
        
        json_object = json.dumps(data, indent = 4) 
        
        with open('reacta/src/data.json', 'w') as fp:
          json.dump(data, fp)
        return Response(data)

        #except Exception as e:
        #    print(str(e))
            
        #    return Response({})
        serializer = fichieSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = fichieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoView(viewsets.ModelViewSet):
    serializer_class = fichieSerializer
    queryset = fichie.objects.all()