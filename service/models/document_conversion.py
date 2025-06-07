from django.db import models
from service.models import BaseModel, Documents

class DocumentConversion(BaseModel):

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        QUEUED = 'queued', 'Queued'
        COMPLETED = 'completed', 'Completed'

    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    user_id = models.IntegerField(null=False, blank=False)
    conversion_meta_data = models.JSONField(null=False, blank=False)
    converted_url = models.CharField(max_length=1024, null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    class Meta:
        db_table = 'document_conversion'
