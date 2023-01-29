# coding=utf8
ponc =[',','.',':',';','،','"',"!","؟",".","؛","،","﻿","،","(",")","ٍٍٍ"]
et = ['و']
avant = ["ك","ب","و"]
hraqat = ["´","˝","`"," ̏","˘"," ̑","ˇ","¸","ˆ","¨","·"," ","̡"," ̉","̢","̛ ","¯","˛","῾","َ","ُ","ِ","ْ","ٌ","ّ","~ ","ـٰ","ٍ"]
number = ["1",'2',"3",'4','5','6','7','8',"9"]
def final(not_necassery, parag_without_keyword):
    not_list = not_necassery.split()
    final = []
    for w in parag_without_keyword :
        if w not in not_list :
            final.append(w)
    return final

def mot_find(q_list, paragraph):
    full_list = []
    #sort the list by lenth 
    q_list.sort(key=len)
    for key in q_list : 
      _list= [key]
      for url in range(1):
        words = paragraph.split()
        list_key = key.split()
        counter = 0
        debut = 0
        end = len(list_key)
        emplacment = []
        while debut < len(words) - len(list_key):
          
          if words[debut] == list_key[0]:
            emplacment.append(debut)
            for i in range(end) : 
              if words[debut] == list_key[i]:
                debut = debut+1
                if(debut > len(words)):
                    counter = counter - 1
                    break
              else:
                counter = counter - 1
                break
            counter = counter + 1
          debut=debut+1
    #print(counter)
         
        _list.append(counter)
    #print(_list)
      full_list.append(_list)
    #print(full_list)
    return full_list
def remove(q_list, paragraph,replace = "q"):
    full_list = []
    key_number = 0
    words = paragraph.split()
    #sort the list by lenth of string
    q_list.sort(key=len)
    q_list.reverse()
    #--------------
    
    for key in q_list :
      _list= [key]
      
      remplace = 0
      list_key = key.split()
      counter = 0
      debut = 0
      end = len(list_key)
      
      while debut < len(words) - len(list_key):
        remplace = debut
        if words[debut] == list_key[0]:
          
          remplace = debut
          for i in range(end) : 
            if words[debut] == list_key[i]:
              debut = debut+1
              if(debut > len(words)):
                  counter = counter - 1
                  remplace = -1
                  break
            else:
              counter = counter - 1
              remplace = -1
              break
          counter = counter + 1
          if remplace != -1 :
            
            words.insert(remplace, "q"+str(key_number))
            for n in range(end):
                words.pop(remplace+1)
              
          #print(remplace)
        debut=debut+1
        remplace = debut
      _list.append(counter)
      _list.append("q"+str(key_number))
      full_list.append(_list)
      key_number = key_number+1

    return full_list,words
def mot_for_remove(p):
    mots_present = []
    for mot in p : 
        if mot[1] > 0 :
          
           mots_present.append(mot)
    return mots_present

def final_func(not_necassery, q_list, param):
    final_q = []
    full,parag = remove(q_list,param)
    
    #print(parag)
    fuq = final(not_necassery, parag)

    full = mot_for_remove(full)
    debut = 0
    #print(fuq)
    for i in range(len(fuq)) : 
      _list=[]
      if fuq[i][0] == "q" :
        _list.append(fuq[i])
        end = i+1
        while debut < i : 
            _list.append(fuq[debut+1])
            debut = debut+1
        while end < len (fuq) :
            if fuq[end][0] == "q" : 
                _list.append(fuq[end])
                break 
            _list.append(fuq [end])
            end = end + 1
        #print(_list)
        final_q.append(_list)
       
    return final_q , full
def list_only_q(word_list):
    q = []
    for p in word_list :
      q.append(p[2])
    return q
#first q is the title
def final_func_last_2( q_list, param,clean_q,full_qyan_accurnce):
    final_q = []

    
    fuq = clean_q
    
    full = mot_for_remove(full_qyan_accurnce)
    
    debut = 0
    temp = []
    for n in fuq :
      if n != "" :
        temp.append(n)
    fuq = temp 

    for i in range(len(fuq)) : 
      _list=[]
      
      #print(fuq[0])
      if fuq[i][0] == "q" :
        
        _list.append(fuq[i])
        end = i+1
        while debut <= i : 
            _list.append(fuq[debut])
            debut = debut+1
        while end < len (fuq) :
            
            
            if fuq[end][0] == "q" : 
                _list.append(fuq[end])
                break 
            _list.append(fuq [end])
            end = end + 1
        #print(_list)
        final_q.append(_list)
    #print(final_q)
    return final_q , full

