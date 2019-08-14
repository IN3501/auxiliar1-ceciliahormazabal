from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def horario(request):
	return render(request, 'miapp/horario.html')	

def equipodocente(request):
	return render(request, 'miapp/equipodocente.html')