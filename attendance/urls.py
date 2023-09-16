from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.participant_list, name='participant_list'),
    path('list/', views.participant_form, name='insert'),
    path('<int:num>/', views.participant_form, name='update'),
    path('delete/<int:num>/', views.participant_delete, name='delete')
]