from schedule_item import ScheduleItem


class Schedule:
    """Manages a collection of schedule items using a dictionary."""
    
    def __init__(self):
        """Initialize an empty schedule dictionary."""
        self.schedule_dict = {}
    
    def add_entry(self, item: ScheduleItem):
        """Adds a schedule item to the dictionary using its key."""
        key = item.get_key()
        self.schedule_dict[key] = item
    
    def print_header(self):
        """Prints the formatted header for the schedule report."""
        print(f"{'Subject':<8} {'Catalog':<8} {'Section':<8} "
              f"{'Component':<10} {'Session':<8} {'Units':<6} "
              f"{'TotEnrl':<8} {'CapEnrl':<8} {'Instructor'}")
        print("-" * 90)
    
    def print(self):
        """Prints all schedule items with header."""
        self.print_header()
        for item in self.schedule_dict.values():
            item.print()
    
    def find_by_subject(self, subject: str) -> list:
        """Returns a list of items matching the given subject."""
        return [item for item in self.schedule_dict.values() 
                if item.subject.upper() == subject.upper()]
    
    def find_by_subject_catalog(self, subject: str, catalog: str) -> list:
        """Returns a list of items matching subject and catalog number."""
        return [item for item in self.schedule_dict.values() 
                if item.subject.upper() == subject.upper() 
                and item.catalog == catalog]
    
    def find_by_instructor_last_name(self, last_name: str) -> list:
        """Returns a list of items taught by instructor with matching last name."""
        return [item for item in self.schedule_dict.values() 
                if item.instructor.split(',')[0].upper() == last_name.upper()]