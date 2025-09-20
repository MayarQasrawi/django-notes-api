from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by("-created_at")
    serializer_class = NoteSerializer

    # Bonus: Search by query parameter (title OR content)
    @action(detail=False, methods=["get"], url_path="search")
    def search_notes(self, request):
        query = request.query_params.get("query", "")
        if not query:
            return Response({"error": "Query parameter is required"}, status=400)

        notes = self.queryset.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        serializer = self.get_serializer(notes, many=True)
        return Response(serializer.data)
