from django.core.management.base import BaseCommand

from shop_app.tasks import update


class Command(BaseCommand):
    help = u'Updates database from warehouse api'  # noqa A003

    def handle(self, *args, **kwargs):
        update()
