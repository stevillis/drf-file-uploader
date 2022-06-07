from django.db import models


class DocumentVersion(models.Model):
    name = models.CharField(max_length=255)
    doc_file = models.FileField(upload_to='media/')
