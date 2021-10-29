from django.db.models.signals import pre_delete
from django.dispatch import receiver

from tool.models import Interview


@receiver(pre_delete, sender=Interview)
def get_free_interview_slot(sender, instance, **kwargs):
    if instance.recruiter:
        instance.recruiter.interviews -= 1
        instance.recruiter.save()

