import traceback

from django.core.exceptions import FieldError
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import exception_handler

from config import load_config

cfg = load_config()

def custom_exception_handler(exc):
    # Call REST framework's default exception handler first,
    # to get the standard error response if in debug mode

    if cfg.get("ENVIRONMENT") == "LOCAL":
        return exception_handler(exc)

    if isinstance(exc, ValueError):
        error = 'invalid request'
        status = 400
    elif isinstance(exc, Http404):
        error = exc.args[0]
        status = 404
    elif isinstance(exc, FieldError):
        error = 'invalid search/filter query'
        status = 400
    elif len(exc.args) > 1:
            status, error = exc.args
    else:
        error = exc.args
        status = 500

    response = dict(status=status, error=error, stacktrace=traceback.format_exc())
    return Response(response, status=response["status"])
