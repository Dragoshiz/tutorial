def add_classes_to_school(school, class_grade, class_type, new_student_count):
	"""
	1. build  a new class dictionary which holds another dictinary rith the student count
	   This dictinary should have the class_type which should hold the other dictionary containing
	   the student_count key and value
	2. Add this new dictionary to the existing classes dictonary (from the school) and return
	   updated school obect
		GOOGLE: python add new value to existing dictionary
	"""
	new_student_count_dict = {"student_count": new_student_count}
	class_type_dict = {class_type: new_student_count_dict}
	class_grade_dict = {class_grade: class_type_dict}
	school['classes'].update(class_grade_dict)
	return school
bod_peter_updated = add_classes_to_school(
	school=bod_peter,
	class_grade= 'XI',
	class_type='A',
	new_student_count=32
)
bod_peter_updated = add_classes_to_school(
	school=bod_peter_updated,
	class_grade= 'XII',
	class_type='C',
	new_student_count=16
)
bod_peter_updated = add_classes_to_school(
	school=bod_peter_updated,
	class_grade= 'X',
	class_type='B',
	new_student_count=60
)
bod_peter_updated = add_teachers_to_school(
	school=bod_peter_updated,
	teacher_name='Ferike Infotanar',
	teacher_age= 44,
	teacher_salary= 4000
)
# write a function wich update the school description 
# it should take a school and a new description parameter and return the updated school
def new_description_to_school(school, new_description):




	bod_peter_updated= new_description_to_school()
