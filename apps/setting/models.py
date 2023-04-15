from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="описание сайта"
    )
    logo = models.ImageField(
        upload_to="logo",
        verbose_name='логотип сайта'
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Тел.ном"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    adress = models.CharField(
        max_length=250,
        verbose_name="Адресс"
    )
    facebook = models.URLField(
        verbose_name="Facebook"
    )
    instagram = models.URLField(
        verbose_name="Instagram"
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name =  "Настройки сайта"
        verbose_name_plural = "Настройки айта"