def final_func_last( q_list, param,clean_q):
    final_q = []
    full,parag = remove(q_list,param)
    
    #print(parag)
    fuq = clean_q
    
    #print(fuq)
    
    full = mot_for_remove(full)
    debut = 0
    for i in range(len(fuq)) : 
      _list=[]
      if fuq[i][0] == "q" :
        _list.append(fuq[i])
        end = i+1
        while debut < i : 
            _list.append(fuq[debut+1])
            debut = debut+1
        while end < len (fuq) :
            if fuq[end][0] == "q" : 
                _list.append(fuq[end])
                break 
            _list.append(fuq [end])
            end = end + 1
        #print(_list)
        final_q.append(_list)
       
    return final_q , full

def list_only_q(word_list):
    q = []
    for p in word_list :
      q.append(p[2])
    return q

def list_final_func(divsion, word_list):
    list_final =[]
    for n in divsion :
        for p in word_list :
      #print(p)
          if n[0] == p[2]:
             n[0] = p[0]
             list_final.append(n)
    return list_final


def read_qyan():
    q_list_next_line = []
    with open('qword.txt', 'r',encoding='utf-8') as f:
        for line in f:
          q_list_next_line.append(line)
    q_list = []
    for  q in range(len(q_list_next_line)):
       qnext = q_list_next_line[q].split("\n")[0]
       if qnext != "":
        q_list.append(qnext)
    
    return q_list
def read_not():
    q_list_next_line = []
    with open('not.txt', 'r',encoding='utf-8') as f:
        for line in f:
          q_list_next_line.append(line)
    q_list = []
    for  q in range(len(q_list_next_line)):
       q_list.append(q_list_next_line[q].split("\n")[0])
    j=[]
    for l in ponc:
      for n in q_list:
        
        j.append(n + l)
        j.append( l + n )
        #print(j)
    for k in j : 
      q_list.append(k)
    return q_list
  
def func_get_by_phrase(parag):
    full_f = []
    i = 0
    while i < len(parag):
  
      if parag[i][0] == "q":
        full_f.append(parag[i] )
      if parag[i] != "*" and parag[i][0] != "q" :
        phrase = True
        add = False
        ph = parag[i]
        if i+1 < len(parag) : 
          while (phrase == True and i+1 < len(parag)):
            if parag[i+1] != "*" and parag[i+1][0] != "q":
              ph = ph + ' '+ parag[i+1]
              i = i + 1 
              add = True
            else : 
              phrase = False
      
        full_f.append(ph)
      i = i+1
    return full_f

def read_artcl(parag):
        param =  parag.replace('\n', ' ')
        paragraph =  parag.replace('\n', ' ')
        for c in range(len(param)) :
          #supprmer les source[2]
          if c < len(param) and c > 0 :
            if param[c] in number and param[c-1] == "\n":
              param = param[:c]+param[c+1:]
        param = param.replace('\n', ' ')
        for c in hraqat :
           param = param.replace(c, '')
        for c in ponc :
           param = param.replace(c, ' ')
        for c in range(len(param)) :
          #supprmer les source[2]
          if c+2 < len(param):
            if param[c] == "[":
              param = param[:c]+param[c+3:]
        
        return param

def remplace_not(not_list, parag):
    for i in range(len(parag)) :
      if parag[i] in not_list : 
        parag[i] = "*"
def func_ponc(ponc, full_f):
    last_full =[]
    for j in range(len(full_f)) :
      c=0
      p = full_f[j]
      while c < len(full_f[j]):
        if p[c] in ponc :
          p = p[:c] + '**' + p[c+1:]
        c=c+1
      last_full.append(p)
    return last_full
def func_et(et, last_full):
    final = []
    for p in last_full :
      c=0
      while c < len(p)-2:
        if p[c] in et :
          if p[c+1] == 'ا' and p[c+2] == 'ل' :
            q = ' '
            p = p[:c] + '**' + p[c+1:]
        
            c=c+1
        
    
        c=c+1
      for w in p.split("**"):
        final.append(w)
    return final


