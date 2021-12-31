from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model, User):
    charge = models.FloatField()
    fixed_limit = 1000

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_charge_lte_fixed_limit",
                check=models.Q(charge__lte=models.F("fixed_limit")),
            )
        ]