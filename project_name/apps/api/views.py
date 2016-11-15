from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
import json
import logging

logger = logging.getLogger('infologger')

# http://www.django-rest-framework.org/tutorial/3-class-based-views
# http://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme
#
# url -X GET --header 'Accept: application/json' \
#        --header 'Authorization: Token 550c942596d689424b473336d4bdec08d0f0a747' \
#        'http://127.0.0.1:8000/api/list/'
#

class ListView(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  """
  get
  """
  def get(self, request):
    logger.info('Get.')
    try:
      response_data = {'count': 0, 'total': 0, 'index': 0}
      response = Response(response_data, status=status.HTTP_200_OK)
    except Exception as ex:
      logger.info('Error getting list.')
      response = HttpResponse()
      response.stats_code = 200
      response.write( str(ex) )
    return response



class DetailView(APIView):
  """
  get, create, update, delete
  """
  def get(self, request):
    logger.info('Get.')
    try:
      response_data = {'id': 0}
      response = Response(response_data, status=status.HTTP_200_OK)
    except Exception as ex:
      logger.info('Error getting list.')
      response = HttpResponse()
      response.stats_code = 200
      response.write( str(ex) )
    return response

  def post(self, request, pk=None):
    logger.info('Create.')
    response_data = {'id': 0}
    response = Response(response_data, status=status.HTTP_200_OK)
    return response

  def put(self, request):
    logger.info('Update.')
    response_data = {'id': 0}
    response = Response(response_data, status=status.HTTP_200_OK)
    return response

  def delete(self, request, pk=None):
    logger.info('Delete.')
    response_data = {'id': 0}
    response = Response(response_data, status=status.HTTP_200_OK)
    return response

