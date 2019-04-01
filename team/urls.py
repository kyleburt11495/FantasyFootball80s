from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('draft/', views.draft, name='draft'),
]