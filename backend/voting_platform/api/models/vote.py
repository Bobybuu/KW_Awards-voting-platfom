from django.db import models
from .category import SubCategory
from .nominee import Nominee
import uuid


class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name='sub_categories')
    nominee = models.ForeignKey(
        Nominee, on_delete=models.CASCADE, related_name='nominees')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sub Category: {self.sub_category.name} | Category: {self.sub_category.category.name}"
