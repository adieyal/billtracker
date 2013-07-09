from django.core.management.base import BaseCommand, CommandError
from _scrapegovinfo import scrape

class Command(BaseCommand):
    def handle(self, *args, **options):
        results = scrape()
        for r in results:
            print r

