from django.shortcuts import render

def index(request):
	return render (request, 'Cinema4D/base.html')
