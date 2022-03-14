from django.urls import path
from django.urls import path
from folio import views


urlpatterns = [
    path('',views.index , name='landing-page'),
    path('project/<str:pk>/', views.projectPage, name='project')
]
