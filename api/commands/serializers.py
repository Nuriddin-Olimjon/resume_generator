from rest_framework import serializers

from apps.commands.models import Command


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = (
            'id',
            'org_name',
            'date',
            'number',
            'region',
            'type',
            'person_name',
            'paragraph_1',
            'paragraph_2',
            'cause',
            'confirmer_role',
            'confirmer_name',
            'address_uz',
            'address_en',
            'phone_number',

            'pdf_file',
        )
        read_only_fields = ('pdf_file',)


class FileSerializer(serializers.Serializer):
    pdf_file = serializers.FileField()
