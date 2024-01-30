from .serializers import MovieSerializer
from watchlist_app.models import Movie
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class MovieListAV(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk = pk)
        except Movie.DoesNotExist:
            return Response({'Error': "Movie doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, pk):
        movie = Movie.objects.get(pk = pk)
        serializer = MovieSerializer(movie, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk = pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def movie_list(request):

#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many = True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method == "POST":
#         serializer = MovieSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     try:
#         movie = Movie.objects.get(pk = pk)
#     except Movie.DoesNotExist:
#         return Response({'Error': "Movie doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status= status.HTTP_200_OK)
    
#     if request.method == "PUT":
#         serializer = MovieSerializer(movie, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status= status.HTTP_304_NOT_MODIFIED)
        
#     if request.method == "DELETE":
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)