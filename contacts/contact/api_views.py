
from rest_framework import generics
from contact import models


class ContactListCreateAPIView(generics.ListCreateAPIView):
  queryset = models.Contact.objects.all()
  serializer_class = models.ContactSerializer

class ContactRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Contact.objects.all()
  serializer_class = models.ContactSerializer
  