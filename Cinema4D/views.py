from django.shortcuts import render, render_to_response

def index(request):
	return render (request, 'Cinema4D/Cinema4D.html')
