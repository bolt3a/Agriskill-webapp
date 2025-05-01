from django.db import models
from django.contrib.auth.hashers import make_password, check_password as check_hashed_password
from django.core.validators import MinValueValidator, RegexValidator
from django.contrib.auth.models import User
# Base model with shared fields
class UserBase(models.Model):
    full_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    mobile_number = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    password = models.CharField(max_length=128)
    district = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_hashed_password(raw_password, self.password)

# Landowner model
class Landowner(UserBase):
    total_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    help_needed = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Landowner: {self.full_name}"

# Skilled Professional model
class SkilledProfessional(UserBase):
    skills = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Skilled Professional: {self.full_name}"\

class SkillSharePost(models.Model):
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='skillshare_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} - {self.text[:30]}"

