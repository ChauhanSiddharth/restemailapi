from django.shortcuts import render
from .serializers import EmailSerializers
from rest_framework import viewsets
from .models import EmailModel

# Create your views here.

class EmailViewSet(viewsets.ModelViewSet):
    queryset = EmailModel.objects.all().order_by('receiver_name')
    serializer_class = EmailSerializers

def viewInbox(request):
	return render(request,'index.html')
