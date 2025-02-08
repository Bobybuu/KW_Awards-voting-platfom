from rest_framework import serializers
from ..models import User
#import cloudinary.uploader  # Assuming you are using Cloudinary for file uploads


class UserSerializer(serializers.ModelSerializer):
    profile_photo_file = serializers.FileField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "stage_name",
            "email", "id", "is_staff",
            "type", "phone_number", "profile_photo",
            "bio", "created_at", "updated_at",
            "profile_photo_file", "password"
        ]

    def create(self, validated_data):
        # Handle file saving, fake saving to Cloudinary (replace with actual Cloudinary logic)
        
        profile_photo_file = validated_data.get('profile_photo_file', None)
        
        if profile_photo_file:
            # Simulating saving the image to Cloudinary
            # response = cloudinary.uploader.upload(profile_photo)
            # You can return the URL for the saved file if using Cloudinary
            # self.validated_data['profile_photo'] = response['secure_url']
            
            # For now, we're faking the URL to be some cloud URL
            self.validated_data['profile_photo'] = "https://fake-cloudinary-url.com/fake_image.jpg"

        user = User.objects.create(**validated_data)
        return user
