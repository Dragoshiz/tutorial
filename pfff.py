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
def add_teachers_to_school(school, teacher_name, teacher_age, teacher_salary):
	new_teacher = {"name": teacher_name, "age": teacher_age, "salary": teacher_salary}
	school["teachers"].append(new_teacher)
	import ipdb; ipdb.set_trace()
	return school



bod_peter_updated = add_teachers_to_school(
    school= bod_peter,
    teacher_name='Soos Erno',
    teacher_age= 24,
    teacher_salary= 2000
)
bod_peter_updated = add_teachers_to_school(
    school= bod_peter_updated,
    teacher_name='anyad',
    teacher_age= 54,
    teacher_salary= 20005
)
print(bod_peter_updated)