from django.shortcuts import render, redirect
from seuapp.forms import UsersForm
from seuapp.models import Usuario
# Create your views here.

def main_template(request):
	tabela = Usuario.objects.all()
	return render(request, 'main_template.html', {'usuario': tabela})

def games (request):
    return render(request, 'games.html', {})

def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request, 'cadastro.html', data)

def docad(request):
	usuario = Usuario.objects.all()
	form = UsersForm(request.POST or None)
	erro = ''
	for c in usuario:
		if form['usuario'].data == c.usuario:
			erro = "Mensagem de erro"
	if form.is_valid() and erro == '':
		form.save()
	return redirect('cadastro')