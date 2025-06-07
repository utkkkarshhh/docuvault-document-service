from django.db import models

from service.models import BaseModel, DocumentCategoryMaster


class Documents(BaseModel):
    unique_name = models.CharField(max_length=255, null=False, blank=False)
    upload_name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    type = models.ForeignKey(DocumentCategoryMaster, null=False, on_delete=models.DO_NOTHING)
    link = models.CharField(max_length=255, null=False, blank=False)
    format = models.CharField(max_length=255, null=False, blank=False)
    user_id = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'documents'
