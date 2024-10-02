from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy,gettext as _
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_field):
        if not email:
            raise ValueError("user most have some email address.")

        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email ,password):
        if not email:
            raise ValueError("user most have some email address.")

        user = self.create_user(email,password)
        user.active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    national_code = models.CharField(max_length=15)
    address = models.TextField()
    birth_date = models.DateField(null=True,blank=True)
    img = models.ImageField(upload_to='images/profile', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    Objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='images/clinic')
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True, upload_to='images/specialty')

    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)

    def __str__(self):
        return self.user.__str__()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialties = models.ManyToManyField(Specialty)

    def __str__(self):
        return self.user.__str__()


class BusinessHours(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.user.f_name}"


class ClinicDoctor(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('clinic','doctor')

    def __str__(self):
        return f"{self.doctor.user.f_name} - {self.clinic.name}"


class ClinicSpecialty(models.Model):
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('clinic','specialty')

    def __str__(self):
        return f"{self.clinic.name} {self.specialty.name}"


class Appointment(models.Model):
    class StatusChoices(models.TextChoices):
        Booked = 'bo', _('رزرو شده')
        Canceled = 'ca', _('لغو شده')
        Pending = 'pe', _('در انتظار تایید')

    class PaymentStatus(models.TextChoices):
        Paid = 'pa', _('پرداخت شده')
        Unpaid = 'un', _('پرداخت نشده')

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=StatusChoices, default=StatusChoices.Booked)
    payment_status = models.CharField(max_length=2, choices=PaymentStatus, default=PaymentStatus.Unpaid)
    date = models.DateField()

    def __str__(self):
        return f"Appointment for {self.patient.user.__str__()} with {self.doctor.user.__str__()} on {self.date}."

    def price(self):
        clinic_doctor = ClinicDoctor.objects.get(clinic=self.clinic, doctor=self.doctor)
        return clinic_doctor.consultation_fee





