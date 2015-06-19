from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/

    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('', '- - -'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')

    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    interests = models.CharField(max_length=5000, null=True, blank=True, help_text="Eg. swimming reading travelling singing jogging")

    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    photo = models.ImageField(upload_to='user_profile_photos', null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def username(self):
        return self.user.username

    @property
    def name(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    @property
    def age(self):
        return (datetime.date.today() - self.birth_date).days // 365 if self.birth_date else None

    @property
    def gender2(self):
        for x, y in self.GENDER_CHOICES:
            if self.gender == x:
                return y
        return "Unmatched 239"

    @property
    def photo_url(self):
        return settings.MEDIA_URL + str(self.photo)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
