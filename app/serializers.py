from rest_framework import serializers
from .models import Task, Lkstatuscode

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','task_for', 'last_modified_on', 'lk_status_code']
    
    def update(self, validated_data):
        # Manually update the object without running full validation
        lk_status_code = Lkstatuscode.objects.filter(
            lk_status_code=validated_data.get('lk_status_code')).last(
                ) or self.instance.lk_status_code
        self.instance.task_for = validated_data.get('task_for', self.instance.task_for)
        self.instance.lk_status_code = lk_status_code
        self.instance.save()
        return self.instance    
        
class LKStatusCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lkstatuscode
        fields = ['id', 'task_for', 'last_modified_on', 'lk_status_code']
        
                