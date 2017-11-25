from django.http import HttpResponse
from django.shortcuts import render
import random
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
#function-based view
def home(request): #this is function-based view!
	num = None
	some_list = [random.randint(0, 10000000),
				 random.randint(0, 10000000),
				 random.randint(0, 10000000)
	]
	condition_bool_item = True
	if condition_bool_item:
		num = random.randint(0, 10000000)
	context = {
		"num": num,
		"some_list": some_list
	}
	return render(request, "home.html", context) # it takes a request, it takes template and takes content and returns better result

def about(request): #this is function-based view!
	context = {
	}
	return render(request, "about.html", context) # it takes a request, it takes template and takes content and returns better result

def contact(request): #this is function-based view!
	context = {
	}
	return render(request, "contact.html", context) # it takes a request, it takes template and takes content and returns better result


class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs) #saves HomeView object into context variable, printed in shell
		num = None
		some_list = [random.randint(0, 10000000),
					 random.randint(0, 10000000),
					 random.randint(0, 10000000)
		]
		condition_bool_item = True
		if condition_bool_item:
			num = random.randint(0, 10000000)
		context = {
			"num": num,
			"some_list": some_list
		}
		return context