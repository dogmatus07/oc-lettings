from django.db import transaction
from lettings.models import Letting, Address
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
django.setup()


@transaction.atomic()
def seed_data():
    """
    Seed the database with sample data.
    This function creates a sample address and a letting.
    """
    # Check if the database is already populated
    # Check if the database is already populated
    if Letting.objects.exists():
        print("Sample data already populated.")
    else:
        try:
            address = Address.objects.create(
                number=123,
                street="Main Street",
                city="Springfield",
                state="IL",
                zip_code=12345,
                country_iso_code="US"
            )
            Letting.objects.create(title="Cozy Apartment Downtown", address=address)
            print("Sample letting added.")
        except Exception as e:
            print(f"Error seeding data: {e}")


if __name__ == "__main__":
    seed_data()
    print("Database seeded with sample data.")
