from django.urls import path
from . import views

urlpatterns = [
    path("people/", views.all_people, name="people"),
    path("sql_inj/", views.simple_form_inj, name='sql_inj')
]