from django.urls import path
from django.urls import path
from folio import views


urlpatterns = [
    path('',views.index , name='landing-page'),
    path('project/<str:pk>/', views.projectPage, name='project'),
    path('add-project/', views.addProject, name='add-project'),
    path('edit-project/<str:pk>/', views.editProject, name='edit-project')
]
