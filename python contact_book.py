import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file if it exists, else start empty
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        contacts = json.load(f)
else:
    contacts = []

def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=2)
    print("✅ Saved!")

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    skill = input("Skill (e.g. Plumber, Designer): ")
    note = input("Note: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "skill": skill,
        "note": note
    }
    contacts.append(new_contact)
    save_contacts()
    print(f"✅ {name} added!")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
        return
    print("\n--- ALL CONTACTS ---")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['skill']} | {c['note']}")

def search_contact():
    query = input("Search name or skill: ").lower()
    found = False
    for c in contacts:
        if query in c['name'].lower() or query in c['skill'].lower():
            print(f"FOUND: {c['name']} | {c['phone']} | {c['skill']} | {c['note']}")
            found = True
    if not found:
        print("No match found.")

def delete_contact():
    view_contacts()
    try:
        num = int(input("Enter number to delete: "))
        removed = contacts.pop(num - 1)
        save_contacts()
        print(f"🗑️ Deleted {removed['name']}")
    except:
        print("Invalid number!")

# Main Menu Loop
while True:
    print("\n=== CONTACT BOOK 🇰🇪 ===")
    print("1. Add Contact")
    print("2. View All")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")
    choice = input("Choose (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Bye G! 👋")
        break
    else:
        print("Invalid choice, try again.")