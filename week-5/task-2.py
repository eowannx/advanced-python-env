import json
import os

def process_student_grades(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            students = json.load(file)

        for student in students:
            grades = student.get('grades', [])
            if grades:
                average = sum(grades) / len(grades)
                student['average_grade'] = round(average, 2)
            else:
                student['average_grade'] = 0

        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(students, file, indent=4, ensure_ascii=False)
        
        print(f"Success! Data saved to: {output_path}")

    except FileNotFoundError:
        print(f"Error: File not found at {input_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    source = os.path.join(script_dir, "students.json")
    result = os.path.join(script_dir, "students_updated.json")
    
    process_student_grades(source, result)