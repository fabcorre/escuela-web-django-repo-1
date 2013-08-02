#encoding=utf-8
from django.contrib.auth.models import User
from .models import UserProfile, RegistrationProfile
import factory
from hashlib import md5
import base64

class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: 'testuser_%s' % n)
    first_name = 'John'
    last_name = 'Doe'
    email = factory.LazyAttribute(lambda obj: '%s@tudominio.com' % ('_'.join([obj.first_name, obj.last_name]).lower()))

    @classmethod
    def _prepare(cls, create, **kwargs):
        user = super(cls, UserFactory)._prepare(create, **kwargs)

        user.set_password('1234')

        if create:
            user.save()

        return user


class RegistrationProfileFactory(factory.Factory):
    FACTORY_FOR = RegistrationProfile

    user = factory.SubFactory(UserFactory)
    token = md5('1').hexdigest()
    encoded = factory.LazyAttribute(lambda obj: base64.b64encode('|'.join((obj.token, obj.user.email))))


class UserProfileFactory(factory.Factory):
    FACTORY_FOR = UserProfile

    user = factory.SubFactory(UserFactory)
    gravatar = factory.LazyAttribute(lambda obj: md5(obj.user.email).hexdigest())
    twitter = factory.LazyAttribute(lambda obj: '@%s' % obj.user.username)
