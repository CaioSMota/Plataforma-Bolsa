from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import ModelsForm
from .models import Modelos


@login_required
def models_list(request):
	models = Modelos.objects.all()
	return render(request, 'website/models_list.html', {
		'models': models
	})


@login_required
def upload_Models(request):
	if request.method == 'POST':
		form = ModelsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('models_list')
	else:
		form = ModelsForm()

	return render(request, 'website/upload_models.html', {
		'form': form
	})


def home(request):
    return render(request, 'website/index.html')


class About(TemplateView):
	template_name = "website/about.html"


class DataVisualization(TemplateView):
	template_name = "website/datavisualization.html"


class Contact(TemplateView):
	template_name = "website/contact.html"

