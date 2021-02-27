from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, nickname, password):
        if not username:
            raise ValueError("아이디를 입력해주세요.")
        if not nickname:
            raise ValueError("닉네임을 입력해주세요.")
        user = self.model(username=username, nickname=nickname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, password):
        user = self.create_user(username=username, nickname=nickname, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    username = models.CharField(_("ID"), max_length=20, unique=True)
    nickname = models.CharField(_("닉네임"), max_length=16, unique=True)
    is_staff = models.BooleanField(_("스태프 여부"), default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nickname"]

    class Meta:
        verbose_name = "회원"
        verbose_name_plural = "회원"