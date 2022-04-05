from django.db import models

class Airpot(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=20)
  
    def __str__(self):
        return f"({self.code},{self.city})"

class Flight(models.Model):
    origin=models.ForeignKey(Airpot,on_delete=models.CASCADE,related_name="depatures")
    destination=models.ForeignKey(Airpot,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return f'({self.origin},{self.destination},{self.duration})'

class Passenger(models.Model):
    sex_choices=[
    ('M',"Male"),
    ("F","Female"),
    ("N","Neutral") ]
    First_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    sex=models.CharField(max_length=1,choices=sex_choices)
    flights=models.ManyToManyField(Flight,blank=True,related_name="abcdefght")


    def __str__(self):
        return f"({self.First_name},{self.age},{self.sex},{self.last_name},{self.flights})"
   
    


