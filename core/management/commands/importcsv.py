from django.core.management.base import BaseCommand
import csv

from core.models import Customer
from core.utils import get_latlon, InvalidCredentialsError



class Command(BaseCommand):
    help = 'Import customers from external CSV file. Takes the complete file path as argument.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='CSV Filename')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        customer_list = []
        do_geocode = True
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['gender'] = row['gender'][:1]
                # Geocoding is done one by one because google does not support multiple addresses per request
                self.stdout.write(f'Importing {row["id"]} {row["first_name"]} {row["last_name"]}')
                if do_geocode:
                    try:
                        row['lat'], row['lon'] = get_latlon(row['city'])
                    except InvalidCredentialsError:
                        do_geocode = False
                customer, created = Customer.objects.update_or_create(**row)
                #customer = Customer(**row)
                customer_list.append(customer)

        # For performance reasons, bulk_create was used. However, for development, I have chosen the update_or_create
        # method instead so I could get partial imports if I interrupt the process.
        #inserted = Customer.objects.bulk_create(customer_list)
        self.stdout.write(f'Done importing {len(customer_list)} customers.')
