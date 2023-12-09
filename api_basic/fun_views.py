from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Articles
from .serializers import ArticlesSerializer

# Create your views here.

# ========== simple serializer viev ==================================
# @csrf_exempt
# def old_article_list(request):
#     """
#     List all code article, or create a new article.
#     """
#     if request.method == 'GET':
#         article = Articles.objects.all()
#         serializer = ArticlesSerializer(article, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticlesSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def article_list(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         article = Articles.objects.get(pk=pk)
#     except Articles.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = ArticlesSerializer(article)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticlesSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)


# =====================================================================================================

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def old_article_list(request):
    """
    List all code article, or create a new article.
    """
    if request.method == 'GET':
        article = Articles.objects.all()
        serializer = ArticlesSerializer(article, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_list(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        article = Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticlesSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticlesSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)