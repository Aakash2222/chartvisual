import json
from django.core.management.base import BaseCommand, CommandError
from chartapp.models import Product

class Command(BaseCommand):
    help = 'Import External Json File data into Django Database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file_path = options['json_file']

        try:
            with open(json_file_path, 'r', encoding='utf8') as file:
                data = json.load(file)

                for index, item in enumerate(data, start=1):
                    try:
                        Product.objects.create(
                            end_year=item['end_year'],
                            intensity=int(item.get('intensity', 0) or 0),
                            sector=item['sector'],
                            topic=item['topic'],
                            insight=item['insight'][:255],  # Truncate if longer than 255 characters
                            url=item['url'][:255],  # Truncate if longer than 255 characters
                            region=item['region'][:255],  # Truncate if longer than 255 characters
                            start_year=item['start_year'],
                            impact=int(item.get('impact', 0) or 0),
                            added=item['added'],
                            published=item['published'],
                            country=item['country'],
                            relevance=int(item.get('relevance', 0) or 0),
                            pestle=item['pestle'],
                            source=item['source'],
                            title=item['title'][:255],  # Truncate if longer than 255 characters
                            likelihood=int(item.get('likelihood', 0) or 0),
                        )
                    except KeyError as e:
                        self.stderr.write(self.style.ERROR(f"KeyError: {e} missing in item at index {index}"))
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f"Error: {e} occurred while importing item at index {index}"))
        except FileNotFoundError:
            raise CommandError("File not found")

        except Exception as e:
            raise CommandError(f"Error: {e} occurred while opening file")

        self.stdout.write(self.style.SUCCESS('Import done'))
