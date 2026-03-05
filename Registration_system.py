# School Registration System

# We use a list to store student dictionaries
# Each dictionary represents one student's record
students_db = []

def add_student():
    print("\n--- Register New Student ---")
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Grade Level: ")
    
    # Create a dictionary for the new student
    new_student = {
        "id": student_id,
        "name": name,
        "grade": grade
    }
    
    # Add the dictionary to our main list
    students_db.append(new_student)
    print(f"Success: {name} has been registered.")

def remove_student():
    print("\n--- Remove Student ---")
    target_id = input("Enter the ID of the student to remove: ")
    
    # Search for the student by ID
    for student in students_db:
        if student["id"] == target_id:
            students_db.remove(student)
            print(f"Success: Student ID {target_id} removed.")
            return # Exit the function once found and removed
            
    print("Error: Student ID not found.")

def update_student():
    print("\n--- Update Student Info ---")
    target_id = input("Enter the ID of the student to update: ")
    
    for student in students_db:
        if student["id"] == target_id:
            print(f"Current Info: {student}")
            student["name"] = input("Enter new name (or press enter to keep current): ") or student["name"]
            student["grade"] = input("Enter new grade (or press enter to keep current): ") or student["grade"]
            print("Update complete!")
            return
            
    print("Error: Student ID not found.")

def display_students():
    print("\n--- Current Student List ---")
    if not students_db:
        print("The school registry is currently empty.")
    else:
        # Loop through the list and print formatted details
        for student in students_db:
            print(f"ID: {student['id']} | Name: {student['name']} | Grade: {student['grade']}")

def main_menu():
    """This function acts as the control center for the system."""
    while True:
        print("\n=== School Management System ===")
        print("1. Add New Student")
        print("2. Remove Student")
        print("3. Update Student Information")
        print("4. Show Student List")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            display_students()
        elif choice == '5':
            print("Closing system. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

# Start the program
if __name__ == "__main__":
    main_menu()