#-------------------------------------------------------debut---------------------------
def qayan_9yam(sectionH):
  q_list = read_qyan()
  #print(q_list)
  para = sectionH
  param = read_artcl(para)#paragraphe aanalser
  
  not_necassery = read_not()
  not_list = not_necassery
  full_qyan_accurnce,parag = remove(q_list,param)
#----------------------------------------------reglage de \ufeff ------------------------------------

#-------------------------remplace not nessecary wth *-------------------------------------

  remplace_not(not_list, parag)
#-----------------------get all the phrase --------------------------------------

  full_f = func_get_by_phrase(parag)

#-----------------------enlver la ponctn --------------------------------------

  last_full = func_ponc(ponc, full_f)

#enlever le et
  final = func_et(et, last_full) 
  ls = final
  #remove not necessary second tlme
  final = []
  for n in ls :
    if n not in not_list:
      final.append(n)

  list_final,word_list = final_func_last_2( q_list, param,final,full_qyan_accurnce)

  test = []
  final =[]

  for n in list_final :
    for p in word_list :
      #print(p)
      if n[0] == p[2]:
     
        n[0] = p[0]
        #print(n)
    final.append(n)

  spaceq ='------------كيان-----------------'
  space ='----------------------------'

  fltr_fnl = []
  for n in final:
    fltr_q = []
    y = 1
    fltr_q.append(n[0])
    while y < len(n) :
      if n[y] not in fltr_q:
        fltr_q.append(n[y])
      y = y+1
    fltr_fnl.append(fltr_q)
  finalg =[]
  final_last = []

  return fltr_fnl


