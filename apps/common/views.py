from django.db import transaction
from django.shortcuts import render, HttpResponse
from psycopg2._psycopg import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import logging

logger = logging.getLogger(__name__)


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World! You are authenticated'}
        return Response(content)


@api_view()
def AboutView(request):
    return Response({'message': 'About Page'})


def trigger_error(request):
    division_by_zero = 1 / 0


@api_view(['GET'])
def health_check(request):
    return Response({'message': 'Hello, world!'}, status=200)
    #return HttpResponse("Health Check Status: Stable", status=200)


def trigger_error_exception(request):
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        logger.exception(e)


def loggerDefault(request):
    try:
        with transaction.atomic():
            logging.debug("I am ignored | this is a DEBUG")
    except IntegrityError:
        return Response('This example already exists', status=409)

    logging.debug("I am ignored | this is a DEBUG")
    logging.info("I am a breadcrumb | this is a INFO")
    logging.warning("An exception | this is WARNING", extra=dict(bar=43, foo=66))
    logging.error("I am an event | this is ERROR", extra=dict(bar=43))
    logging.exception("An exception happened")

    return HttpResponse("Se disparo logging por default")