from django.db import models
from common.base_model import BaseModel

class Department(BaseModel):
    dept_name = models.CharField(max_length=100, unique=True)
    dept_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)



    class Meta:
        db_table = "department"
        ordering = ["dept_name"]

    def __str__(self):
        return self.dept_name