"""
Defines the Votes table and its relationship
"""
from django.db import models
from .nominees import Nominees
from .sub_category import SubCategory
import uuid


class Votes(models.Model):
    """
    Defines the voteing functionality.
    """
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
                                     to_field="id")
    nominee = models.ForeignKey(Nominees, on_delete=models.CASCADE,
                                to_field="ID")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Indexes by ID
        """
        indexes = [
            models.Index(fields=["ID"])
        ]
