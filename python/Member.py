from Constituency import Constituency

class Member:
    def __init__(self, name, constituency, party, contact_info):
        self.name = name
        self.constituency = constituency
        self.party = party
        self.contact_info = contact_info

    def attend_session(self, session):
        session.add_attendee(self)

    def propose_bill(self, bill):
        print(f"{self.name} has proposed the bill: {bill.title}")

    def vote_on_bill(self, bill, vote):
        print(f"{self.name} has voted {vote} on the bill: {bill.title}")
