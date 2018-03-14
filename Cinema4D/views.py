from django.shortcuts import render

def index(request):
	return render_to_response (request, 'Cinema4D/Cinema4D.html')
