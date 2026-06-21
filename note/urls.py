from django.urls import path
from . import views

urlpatterns=[
    path('', views.notes_list, name="notes_list"),
    path('delete/<int:pk>/', views.notes_delete, name='notes_delete'),
    path('create/', views.notes_create, name='notes_create'),
    path('edit/<int:pk>/', views.notes_edit, name='notes_edit'),
    path('details/<int:pk>/', views.notes_detail, name='notes_detail'),
    path('register/', views.register_notes, name='register_notes'),
    path('login/', views.login_notes, name='login_notes'),
    path('logout/', views.logout_views, name="logout_views")
]


