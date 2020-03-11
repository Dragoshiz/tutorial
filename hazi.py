bod_peter = {
    "name": "bod_peter",
    "description": "Fasza",
    "teachers": [{"name": "Joska", "age": 40, "salary": 5000}, {"name": "Len Csaba", "age": 20, "salary": 5000}],
    "classes": {"IX": {"A": {"student_count": 25}, "B": {"student_count": 15}}},
}

gabor_aron = {
    "name": "gabor_aron",
    "description": "Fasza",
    "teachers": [{"name": "Joska", "age": 40, "salary": 5000}, {"name": "Len Csaba", "age": 20, "salary": 5000}],
    "classes": {"IX": {"A": {"student_count": 15}, "B": {"student_count": 15}}},
}

# # write a function to append a new teacher to the teachers list
# parameters are school
#                 teacher name, age, salary
# the function should build the teacher dictionary and append it to the teachers list 
# it should return the updated school

# Programming process
# You should be able to run this program almos every case during building it


def add_teachers_to_school(school, teacher_name, teacher_age, teacher_salary):
    """
    1. Build the teacher dictionary having the same keys (name/age/salary)
       as the rest
        - create a new variable for example `added_teacher`/`new_teacher` which holds
          a dictionary type holding the name/age/salary keys with the coresponding data (
          teacher_name, teacher_age, teacher_salary)
    2. append the new variable (new teacher dictionary) to the school-teachers:
        - the school variable is a dictionary. U want to add this new teacher to the
          `teachers` key (which is a list). to access the teacher list u can do a
          school['teachers'] and u can append to the end by calling `.append(new_teacher)
    3. Return the school variable (which is now updated with the new teacher dict) from the
       function.

    """
    pass



bod_peter_updated = add_teachers_to_school(
    school= bod_peter,
    teacher_name='Soos Erno',
    teacher_age= 24,
    teacher_salary= 2000
)
# TODO: print the bod_peter_updated variable to see if the function returned the
#       updated school (withthe new teacher)

# new_teacher = {"name": "Soos Erno", "age": 24, "salary": 2000}
# bod_peter["teachers"].append(new_teacher)
# print(bod_peter["teachers"])


# def newbodpeti(teacher_name, teacher_age, teacher_salary):
#     print(bod_peter["teachers"]+ teacher_name, teacher_age, teacher_salary)
# newbodpeti(["Soos Erno"], ["24"], ["2000"])