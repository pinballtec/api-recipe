import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as PsycopgError
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for db')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(PsycopgError, OperationalError):
                self.stdout.write('Database is not responding')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is available'))