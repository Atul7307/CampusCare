from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from .permissions import IsStudent, IsCounsellor, IsAdminRole


User = get_user_model()


class MeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        serializer = UserSerializer(request.user)
        
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated, IsStudent])
    def student_area(self, request):
        return Response({"message": "Welcome student"})

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated, IsCounsellor])
    def counsellor_area(self, request):
        return Response({"message": "Welcome counsellor"})

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated, IsAdminRole])
    def admin_area(self, request):
        return Response({"message": "Welcome admin"})
