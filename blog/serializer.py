from rest_framework import serializers
from .models import Author,post,tag


class Post_Serializer(serializers.ModelSerializer):
	class Meta:
		model = post 
		fields = '__all__'



class AuthorSerializer(serializers.ModelSerializer):
	legacy = Post_Serializer(many=True)
	class Meta:	
		model = Author
		fields = '__all__'


