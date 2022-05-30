from django.db import models


class Command(models.Model):
    org_name = models.CharField(max_length=255)
    date = models.DateField()
    number = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    type = models.ForeignKey('CommandType', on_delete=models.CASCADE)
    person_name = models.CharField(max_length=255)
    paragraph_1 = models.TextField()
    paragraph_2 = models.TextField()
    cause = models.TextField()
    confirmer_role = models.CharField(max_length=30)
    confirmer_name = models.CharField(max_length=50)
    address_uz = models.CharField(max_length=255)
    address_en = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)

    pdf_file = models.FileField(upload_to='commands/%y/%m/%d/')
    confirmed = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommandType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class CommandTypeText(models.Model):
    type = models.ForeignKey(CommandType, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return self.type.title + '| buyruq text'
