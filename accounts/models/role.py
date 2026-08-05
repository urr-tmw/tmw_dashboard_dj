from django.db import models

from common.base_model import BaseModel
from accounts.models.permission import Permission


class Role(BaseModel):
    """
    Role Model

    Example:
        HR Manager
        Super Admin
        Attendance Admin
    """

    role_name = models.CharField(
        max_length=100,
        unique=True,
    )

    role_code = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="roles",
    )

    class Meta:
        db_table = "roles"
        ordering = ["role_name"]
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.role_name