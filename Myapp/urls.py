from Myapp import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('form',views.form),
    path('delete/<person_id>', views.delete),
    path('edit/<person_id>', views.edit),
    path('login_form', views.login_view, name='login'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('logout', views.logout_view, name='logout'),
    path('JavaScript_Exercises', views.JavaScript_Exercises, name='JavaScript_Exercises'),

]
