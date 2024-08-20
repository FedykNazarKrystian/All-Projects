from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField("Назва статті", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    full_text = models.TextField("Текст Статті")
    data = models.DateTimeField("Дата Публікації", default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

    def __str__(self):
        return self.title
