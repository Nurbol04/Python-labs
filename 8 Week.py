# 1.1
t = input("Enter: ").lower()
c = list(t)
print("Created list is:")
print(c)

# 1.2
l = []
while True:
    l_input = input("> ").strip()
    if l_input.lower() == 'end':
        break
    try:
        char, count = l_input[0], int(l_input[2:])
        l.append((char, count))
    except (IndexError, ValueError):
        print("Error")
vowels = 'aeiou'
list_vow = []
list_cons = []
list_sym = []
for char, count in l:
    if char in vowels:
        list_vow.append((char, count))
    elif char.isalpha():
        list_cons.append((char, count))
    else:
        list_sym.append((char, count))
print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_sym)


# 2.1
def create_student():
    name = input("Name: ")
    assignments = list(map(int, input("Assignment: ").split()))
    labs = list(map(float, input("Lab: ").split()))
    tests = list(map(int, input("Test: ").split()))
    student = {
        'name': name,
        'assignment': assignments,
        'test': tests,
        'lab': labs
    }
    print("\n2.1:")
    print(f"student = {student}")
    return student


# 2.2
def check_submissions(student):
    submitted_activities = len(student['assignment']) + len(student['lab']) + len(student['test'])
    submission_check = {student['name']: submitted_activities}
    print("\n2.2:")
    print(submission_check)
    return submission_check


# 2.3
def calculate_final_grade(student, submission_check):
    student_name = student['name']
    submitted_count = submission_check.get(student_name, 0)
    if submitted_count >= 4:
        avg_assignment = sum(student['assignment']) / len(student['assignment']) if student['assignment'] else 0
        avg_lab = sum(student['lab']) / len(student['lab']) if student['lab'] else 0
        avg_test = sum(student['test']) / len(student['test']) if student['test'] else 0
        final_grade = 0.3 * avg_assignment + 0.5 * avg_lab + 0.2 * avg_test
    else:
        final_grade = 0
    student['final_grade'] = final_grade
    print("\n2.3:")
    print(f"student = {student}")
    return student


# 2.4
def create_students_dict(*students):
    students_dict = {}
    for student in students:
        students_dict[student['name']] = {k: v for k, v in student.items() if k != 'name'}
    print("\n2.4:")
    print(f"students = {students_dict}")
    return students_dict


num_students = int(input("Number of students: "))
students_list = []
for _ in range(num_students):
    student = create_student()
    submission_check = check_submissions(student)
    student_with_grade = calculate_final_grade(student, submission_check)
    students_list.append(student_with_grade)
students = create_students_dict(*students_list)
