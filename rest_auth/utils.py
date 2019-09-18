from six import string_types
from importlib import import_module
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


def import_callable(path_or_callable):
    if hasattr(path_or_callable, '__call__'):
        return path_or_callable
    else:
        assert isinstance(path_or_callable, string_types)
        package, attr = path_or_callable.rsplit('.', 1)
        return getattr(import_module(package), attr)


def default_create_token(token_model, user, serializer):
    token, _ = token_model.objects.get_or_create(user=user)
    return token


def jwt_encode(user):
    refresh = TokenObtainPairSerializer.get_token(user)
    return refresh.access_token, refresh
