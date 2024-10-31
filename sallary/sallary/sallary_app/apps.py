from django.apps import AppConfig


class SallaryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sallary_app'

    def ready(self):
        from .tasks import send_welcome_email
        send_welcome_email.delay('nazarfediku@gmail.com')
