from django.db import models
import uuid

class Nominees(models.Model):
    """
    Defines the companies to which you will vote for.
    """
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    name = models.TextField()
    description = models.TextField()
    image = models.URLField(default="NA")
    votes = models.IntegerField(default=0)
    share_link = models.URLField(default="NA")
    category_ID = models.ForeignKey("Category", on_delete=models.CASCADE,
                                    to_field="id") # Check
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # I don't think it is necessary to update it

    class Meta:
        indexes = [
            models.Index(fields=["name"])
        ]
