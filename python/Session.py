class Session:
    def __init__(self, date, agenda):
        self.date = date
        self.agenda = agenda
        self.attendees = []

    def add_attendee(self, member):
        self.attendees.append(member)
