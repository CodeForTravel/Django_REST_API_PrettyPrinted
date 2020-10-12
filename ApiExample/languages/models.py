from django.db import models



class Paradigm(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    paradigm = models.ForeignKey(Paradigm,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=50,null=True)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.name