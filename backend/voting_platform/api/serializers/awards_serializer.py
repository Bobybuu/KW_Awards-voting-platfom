"""
Handels the object-to-json and viseversa converts
"""
from rest_framework import serializers
from ..models.awards import Awards

class AwardsSerializer(serializers.ModelSerializer):
    """
    Handles the serialization process of this table.
    """
    class Meta:
        model = Awards
        fields = ["ID", "name", "sub_category", "created_at"]
        read_only_fields = ["ID", "created_at"]


    def validate_name(self, value):
        """
        Makes sure names are unique.
        """
        if Awards.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError(
                "A nominee with this name exists")
        return value
