from rest_framework import serializers
from slavasity.models import *
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name']

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['id', 'name', 'description', 'logo', 'founded_date']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'description', 'logo', 'founded_date']

class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    platforms = PlatformSerializer(many=True, read_only=True)
    developer = DeveloperSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'price', 'image', 'categories', 'platforms', 'release_date', 'developer', 'publisher']

class ReviewSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    user = serializers.StringRelatedField() 
    class Meta:
        model = Review
        fields = ['id', 'game', 'user', 'rating', 'comment', 'created_at']

class PosOrderSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = PosOrder
        fields = ['id', 'order', 'license_key', 'delivery_status', 'updated_at']

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  
    games = GameSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'games', 'total_price', 'created_at', 'status', 'login_address', 'payment_method']

class WishlistSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField() 
    game = GameSerializer(read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'game', 'added_at']

class UserSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    wishlist = WishlistSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'orders', 'reviews', 'wishlist']