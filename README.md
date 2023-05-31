# Check_Result_Python
This program connects to a MySQL database using the `mysql.connector` module in Python. It assumes that there is a database named "employee" with a table called "stu_result" containing student information and their marks. 

The program prompts the user to enter a student ID and then retrieves all the student IDs from the "stu_result" table. It then iterates through the retrieved IDs and checks if the entered student ID matches any of them. If a match is found, it executes another SQL query to fetch the details of the student with the matching ID.

Once the student details are fetched, the program prints out a formatted mark sheet for the student. It displays the student's name, ID, roll number, and marks in different subjects (Mathematics, Physics, Chemistry, English, and CPF). It also calculates the total marks and displays it, along with the grade and the percentage scored.

If no match is found for the entered student ID, it prints a message stating that the ID was not found.

Overall, this program retrieves and displays the mark sheet for a student based on their ID from a MySQL database.
