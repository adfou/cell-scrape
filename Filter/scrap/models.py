
from django.db import models
class Article(models.Model):
    Article_url = models.CharField(max_length=300)
    def get_url():
        return Article_url
    

class Head(models.Model):
    t_ype = models.CharField(max_length=30)
    father = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    paragraph = models.TextField(default="paragrpahe") 
    
    

class Madjmo3at(models.Model):
    text_m = models.CharField(max_length=300)
    def __str__(self):
        return self.text_m
class fichie(models.Model):
    text_f = models.CharField(max_length=300)
    father = models.ForeignKey(Madjmo3at, on_delete=models.CASCADE)    
    def __str__(self):
        return self.text_f
class word(models.Model):
    text_w = models.CharField(max_length=300)
    father = models.ForeignKey(fichie, on_delete=models.CASCADE) 
    def __str__(self):
        return self.text_w