from rest_framework import serializers
from .models import Book, Journal


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = '__all__'




class JournalSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Journal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Journal
        fields = '__all__'