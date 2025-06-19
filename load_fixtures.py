"""
Script to load fixtures from JSON files into a Django database.
"""

import os
import django
import glob
from django.core.management import call_command


# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
django.setup()

from django.contrib.auth.models import User

# Get the path to the fixtures directory
fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

def load_fixtures():
    """
    Load fixtures from JSON files into the database. Only if DB is empty.
    :return: None
    """
    # Check if the database is empty
    if User.objects.exists():
        print("Database is not empty. Skipping fixture loading.")
        return

    if not os.path.exists(fixtures_dir):
        print(f"Fixtures directory '{fixtures_dir}' does not exist.")
        return

    # Find all JSON files in the fixtures directory
    fixture_files = glob.glob(os.path.join(fixtures_dir, '*.json'))
    if not fixture_files:
        print("No JSON fixture files found.")
        from seed import seed_data
        seed_data()
        return

    # Load each fixture file into the database
    for fixture_file in fixture_files:
        fixture_name = os.path.basename(fixture_file)
        print(f"Loading fixture '{fixture_name}'...")
        try:
            call_command('loaddata', fixture_file)
            print(f"Fixture '{fixture_name}' loaded successfully.")
        except Exception as e:
            print(f"Error loading fixture '{fixture_name}': {e}")


if __name__ == "__main__":
    print("Loading fixtures...")
    load_fixtures()
    print("Fixtures loaded.")
