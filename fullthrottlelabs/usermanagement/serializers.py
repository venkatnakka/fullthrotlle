from rest_framework.serializers import *
from .models import *



class UserActivitySerializer(ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ["start_time","end_time"]

class UserSerializer(ModelSerializer):
    activity = UserActivitySerializer(many=True)
    class Meta:
        model = User
        fields = ["id","real_name","tz","activity"]
