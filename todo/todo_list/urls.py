from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name="home"),
    path('create/',create, name="create"),
    path('my-task/',my_task, name="my-task"),
    path('edit-task/<int:id>/', edit_task, name="edit-task"),
    path('delete-task/<int:id>/', delete_task, name="delete-task"),
]