from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('session/<int:id>', views.session, name='session'),
]
