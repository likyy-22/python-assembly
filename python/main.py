from LegislativeAssembly import LegislativeAssembly
from Member import Member
from Constituency import Constituency
from Session import Session
from Bill import Bill
import sys

def add_member(assembly):
    name = input("Enter Member Name: ")
    constituency_name = input("Enter Constituency Name: ")
    population = int(input("Enter Population: "))
    constituency = Constituency(constituency_name, population)
    party = input("Enter Party: ")
    contact_info = input("Enter Contact Info: ")
    member = Member(name, constituency, party, contact_info)
    assembly.add_member(member)
    print("Member added successfully.")

def schedule_session(assembly):
    date = input("Enter Session Date: ")
    agenda = input("Enter Agenda: ")
    session = Session(date, agenda)
    assembly.schedule_session(session)
    print("Session scheduled successfully.")

def propose_bill(assembly):
    name = input("Enter Member Name: ")
    member = next((m for m in assembly.get_members() if m.name == name), None)
    if member:
        title = input("Enter Bill Title: ")
        description = input("Enter Bill Description: ")
        bill = Bill(title, description)
        member.propose_bill(bill)
        print("Bill proposed successfully.")
    else:
        print("Member not found.")

def vote_on_bill(assembly):
    name = input("Enter Member Name: ")
    member = next((m for m in assembly.get_members() if m.name == name), None)
    if member:
        title = input("Enter Bill Title: ")
        vote = input("Enter Vote (yes/no): ")
        bill = Bill(title, "")
        member.vote_on_bill(bill, vote)
        print("Vote recorded successfully.")
    else:
        print("Member not found.")

def display_members(assembly):
    members = assembly.get_members()
    if not members:
        print("No members found.")
    else:
        print("Members of the Goa Legislative Assembly:")
        for member in members:
            print(f"Name: {member.name}, {member.constituency.get_details()}, Party: {member.party}, Contact Info: {member.contact_info}")

def main():
    assembly = LegislativeAssembly("Goa Legislative Assembly", "Panaji")

    while True:
        print("\nGoa Legislative Assembly Management System")
        print("1. Add Member")
        print("2. Schedule Session")
        print("3. Propose Bill")
        print("4. Vote on Bill")
        print("5. Display Members")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_member(assembly)
        elif choice == 2:
            schedule_session(assembly)
        elif choice == 3:
            propose_bill(assembly)
        elif choice == 4:
            vote_on_bill(assembly)
        elif choice == 5:
            display_members(assembly)
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
