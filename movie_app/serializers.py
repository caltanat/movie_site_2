from rest_framework import serializers
from .models import *


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieListSerializers(serializers.ModelSerializer):
    year = serializers.DateField(format('%Y'))
    genre = GenreSerializers(many=True)
    country = CountrySerializers(many=True)
    avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'movie_image',
                  'year', 'genre', 'country', 'status_movie', 'avg_rating']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class CountryDetailSerializers(serializers.ModelSerializer):
    movies = MovieListSerializers(many=True, read_only=True )
    class Meta:
        model = Country
        fields = ['country_name', 'movies']


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class ActorDetailSerializers(serializers.ModelSerializer):
    actor_movies = MovieListSerializers(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ['actor_image', 'actor_name', 'bio', 'age', 'actor_movies']


class  DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieVideosSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class MovieMomentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class RatingSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    user = ProfileSimpleSerializers()
    class Meta:
        model = Rating
        fields = ['id', 'user', 'text', 'parent', 'stars', 'created_date']


class MovieDetailSerializers(serializers.ModelSerializer):
    year = serializers.DateField(format('%d-%m-%Y'))
    genre = GenreSerializers(many=True)
    country = CountrySerializers(many=True)
    director = DirectorSerializers(many=True)
    actor = ActorSerializers(many=True)
    movie_videos = MovieVideosSerializers(many=True, read_only=True)
    movie_moments = MovieMomentsSerializers(many=True, read_only=True)
    ratings = RatingSerializers(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_image', 'movie_trailer', 'types',
                  'director', 'actor', 'year',
                  'genre', 'country', 'movie_time', 'description',
                  'status_movie', 'movie_videos', 'movie_moments', 'ratings']


class HistorySerializers(serializers.ModelSerializer):
    user = ProfileSimpleSerializers()
    movie = MovieListSerializers()
    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']



class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'
