from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성" # 첫번째가 실제 저장되는 값, 두번째는 디스프레이 되는 값
        FEMALE = "F", "여"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")], blank=True)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, blank=True)
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요.")

    def send_welcome_email(self):
        subject = render_to_string("accounts/welcome_email_subject.txt", {
            "user": self,
        })
        content = render_to_string("accounts/welcome_email_content.txt", {
            "user": self,
        })
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject, content, sender_email, [self.email], fail_silently=False)