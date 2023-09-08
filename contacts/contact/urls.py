from django.urls import path
from contact import views
from contact import api_views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', api_views.ContactListCreateAPIView.as_view(), name='list-create-view'),
    path('api/contacts/<int:id>', api_views.ContactRetrieveUpdateDestroyAPIView.as_view(), name='retrive-update-destroy-contact'),
]
