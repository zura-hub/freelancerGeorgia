

from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancy, name='vacancy'),
    path('create', views.create, name='create'),
    path('<int:pk', views.jobsDetailView.as_view(), name='jobs-detail')

]
