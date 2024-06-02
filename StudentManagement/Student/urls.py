from django.urls import path
from . import views

urlpatterns = [
    path('/',views.home),
    path('home/', views.home),
    path('addStudent/', views.add_student),
    path('deleteStud/<int:roll>', views.delete_student),
    #path('updateStud/', views.update_student),
]
