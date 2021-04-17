import wget
import os

from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils import (
    get_image_border_color,
    get_dominant_color,
)    


# Create your views here.
@api_view(['GET'])
def color_picker_view(request):
    img_url = request.GET.get('src', '')
    print(img_url)
    if img_url !=    '':
        image_filename = wget.download(img_url)
        dictionary = {
            'logo_border': str(get_image_border_color(image_filename)),
            'dominant_color': str(get_dominant_color(image_filename))
        }
        os.remove(image_filename)
        return Response(dictionary)
    return Response(status=status.HTTP_404_NOT_FOUND)
