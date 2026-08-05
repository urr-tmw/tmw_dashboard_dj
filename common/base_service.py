
from django.db import transaction
from django.shortcuts import get_object_or_404


class BaseMasterService:
    """
    Base service class for all master modules.
    Child classes must define:
        - model
        - serializer_class
        - ordering_field
    """

    model = None
    serializer_class = None
    ordering_field = "id"

    @classmethod
    def get_queryset(cls):
        return cls.model.objects.all().order_by(cls.ordering_field)

    @classmethod
    def get_by_id(cls, object_id):
        return get_object_or_404(
            cls.model,
            id=object_id,
        )

    @classmethod
    @transaction.atomic
    def create(cls, data):

        serializer = cls.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.instance

    @classmethod
    @transaction.atomic
    def update(cls, object_id, data):

        instance = cls.get_by_id(object_id)

        serializer = cls.serializer_class(
            instance,
            data=data,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.instance

    @classmethod
    @transaction.atomic
    def partial_update(cls, object_id, data):

        instance = cls.get_by_id(object_id)

        serializer = cls.serializer_class(
            instance,
            data=data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.instance

    @classmethod
    @transaction.atomic
    def update_status(cls, object_id, is_active):

        instance = cls.get_by_id(object_id)

        instance.is_active = is_active
        instance.save(update_fields=["is_active"])

        return instance

    @classmethod
    @transaction.atomic
    def delete(cls, object_id):

        instance = cls.get_by_id(object_id)
        instance.delete()

        return instance



class BaseService:

    @staticmethod
    @transaction.atomic
    def atomic():
        pass