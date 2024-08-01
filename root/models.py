from django.db import models
from django.contrib.auth.models import User
class Services(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.TimeField(auto_now_add=True)
    
    


    def __str__(self):
        return self.name
        

    class Meta:
        ordering = ["created_at"]



class SpecialServices(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ["created_at"]






class Questions(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    



    def __str__(self):
        return self.question
        

    class Meta():
        ordering = ["-created_at"]   






class Propertyes(models.Model):
    name = models.CharField(max_length=120)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ["created_at"]




class Pricing(models.Model):
    name = models.CharField(max_length=100)
    contect = models.TextField()
    price = models.FloatField(default=10)
    propertyes = models.ManyToManyField(Propertyes)
    status = models.BooleanField(default=False)
    created_at = models.TimeField(auto_now_add=True)



    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["created_at"]



class Skills(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]



class Makers(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to="root",default="default.png")
    skills = models.ForeignKey(Skills,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)



    class Meta:
        ordering = ["created_at"]


    def __str__(self):
        return self.name.username


