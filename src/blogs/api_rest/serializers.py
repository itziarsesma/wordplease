from rest_framework import serializers
from rest_framework.reverse import reverse


class BlogSerializer(serializers.Serializer):

    username = serializers.CharField()
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return self.context.get('request').build_absolute_uri(reverse('user_posts_list', args=[obj.get('username')]))