from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=14)
    image=models.FileField(upload_to="portifolo_images/",blank=True)
    def __str__(self):
        return f"Name : {self.name},email : {self.email},phone_no : {self.phone}"
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    stars=models.IntegerField(default=5)
    idea=models.BooleanField()
    def __str__(self):
        return f"Name : {self.user.name} ,Comment : self.comment ,Idea : {self.idea}"