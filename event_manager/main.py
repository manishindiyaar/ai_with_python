import json 
import random 
from datetime import datetime

class Event:

    "A class to represent an event"

    def __init__(self, name, date, description):
        self.id = random.randint(1000, 9999)

        self.name = name
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description

    def to_dict(self):
        """Convert the event to a dictionary for JSON storage.""" 


        return {
            'id': self.id,
            'name': self.name,
            'date': self.date.strftime('%Y-%m-%d'),
            'description': self.description
        }      
    

def load_events():
    """Load events from the JSON file """
    try:
        with open('events.json', 'r') as file:
            return []
        
    except FileNotFoundError:
        return []

def load_file():
    """Load file"""
    try:
        with open('main.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 
       
def save_file(events):
    with open('main.txt', 'w') as file:
        json.dump(events, file, indent=4)




def save_events(events):
    """Save events to the JSON file."""
    with open('events.json', 'w') as file:
        json.dump(events, file, indent=4)

if __name__ == '__main__':
    # Load existing events
    # events = load_events()
    events = load_file()

    # Create a new event
    new_event = Event('Python Workshop', '2023-10-05', 'A workshop about Python basics.')
    events.append(new_event.to_dict())  # Add the new event to the list

    # Save the updated list of events
    # save_events(events)
    save_file(events)