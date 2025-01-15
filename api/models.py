# # Create your models here.
# class User(models.Model):
#     age = models.IntegerField()
#     name =  models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# print(User)

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class AccessProfile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
        
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    employee_full_name = models.CharField(max_length=200, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    employment_status = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    user_status = models.CharField(max_length=50, blank=True, null=True)
    primary_job = models.CharField(max_length=100, blank=True, null=True)
    department_number = models.CharField(max_length=50, blank=True, null=True)
    department_description = models.CharField(max_length=200, blank=True, null=True)
    reports_to = models.CharField(max_length=100, blank=True, null=True)
    reports_to_employee_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number_1 = models.CharField(max_length=15, blank=True, null=True)
    phone_number_2 = models.CharField(max_length=15, blank=True, null=True)
    phone_number_3 = models.CharField(max_length=15, blank=True, null=True)
    pay_rule = models.CharField(max_length=100, blank=True, null=True)
    hourly_wage_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    worker_type = models.CharField(max_length=50, blank=True, null=True)
    schedule_group_name = models.CharField(max_length=100, blank=True, null=True)
    accrual_profile_name = models.CharField(max_length=100, blank=True, null=True)
    badge_number = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    access_profiles = models.ManyToManyField(AccessProfile, related_name="users", blank=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Permission(models.Model):
    access_profile = models.ForeignKey(AccessProfile, on_delete=models.CASCADE, related_name="permissions")
    function_name = models.CharField(max_length=255)
    can_view = models.BooleanField(default=False)  # Allows all actions

    def __str__(self):
        return f"{self.function_name} - {self.access_profile.name}"

class Punch(models.Model):
    PUNCH_TYPES = [
        ('IN', 'In'),
        ('OUT', 'Out'),
        ('MEAL_IN', 'Meal In'),
        ('MEAL_OUT', 'Meal Out'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='punches')  # Link to User model
    punch_type = models.CharField(max_length=10, choices=PUNCH_TYPES)  # Type of punch
    punch_time = models.DateTimeField()  # Date and time of the punch
    comments = models.TextField(blank=True, null=True)  # Optional comments

    def __str__(self):
        return f"{self.get_punch_type_display()} for {self.user.first_name} at {self.punch_time}"

class Schedule(models.Model):
    STATUS_CHOICES = [
        ('SAVED', 'Saved'),
        ('POSTED', 'Posted'),
    ]

    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='SAVED')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'date', 'start_time', 'end_time')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | {self.date} | {self.start_time} - {self.end_time} ({self.status})"
