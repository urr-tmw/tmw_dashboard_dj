# from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from .department import Department
from .designation import Designation
from common.base_model import TimeStampedModel

class Employee(TimeStampedModel):

    class EmployeeStatus(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        PROBATION = "PROBATION", "Probation"
        NOTICE_PERIOD = "NOTICE_PERIOD", "Notice Period"
        RESIGNED = "RESIGNED", "Resigned"
        TERMINATED = "TERMINATED", "Terminated"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )

    employee_code = models.CharField(
        max_length=20,
        unique=True,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    designation = models.ForeignKey(
        Designation,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    reporting_manager = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="team_members",
    )
    roles = models.ManyToManyField(
    "Role",
    blank=True,
    related_name="employees",
)
    joining_date = models.DateField()

    dashboard_access = models.BooleanField(default=True)

    employee_status = models.CharField(
        max_length=20,
        choices=EmployeeStatus.choices,
        default=EmployeeStatus.ACTIVE,
    )

    class Meta:
        db_table = "employee"
        ordering = ["employee_code"]

    def __str__(self):
        return f"{self.employee_code} - {self.user.username}-{self.department.dept_name}-{self.designation.designation_name}"