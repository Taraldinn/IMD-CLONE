from rest_framework import serializers
from watchlist.models import StreamPlatform, Watchlist, Review


# TODO: model serializers part


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Watchlist
        fields = "__all__"


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    # watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie-details'

    class Meta:
        model = StreamPlatform
        fields = "__all__"

# TODO: functional serializers part

# def name_length(value):
#     if len(value)< 2:
#         raise serializers.ValidationError("Name is Too short")

#     else:
#         return value
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         """
#             Create and return a new `Snippet` instance, given the validated data.
#             """
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
