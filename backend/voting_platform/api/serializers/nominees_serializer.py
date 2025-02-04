from rest_framework import serializers
from rest_framework.response import Response
from ..models.nominees import Nominees
from ..models.category import Category
import uuid


class NomineesSerialiser(serializers.ModelSerializer):
    """
    Handles the serialization process of this table.
    """

    category_ID = serializers.CharField()

    class Meta:
        model = Nominees
        fields = ["ID", "name", "description", "created_at",
                  "updated_at", "image", "votes", "share_link",
                  "category_ID"]
        read_only_fields = ["ID", "created_at", "updated_at"]

    def validate_category_ID(self, value):
        """
        Validate category ID to handle both UUID and category names.
        """
        try:
            # If value is a valid UUID
            category_uuid = uuid.UUID(value)
            category = Category.objects.get(id=category_uuid)
        except (ValueError, Category.DoesNotExist):
            # Treat value as a category name
            category = Category.objects.filter(name=value).first()
            if not category:
                raise serializers.ValidationError("Invalid category name"
                                                  +" or UUID.")

        # Return the UUID for internal use
        return category

    def create(self, input_data):
        """
        Creates the object and adds it to the database.
        """
        # Assign the correct UUID from the validated data
        category_id = input_data.pop("category_ID")
        return Nominees.objects.create(category_ID=category_id, **input_data)

    def validate_name(self, value):
        """
        Makes sure names are unique.
        """
        if Nominees.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError(
                "A nominee with this name exists")
        return value
