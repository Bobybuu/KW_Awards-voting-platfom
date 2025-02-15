"""
Handels the object-to-json and viseversa converts
"""
from rest_framework import serializers
from ..models.vote import Votes, Nominees

class VotesSerializer(serializers.ModelSerializer):
    """
    Handles the serialization process of this table.
    """
    class Meta:
        model = Votes
        fields = ["ID", "sub_category", "nominee"]
        read_only_fields = ["created_at", "updated_at"]

    def create(self, validated_data):
        """
        Increments the vote count of a nominee when a vote is done.
        """
        nominee = validated_data["nominee"]
        nominee.votes = +1
        nominee.save()

        return super().create(validated_data)
