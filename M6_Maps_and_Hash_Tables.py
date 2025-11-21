#Thomas Cubstead
#Course_Schedule_System
#main
#11/21/25
#This program loads a course schedule from a CSV file and allows users to search and display courses based on various criteria.

import csv
from schedule import Schedule
from schedule_item import ScheduleItem

#loads the schedule from a csv file into a Schedule object
def load_schedule_from_csv(filename: str) -> Schedule:
    schedule = Schedule()
    try:
        with open(filename, encoding='utf-8-sig', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = ScheduleItem(
                    subject=row['Subject'],
                    catalog=row['Catalog'],
                    section=row['Section'],
                    component=row['Component'],
                    session=row['Session'],
                    units=int(row['Units']) if row['Units'] else 0,
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
def print_results(items: list, schedule: Schedule):
    if items:
        print(f"\nFound {len(items)} course(s):\n")
        schedule.print_header()
        for item in items:
            item.print()
    else:
        print("\nNo courses found matching your criteria.")

#main function to run the program
def main():
    schedule = load_schedule_from_csv('STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv')
    
    #check if data loaded successfully
    if not schedule.schedule_dict:
        print("No data loaded. Closing program.")
        return
    
    #main loop for user interaction
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\n" + "=" * 50)
            print("ALL COURSES")
            print("=" * 50)
            schedule.print()
        
        elif choice == '2':
            subject = input("\nEnter subject code (e.g., BIO, CHM): ").strip()
            results = schedule.find_by_subject(subject)
            print_results(results, schedule)
        
        elif choice == '3':
            subject = input("\nEnter subject code (e.g., BIO, CHM): ").strip()
            catalog = input("Enter catalog number (e.g., 101): ").strip()
            results = schedule.find_by_subject_catalog(subject, catalog)
            print_results(results, schedule)
        
        elif choice == '4':
            last_name = input("\nEnter instructor's last name: ").strip()
            results = schedule.find_by_instructor_last_name(last_name)
            print_results(results, schedule)
        
        elif choice == '5':
            print("\nThanks for using our course schedule system!")
            break
        
        else:
            print("\nInvalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


