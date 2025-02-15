"""
Defines the Awards table and its relationship
"""
from django.db import models
import uuid
from .sub_category import SubCategory


class Awards(models.Model):
    """
    The awards to be handeled to nominees
    """
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    name = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sub_category = models.ForeignKey(SubCategory, to_field="id",
                                     on_delete=models.CASCADE)
    
    class Meta:
        """
        Indexes by name
        """
        indexes = [
            models.Index(fields=["name"])
        ]
