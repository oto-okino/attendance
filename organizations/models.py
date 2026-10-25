from django.db import models
from django.conf import settings

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, unique=True)
    address = models.TextField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Workplace(models.Model):
    workplace_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='workspaces')
    address = models.TextField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Employee(models.Model):
    class OrganizationRole(models.TextChoices):
        ADMIN = 'admin', '管理者'
        EMPLOYEE = 'employee', '一般従業員'
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="employee",)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='employees')
    workplaces = models.ManyToManyField(Workplace, through='WorkplaceAssignment', related_name="employees", blank=True)
    employee_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WorkplaceAssignment(models.Model):
    class WorkplaceRole(models.TextChoices):
        MANAGER = 'manager', 'マネージャー'
        STAFF = 'staff', 'スタッフ'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='workplace_assignments')
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE, related_name='workplace_assignments')
    role = models.CharField(max_length=20, choices=WorkplaceRole.choices, default=WorkplaceRole.STAFF)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['employee', 'workplace'], name='unique_employee_workplace')
        ]