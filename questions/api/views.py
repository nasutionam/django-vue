from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import QuesitonSerializer, AnswerSerializer
from ..models import Question, Answer
from .permissions import IsAuthorOrReadOnly

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    lookup_field = "slug"
    serializer_class = QuesitonSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)