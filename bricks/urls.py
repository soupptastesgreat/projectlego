from django.urls import path
from . import views
from .views import *
from .forms import thebricksForm
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import *
from bricks.models import *

app_name = 'bricks'

urlpatterns = [
	path('', views.index, name='index'),
	path('submit', views.submitbrick, name='submitbrick'),
	path('color', views.brickcolor, name='brickcolor'),
	path('type', views.bricktype, name='bricktype'),
	path('size', views.bricksize, name='bricksize'),
]