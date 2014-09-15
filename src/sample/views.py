from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
import json
import logging

logger = logging.getLogger('infologger')

# http://www.django-rest-framework.org/tutorial/3-class-based-views
class ListView(APIView):
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

