class LegislativeAssembly:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.members = []
        self.sessions = []

    def add_member(self, member):
        self.members.append(member)

    def schedule_session(self, session):
        self.sessions.append(session)

    def get_members(self):
        return self.members

    def get_sessions(self):
        return self.sessions
