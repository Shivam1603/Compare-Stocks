from django.http import JsonResponse
from .models import Security
from .serializers import SecuritySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests # for http requests
from bs4 import BeautifulSoup # for html parsing and scraping
import bs4
from .utils import updateDatabase

@api_view(['GET', 'POST'])
def security_list(request, format = None):
    if(request.method == 'GET'):
        securities = Security.objects.all()
        serializer = SecuritySerializer(securities, many = True)
        return Response(serializer.data)
    elif(request.method == 'POST'):
        serializer = SecuritySerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def security_details(request, name1, name2, format = None):

    # fetch data from google finance API
    response1 = BeautifulSoup(requests.get('https://www.google.com/finance/quote/'+name1+':NSE?hl=en').content, "html.parser")
    response2 = BeautifulSoup(requests.get('https://www.google.com/finance/quote/'+name2+':NSE?hl=en').content, "html.parser")

    security1 = updateDatabase(response1, name1)
    security2 = updateDatabase(response2, name2)

    if(request.method == 'GET'):
        data = [security1, security2]
        return Response({"data": data}, status=status.HTTP_200_OK)
    # elif(request.method == 'PUT'):
    #     serializer = SecuritySerializer(security, data = request.data)
    #     if(serializer.is_valid()):
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    # elif(request.method == 'DELETE'):
    #     security.delete()
    #     return Response(status = status.HTTP_204_NO_CONTENT)
