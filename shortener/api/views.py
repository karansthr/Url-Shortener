from rest_framework.generics import CreateAPIView

from shortener import models
from .serializers import UrlCreateSerializer


class UrlCreateAPIView(CreateAPIView):
    queryset = models.URL.objects.all()
    serializer_class = UrlCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_authenticated:
            user = None
        serializer.save(user=user)
