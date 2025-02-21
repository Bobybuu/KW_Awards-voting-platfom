"""
Defines the Nominees table and its relationship
"""
from django.db import models
import uuid
from .awards import Awards
from .sub_category import SubCategory
from .category import Category

class Nominees(models.Model):
    """
    Defines the companies to which you will vote for.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
            editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    stage_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, unique=True, blank=True,
            null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bio = models.TextField()
    image = models.URLField(default="NA")
    share_link = models.URLField(default="NA")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    to_field="id")
    sub_category  = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
            to_field="id")

    class Meta:
        """
        Indexes by name
        """
        indexes = [
            models.Index(fields=["id"])
        ]