sct = '''قياس مستوى السكر في الدم هو الوسيلة الأساسية التي يمكن من خلالها معرفة ما إذا كانت مستويات الجلوكوز ضمن النطاق الطبيعي أم أنها زادت إلى المعدل الذي يشير لاحتمالية الإصابة بالسكري، لذا من المهم معرفة معدل السكر الطبيعي في الدم، والنسب غير الطبيعية، وما إذا كانت تشير إلى حالة صحية قد تتطلب المتابعة مع الطبيب، وفي هذا المقال سنتعرف إلى الاختبارات الشائعة لقياس الجلوكوز في الدم، والنسب الطبيعية وغير الطبيعية في كلٍ منها.
ما معدل السكر الطبيعي؟

مستوى السكر في الدم يُقصد به كمية الجلوكوز الموجودة في الدم في أي وقت، وقد يشير ارتفاع أو انخفاض مستوى السكر في الدم إلى حالة تحتاج لعناية طبية، وتختلف نسبة السكر الطبيعية من
 شخصٍ لآخر، ويتوقف الأمر على عدة عوامل، والتي منها:

معدل النشاط البدني.
النظام الغذائي.
العادات اليومية.
الإصابة بأمراض مزمنة.
بعض أنواع الأدوية.
مستوى الهرمونات في الجسم.
مؤشر كتلة الجسم.
الحمل.

وقد ترتفع أو تنخفض نسبة السكر في الدم ولكنها تظل طبيعية، لذا فإن النسب المرجعية (الطبيعية) تكون في صورة نطاق مع حد أدنى وحد أقصى، ومعدل السكر الطبيعي هو الذي يقع ضمن هذا النطاق.
من المهم أن تظل مستويات السكر في الدم في نطاق صحي. إذا انخفضت مستويات الجلوكوز بشكل كبير، فإنها تؤثر في القدرة على التفكير والعمل بشكل طبيعي، وقد تصل مضاعفاتها إلى فقدان الوعي والوفاة، كذلك إذا كان الجلوكوز مرتفعًا ولم يتم التحكم في مستواه فقد يتسبب مع الوقت في تلف الأعضاء.
يُوجد أكثر من فحص لقياس مستوى السكر في الدم، إذ يمكن قياس مستوى الجلوكوز في الدم في أثناء الصيام، أو بعد الأكل، أو في أي وقت في اليوم، وتختلف المعدلات الطبيعية للجلوكوز في كل
ٍ منها، وسنتحدث عنها بالتفصيل فيما يلي.
ما معدل السكر الطبيعي للصائم؟
يقيس فحص السكر الصائم مستوى الجلوكوز في الدم بعد صيام ليلة كاملة (8 - 12 ساعة تقريبًا)، وهو الفحص الأكثر شيوعًا لتشخيص مرض السكري، لأنه أكثر دقة، إذ يكون الجسم في حالة حرمان
من الطعام، وبالتالي تكون نسبة الجلوكوز منخفضة إلى حدٍ ما، لذا إذا أشارت النتائج إلى ارتفاع ملحوظ في مستوى الجلوكوز في أثناء الصيام فقد يشير الأمر بنسبة كبيرة للإصابة بالسكري.

كيف يمكن التحضير للاختبار؟
يجب الامتناع عن تناول أي أطعمة أو مشروبات ما عدا الماء قبل الفحص بثمانِ ساعات على الأقل.
كيف يتم الاختبار؟
يسحب اختصاصي التحاليل عينة دم من الوريد، ويرسلها للفحص.
ماذا تعني نتائج اختبار نسبة السكر في الدم للصائم؟

تتراوح نسبة جلوكوز الدم الطبيعي في أثناء الصيام للبالغين الذين لا يعانون من مرض السكري بين 70 و 100 ملليجرام لكل ديسيلتر.
أما إذا كانت النسبة تتراوح من 100 إلى 125 مجم / ديسليتر فهذا يعني أن الشخص قد يكون في مرحلة مقدمات السكري (مقدمات السكري تعني أن مستوى الجلوكوز في الدم لدى الشخص أعلى من المعتاد، لكنه لا يعتبر بعد مريضًا بالسكري).
إذا كان مستوى السكر في الدم 126 مجم / ديسيلتر أو أعلى في اختبارين منفصلين فهذا يشير إلى أن الشخص مريض بالسكري.

ما معدل السكر الطبيعي بعد الأكل؟

قد يطلب الطبيب مع فحص مستوى السكر في أثناء الصيام فحص آخر وهو فحص السكر بعد الأكل بساعتين، ويتم إجراء هذا الاختبار لمعرفة كيف يستجيب الجسم للسكريات والكربوهيدرات بعد تناول الطعام.
في أثناء هضم الطعام ترتفع مستويات الجلوكوز في الدم بشكلٍ كبير، واستجابة لذلك يفرز البنكرياس الأنسولين لنقل الجلوكوز إلى خلايا العضلات والأنسجة الأخرى لاستخدامها كوقود، وفي غض
ون ساعتين من تناول الطعام، يجب أن تعود مستويات الأنسولين والجلوكوز في الدم إلى طبيعتها. إذا ظلت مستويات الجلوكوز في الدم مرتفعة، فقد يشير الأمر للإصابة بالسكري.
كيف يمكن التحضير للاختبار؟
يجب الصيام لمدة 12 ساعة قبل الاختبار ثم تناول وجبة تحتوي على 75 جرامًا على الأقل من الكربوهيدرات. بعد الوجبة، لا يجب تناول أي شيء آخر قبل إجراء الاختبار لمدة ساعتين، كذلك يجب
 عدم ممارسة مجهود بدني شديد خلال هذه الفترة لأنها قد تؤثر في نتائج الاختبار، ويجب إخبار الطبيب بجميع الأدوية والمكملات الغذائية التي يتناولها المريض والتي قد تؤثر في نتيجة الفحص.
ماذا تعني نتائج الاختبار؟

قد تختلف نتائج الاختبار حسب العمر، والجنس، والتاريخ المرضي، وغيرها من العوامل، ومع ذلك فإن النتيجة الطبيعية لاختبار مستوى السكر في الدم بعد الأكل بساعتين لأولئك الذين لا يعانون من مرض السكري تكون أقل من 140 مجم / ديسيلتر.
أما إذا كانت النسبة تتراوح من 140 إلى 199 مجم/ ديسيلتر فهذا يعني أن الشخص في مرحلة ما قبل السكري.
وإذا كان مستوى السكر في الدم بعد تناول الطعام بساعتين هو 200 مجم/ ديسيلتر أو أكثر فهذا يعني أن الشخص مريضًا بالسكري.

كيف يتم إجراء الاختبار؟
يُجرى الاختبار على عينة دم تُسحب من وريد في الذراع أو اليد.
تعرف علي : أفضل أطباء الغدد الصماء والسكر
ما المعدل الطبيعي للسكر العشوائي؟
اختبار الجلوكوز العشوائي هو إحدى طرق قياس كمية الجلوكوز في الدم في أي وقت من اليوم، وسُمي عشوائي أو عرضي لأنه يتم إجراؤه في أي وقت من اليوم سواء كان المريض صائمًا أم لا فلن ي
ؤثر ذلك في الاختبار، ويُستخدم هذا الفحص كوسيلة سريعة لمعرفة ما إذا كان الشخص مصابًا بالسكري، وهو اختبار مهم خاصةً لمرضى السكري من النوع الأول الذين يحتاجون إلى حقن الأنسولين
كعلاج طارئ.
إذا كانت نتيجة فحص السكر العشوائي تشير إلى أن الشخص لديه مستويات جلوكوز أعلى من الطبيعي، سيطلب الطبيب إعادة الاختبار في يوم آخر لتأكيد التشخيص، أو إجراء الاختبارات الأخرى بما في ذلك اختبار مستوى الجلوكوز في الدم في أثناء الصيام وبعد الأكل بساعتين.
كيف يتم إجراء الاختبار؟
يتطلب الاختبار عينة صغيرة من الدم يأخذها الطبيب أو الممرضة باستخدام إبرة، غالبًا من الإصبع.
ماذا تعني نتائج الاختبار؟
في اختبار السكر العشوائي تشير نتيجة 200 ملجم/ ديسيلتر أو أعلى إلى أن الشخص قد يكون مصابًا بالسكري، ومع ذلك، من أجل تشخيص مؤكد، عادةً ما يكرر الطبيب الاختبار في يوم آخر، وتشير
 واحدة من الدراسات التي أُجريت عن عوامل الخطر للإصابة بالسكري، إلى أن اختبار الجلوكوز العشوائي الذي يظهر قراءة أكثر من 100 ملجم/ ديسيلتر يُعد عامل خطر أكبر للإصابة بمرض السكر
ي مقارنةً بالعوامل التقليدية، مثل السمنة.
اعرف أكثر عن أنواع مرض السكر وطرق العلاج مع د. إيمان نصر


وفي مجمل القول، فإن معدل السكر الطبيعي يختلف باختلاف نوع الفحص المستخدم لقياس مستوى الجلوكوز في الدم كما وضحنا في المقال، ولن يبدأ عديد من الأشخاص في الشعور بأعراض ارتفاع السكر حتى يصل مستواه إلى 250 مجم/ ديسيلتر أو أعلى، وتساعد بعض التغييرات في النظام الغذائي، وفقدان الوزن الأشخاص في مرحلة ما قبل السكري على تقليل فرص الإصابة به.
تعرف على كل ما يخص مرض السكري وعلاجه على موقع مستشفيات أندلسية
قياس مستوى السكر في الدم هو الوسيلة الأساسية التي يمكن من خلالها معرفة ما إذا كانت مستويات الجلوكوز ضمن النطاق الطبيعي أم أنها زادت إلى المعدل الذي يشير لاحتمالية الإصابة بالسكري، لذا من المهم معرفة معدل السكر الطبيعي في الدم، والنسب غير الطبيعية، وما إذا كانت تشير إلى حالة صحية قد تتطلب المتابعة مع الطبيب، وفي هذا المقال سنتعرف إلى الاختبارات الشائعة لقياس الجلوكوز في الدم، والنسب الطبيعية وغير الطبيعية في كلٍ منها.
h1





مستوى السكر في الدم يُقصد به كمية الجلوكوز الموجودة في الدم في أي وقت، وقد يشير ارتفاع أو انخفاض مستوى السكر في الدم إلى حالة تحتاج لعناية طبية، وتختلف نسبة السكر الطبيعية من
 شخصٍ لآخر، ويتوقف الأمر على عدة عوامل، والتي منها:
'''
#fltr_fnl=qayan_9yam(sct)
#spaceq ='------------كيان-----------------'
#space ='----------------------------'
'''with open('output1.txt', 'w',encoding='utf-8') as f:
    for elm in fltr_fnl:
      
      #f.write(space+"\n")
      counter = 0
      f.write(spaceq+"\n")
      for line in elm:
          if counter <= 1:
            f.write(space+"\n")
          
          if line[0] != "q" :
            f.write(str(line)+"\n")
          counter =counter+1'''
#print(fltr_fnl)

