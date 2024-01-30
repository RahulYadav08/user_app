from .serializers import WatchListSerializer, StreamPlatformSerializer
from watchlist_app.models import WatchList, StreamPlatform
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class StreamPlatformAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Does not exist'},status=status.HTTP_400_BAD_REQUEST) 
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Does not exist'},status=status.HTTP_400_BAD_REQUEST) 
        serializer = StreamPlatformSerializer(platform, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk = pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        



class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchListSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk = pk)
        except WatchList.DoesNotExist:
            return Response({'Error': "Doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk = pk)
        serializer = WatchListSerializer(movie, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk = pk)
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
    
