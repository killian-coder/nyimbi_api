from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer

# Create your views here.

class ListSongView(generics.ListAPIView):
    """
    Provide a get handler
    """

    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
