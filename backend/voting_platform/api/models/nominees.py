"""
Defines the Nominees table and its relationship
"""
from django.db import models
import uuid
from .awards import Awards


class Nominees(models.Model):
    """
    Defines the companies to which you will vote for.
    """
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    name = models.TextField()
    description = models.TextField()
    image = models.URLField(default="NA")
    votes = models.IntegerField(default=0)
    share_link = models.URLField(default="NA")
    category_ID = models.ForeignKey(Awards, on_delete=models.CASCADE,
                                    to_field="ID")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # I don't think it is necessary to update it

    class Meta:
        """
        Indexes by name
        """
        indexes = [
            models.Index(fields=["name"])
        ]
