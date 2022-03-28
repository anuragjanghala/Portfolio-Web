from django.urls import path
from .views import ProjectList, ProjectDetail, TagList, TagDetail, MessageList, MessageDetail

app_name = 'folio_api'

urlpatterns =[
    path('projects/', ProjectList.as_view(), name='projectlistcreate'),
    path('projects/<str:pk>/', ProjectDetail.as_view(), name='projectdetailcreate'),
    path('tags/', TagList.as_view(), name='taglistcreate'),
    path('tags/<str:pk>/', TagDetail.as_view(), name='tagdetailcreate'),
    path('messages/', MessageList.as_view(), name='messagelistcreate'),
    path('messages/<str:pk>/', MessageDetail.as_view(), name='messagedetailcreate'),
]