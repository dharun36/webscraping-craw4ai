import csv
import os

from models.venue import Venue


def is_duplicate_venue(venue_name: str, seen_names: set) -> bool:
    return venue_name in seen_names


def is_complete_venue(venue: dict, required_keys: list) -> bool:
    return all(key in venue for key in required_keys)


def save_venues_to_csv(venues: list, filename: str):
    if not venues:
        print("No venues to save.")
        return

    # Use field names from the Venue model
    fieldnames = Venue.model_fields.keys()

    # Check if the file already exists to determine if we need to write the header
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header only if the file does not exist
        if not file_exists:
            writer.writeheader()
        
        writer.writerows(venues)
    print(f"Appended {len(venues)} venues to '{filename}'.")
