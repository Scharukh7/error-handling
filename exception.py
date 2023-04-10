import csv

class StudentFailException(Exception):
    pass

filename = '.\student_grades.csv'
try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name = row[0].strip()
            grades = [int(g) for g in row[1:]]

            avg_grade = sum(grades) / len(grades)

            if avg_grade < 70:
                raise StudentFailException(f'{name} has failed with an average grade of {avg_grade:.2f}')
                
            print(f'{name}: Average Grade = {avg_grade:.2f}, Status = PASS')
except FileNotFoundError:
    print("Error: The file 'grades.csv' was not found.")
except ValueError:
    print("Error: The grades in the file must be numeric.")
except StudentFailException as e:
    print(f"Error: {str(e)}")

