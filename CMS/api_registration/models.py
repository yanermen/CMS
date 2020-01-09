from django.db import models


class PersonData(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=50, blank=True, null=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=50, blank=True, null=True)
    username = models.CharField(verbose_name="Username", max_length=50, blank=True, null=True, db_index=True,
                                unique=True,)
    password = models.CharField(verbose_name="Password", max_length=50, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='cms', on_delete=models.CASCADE)

    def __str__(self):
        return self.username

