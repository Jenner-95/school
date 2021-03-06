from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  tipo = models.SmallIntegerField(choices=[(1, 'Administrador'), (2, 'Profesor'), (3, 'Estudiante')])

  def __str__(self):
        return self.get_full_name()

  def get_full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance, tipo=1)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()
