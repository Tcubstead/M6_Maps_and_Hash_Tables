#Thomas Cubstead
#Course_Schedule_System
#main
#11/21/25
#

import csv
from schedule import Schedule
from schedule_item import ScheduleItem

def load_schedule_from_csv(filename: str) -> Schedule:
    schedule = Schedule()

    try:
        with open(filename, encoding='utf-8-sig' , newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                item = ScheduleItem(
                    subject=row['Subject'],
                    catalog=row['Catalog'],
                    section=row['Section'],
                    component=row['Component'],
                    session=row['Session'],
                    units=row['Units'],
                    tot_enr=int(row['TotEnr']) if row['TotEnr'] else 0,
                    cap_enr=int(row['CapEnr']) if row['CapEnr'] else 0,
                    instructor=row['Instructor']
                )
                schedule.add_entry(item)

        print(f"Successfully loaded {len(schedule.schedule_dict)} courses from {filename}\n")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error loading file: {e}")

    return schedule

#various display options for the main menu
def display_menu():
    print("\n" + "=" * 50)
    print("Course Schedule System")
    print("=" * 50)
    print("1. Display all courses")
    print("2. Search by subject")
    print("3. Search by subject and catalog number")
    print("4. Search by instructor last name")
    print("5. Exit")
    print("=" * 50)

#prints out the search results with header
def print_rsults(items: list, schedule: Schedule):
    if items:
        print(f"\nFound {len(items)} course(s):\n")
        schedule.print_header()
        for item in items:
            item.print()
    else:
        print("\nNo courses found matching your criteria.")



