
#LUCHENZA CDSS PYTHON WEBSITE FOR GRADES


#Python Code
import mysql.connector
from mysql.connector import Error

# ---------- DATABASE CONNECTION ----------
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",       #  MySQL host
            user="root",            # MySQL username
            password="your_password", # MySQL password
            database="school_db"    # database name
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# ---------- LUCHENZA CDSS DATABASE SETUP ----------
def setup_database():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS grades (
                id INT AUTO_INCREMENT PRIMARY KEY,
                student_id VARCHAR(20) NOT NULL,
                subject VARCHAR(50) NOT NULL,
                grade VARCHAR(5) NOT NULL
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()

# ---------- TEACHER FUNCTION ON THE LUCHENZA CDSS WEBSITE GRADES ----------
def enter_grade():
    student_id = input("Enter Student ID: ").strip()
    subject = input("Enter Subject: ").strip()
    grade = input("Enter Grade: ").strip().upper()

    if not student_id or not subject or not grade:
        print("All fields are required.")
        return

    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO grades (student_id, subject, grade) VALUES (%s, %s, %s)",
                (student_id, subject, grade)
            )
            conn.commit()
            print("✅ Grade recorded successfully.")
        except Error as e:
            print(f"Error inserting grade: {e}")
        finally:
            cursor.close()
            conn.close()

# ---------- STUDENT FUNCTION ON LUCHENZA CDSS WEBSITE GRADES ----------
def view_grades():
    student_id = input("Enter Your Student ID: ").strip()
    if not student_id:
        print("Student ID is required.")
        return

    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT subject, grade FROM grades WHERE student_id = %s",
                (student_id,)
            )
            results = cursor.fetchall()
            if results:
                print("\n📚 Your Grades:")
                for subject, grade in results:
                    print(f"{subject}: {grade}")
            else:
                print("No grades found for this student.")
        except Error as e:
            print(f"Error retrieving grades: {e}")
        finally:
            cursor.close()
            conn.close()

# ---------- LUCHENZA CDSS ENTERFACE MAIN MENU ----------
def main():
    setup_database()
    while True:
        print("\n--- School Grade System ---")
        print("1. Teacher - Enter Grade")
        print("2. Student - View Grades")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            enter_grade()
        elif choice == "2":
            view_grades()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
#below are important tips for the Luchenza CDSS website to work perfectly
    
#MySQL Setup

#Before running the script, create the database in MySQL:

#CREATE DATABASE school_db;

#How Luchenza CDSS Website Works
#Teachers choose option 1 to enter grades.
#Students choose option 2 to view their grades by entering their Student ID.
#Data is stored in the grades table in MySQL.
