from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
	name = models.CharField(max_length = 120) #this has to be told to python(and the database) that we created new model
											  #use python manage.py makemigrations
											  #use python mange.py migrate
	location = models.CharField(max_length = 120, null = True, blank = True)
	category = models.CharField(max_length = 120, null = True, blank = False)

	#each time im adding something to models, i have to makemigrations+migrate
