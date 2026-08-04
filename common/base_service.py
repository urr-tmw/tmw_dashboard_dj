from django.db import transaction


class BaseService:

    @staticmethod
    @transaction.atomic
    def atomic():
        pass