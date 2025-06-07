from django.db import models

from service.models import BaseModel


class DocumentCategoryMaster(BaseModel):
    name = models.CharField(max_length=55, null=False, blank=False)

    class Meta:
        db_table = 'document_category_master'

