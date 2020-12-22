from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.http import HttpResponseRedirect
from rest_framework import views
from .models import Article
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site


@api_view(["GET", ])
def get_respone(request):
    return Response(data="domain2", status=HTTP_200_OK)


@api_view(["GET"])
def get_object(request, pk):
    current_site = get_current_site(request)
    print(current_site, 9999999999999)
    if current_site.domain == 'domain2:8000':
        print("taiiiiiiiiiiiiiiiiisssssssssssssssssssssssssssssssssssiiiiii")

        a = Article.objects.filter(pk=pk).first()
        return Response(data=a.headline, status=HTTP_200_OK)
    else:
        return Response(data="pl", status=HTTP_200_OK)

    pass
