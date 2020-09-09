import json
from typing import Any

from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest

from tagging.tagging import tag_tokens
from tokenization.tokenize import tokenize_text


def make_json_response(data: Any) -> HttpResponse:
    return HttpResponse(json.dumps(data))


def tokenize(request: HttpRequest) -> HttpResponse:
    text = request.GET.get('text')
    if not text:
        return HttpResponseBadRequest('No text')

    return make_json_response(tokenize_text(text))


def tag(request: HttpRequest) -> HttpResponse:
    text = request.GET.get('text')
    if not text:
        return HttpResponseBadRequest('No text')

    return make_json_response(tag_tokens(tokenize_text(text)))