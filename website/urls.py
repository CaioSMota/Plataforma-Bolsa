from website.views import About, DataVisualization, Contact
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from.import views

app_name = 'website'

#lista de roteamentos de URLs para funções/Views
urlpatterns = [
	path('', views.home, name="home"),
	path('about', About.as_view(), name="about"),
	path('datavisualization', DataVisualization.as_view(), name="datavisualization"),
	path('contact', Contact.as_view(), name="contact"),

	path('accounts/', include('django.contrib.auth.urls')),
	path('models/', views.models_list, name='models_list'),
	path('models/upload/', views.upload_Models, name="upload_models"),
	path('myAdmin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
