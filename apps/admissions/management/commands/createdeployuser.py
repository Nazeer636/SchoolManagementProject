import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a deployment user if it does not already exist"

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("DEPLOY_USERNAME")
        password = os.environ.get("DEPLOY_PASSWORD")
        email = os.environ.get("DEPLOY_EMAIL", "")

        if not username or not password:
            self.stdout.write(
                self.style.WARNING(
                    "DEPLOY_USERNAME or DEPLOY_PASSWORD is not set."
                )
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.SUCCESS(
                    f"User '{username}' already exists."
                )
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"User '{username}' created successfully."
            )
        )