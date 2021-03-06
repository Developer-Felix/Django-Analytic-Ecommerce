from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
# Create your models here.

User = settings.AUTH_USER_MODEL



class BillingProfile(models.Model):
    """
    """
    user = models.OneToOneField(User,blank=True, null=True,on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user)





def user_created_receiver(sender,instance,created,*args,**kwargs):
    # if created and instance.email:
    #     BillingProfile.objects.get_or_create(user=instance,email=instance.email)
    if created:
        BillingProfile.objects.get_or_create(user=instance)


post_save.connect(user_created_receiver,sender=User)    