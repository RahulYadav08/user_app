from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active']

    def get_len_name(self, object):
        return len(object.name)

    # #Field level validator
    def validate_name(self, value):

        if len(value)<2:
            raise serializers.ValidationError("Name is too short")

        return value

# Field level validator
    def validate_description(self, value):

        if len(value)<3:
            raise serializers.ValidationError("Description is too long")

        return value
        


# def name_length(value):
#     if len(value)<2:
#         raise serializers.ValidationError("Name is too short")

#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators = [name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # #Field level validator
#     # def validate_name(self, value):

#     #     if len(value)<2:
#     #         raise serializers.ValidationError("Name is too short")

#     #     return value

# # Field level validator
#     def validate_description(self, value):

#         if len(value)<3:
#             raise serializers.ValidationError("Description is too long")

#         return value


# # Object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description cannot be the same")
        
#         return data
