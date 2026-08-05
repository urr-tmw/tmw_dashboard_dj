from django.db import models

from common.base_model import BaseModel
from django.utils.text import slugify

class Permission(BaseModel):
    """
    Stores individual permissions.
    Example:
        Module : Department
        Action : View
        Code   : department.view
    """

    module = models.CharField(
        max_length=100,
        db_index=True,
    )

    action = models.CharField(
        max_length=50,
        db_index=True,
    )

    permission_name = models.CharField(
        max_length=150,
        unique=True,
    )

    permission_code = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "permissions"
        ordering = ["module", "action"]
        verbose_name = "Permission"
        verbose_name_plural = "Permissions"

    def save(self, *args, **kwargs):
        if not self.permission_code:
            self.permission_code = slugify(f"{self.module}.{self.action}")
        if not self.permission_name:
            self.permission_name = f"{self.module} {self.action}"
        super().save(*args, **kwargs)


    def __str__(self):
        return self.permission_name