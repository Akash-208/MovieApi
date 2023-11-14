from . models import MovieData
from rest_framework import serializers

# Using ModelSerializer for serializing the data
class MovieSerializer(serializers.ModelSerializer):
    name=serializers.CharField(required=True)
    # rating=serializers.IntegerField(required=True,help_text="Rate it between 1 and 3")
    release_year=serializers.IntegerField(required=True,max_value=2023,initial=2023)
    
    class Meta:
        model=MovieData
        fields = '__all__'