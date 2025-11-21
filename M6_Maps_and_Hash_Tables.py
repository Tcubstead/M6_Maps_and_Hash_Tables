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

