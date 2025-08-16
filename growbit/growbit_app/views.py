# growbit/views.py
from rest_framework import generics, viewsets
from .models import User
from .serializers import UserSignupSerializer
from rest_framework.permissions import IsAuthenticated

# user signup
class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer 
# user view
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [IsAuthenticated]