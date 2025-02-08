"""
Defines the Awards table and its relationship
"""
from django.db import models
import uuid


class Awards(models.Model):
    """
    The awards to be handeled to nominees
    """
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    name = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sub_category = models.TextField(default="Should FK to sub" +
                                    " categories table")
    
    class Meta:
        """
        Indexes by name
        """
        indexes = [
            models.Index(fields=["name"])
        ]
