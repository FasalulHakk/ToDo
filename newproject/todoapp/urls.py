from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

    path('abchome/',views.tasklv.as_view(),name='abchome'),
    path('abcdetail/<int:pk>/',views.taskdv.as_view(),name='abcdetail'),
    path('abcupdate/<int:pk>/',views.taskuv.as_view(),name='abcupdate'),
    path('abcdelete/<int:pk>/',views.taskdeletv.as_view(),name='abcdelete'),
]
