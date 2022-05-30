from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, mixins
import weasyprint

from .serializers import CommandSerializer
from apps.commands.models import Command


class CommandCreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        command = serializer.validated_data
        html_string = render_to_string('pdf/commands-base.html', {'command': command})
        html = weasyprint.HTML(string=html_string, base_url=request.build_absolute_uri())
        pdf_binary = html.write_pdf(presentational_hints=True)
        pdf = ContentFile(pdf_binary, name='test.pdf')

        serializer.save(pdf_file=pdf)
        return Response(
            {
                "file_url": serializer.data.get("pdf_file")
            }, status=status.HTTP_201_CREATED
        )


@api_view(['POST'])
def pdf_generate_view(request):
    serializer = CommandSerializer(data=request.data)
    if serializer.is_valid():
        command = serializer.validated_data
        html_string = render_to_string('pdf/commands-base.html', {'command': command})
        html = weasyprint.HTML(string=html_string, base_url=request.build_absolute_uri())
        pdf_binary = html.write_pdf(presentational_hints=True)
        pdf = ContentFile(pdf_binary, name='test.pdf')
        serializer.save(pdf_file=pdf)
        
        return Response(
            {
                "file_url": serializer.data.get("pdf_file")
            }, status.HTTP_201_CREATED
        )
    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
