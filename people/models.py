

# Django
from django.contrib.auth.models import User
from django.db import models

class Advisers(models.Model):
    """Profile model."""
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=20,blank=True)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True, 
        null=True
    )
    # asesor=1, supervisor=2, visualizador=3, 4=generncial
    type_user = models.IntegerField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """return username """
        return self.user.username
