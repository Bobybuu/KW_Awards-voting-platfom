from rest_framework import serializers
from ..models.nominees import Nominees
from ..models.category import Category
from uuid import UUID

class NomineesSerialiser(serializers.ModelSerializer):
    """
    Handels the serialization process of this table
    """
    class Meta:
        """Defins the process of serializing"""
        model = Nominees
        fields = ["ID", "name", "description", "created_at",
                  "updated_at", "image", "votes", "share_link",
                  "category_ID"]
        read_only_fields = ["ID", "created_at", "updated_at"]

    def validate_cat(self, value):
        """
        Checks the category_ID feild and create accordingly 
        """
        # If its a UUID value
        try:
            UUID(str(value))
            category = Category.objects.filter(id=UUID(str(value))).first()
            if category is None:
                raise serializers.ValidationError("No Category with such ID")
            return category
        except ValueError:
            # It must be a name then
            category = Category.objects.filter(name=value).first()
            if category is None:
                raise serializers.ValidationError("No Category with such name")
            return category

    def create(self, checked_data):
        """
        Returns the nominee instanse
        """
        category_instance = checked_data.pop("category_ID")
        return Nominees.objects.create(category_ID=category_instance,
                                       **checked_data)
