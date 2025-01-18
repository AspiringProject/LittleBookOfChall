def convert_to_grade(mark, max_mark=100):
    percentage = (mark / max_mark) * 100
    if percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    elif percentage >= 40:
        return 'E'
    else:
        return 'U'

def main():
    # Get module 1 results
    mark1 = int(input("Enter Module 1 result: "))
    max_mark1 = int(input("Enter maximum mark for Module 1: "))
    grade1 = convert_to_grade(mark1, max_mark1)
    
    # Get module 2 results
    mark2 = int(input("Enter Module 2 result: "))
    max_mark2 = int(input("Enter maximum mark for Module 2: "))
    grade2 = convert_to_grade(mark2, max_mark2)
    
    # Display individual module grades
    print(f"Module 1: {grade1}")
    print(f"Module 2: {grade2}")
    
    # Calculate overall grade
    total_mark = mark1 + mark2
    total_max_mark = max_mark1 + max_mark2
    overall_grade = convert_to_grade(total_mark, total_max_mark)
    
    # Display overall grade
    print(f"AS Level: {overall_grade}")

if __name__ == "__main__":
    main()