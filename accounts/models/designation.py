from django.db import models
from accounts.models import Department
from common.base_model import BaseModel

class Designation(BaseModel):
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="designations"
    )

    designation_name = models.CharField(max_length=100)
    designation_code = models.CharField(max_length=20)

    description = models.TextField(blank=True, null=True)



    class Meta:
        db_table = "designation"
        ordering = ["designation_name"]
        constraints = [
            models.UniqueConstraint(
                fields=["department", "designation_name"],
                name="unique_department_designation_name"
            ),
            models.UniqueConstraint(
                fields=["department", "designation_code"],
                name="unique_department_designation_code"
            ),
        ]

    def __str__(self):
        return f"{self.designation_name}"