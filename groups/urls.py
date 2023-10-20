from django.urls import path
from groups import views

urlpatterns = [

    path('', views.group_list, name='group_list'),
    path('add/', views.group_add, name='group_add'),
    path('<int:group_id>/edit/', views.group_edit, name='group_edit'),
    path('<int:group_id>/delete/', views.group_delete, name='group_delete'),

]