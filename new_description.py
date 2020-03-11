bod_peter = {
	"name": "bod_peter",
	"description": "Fasza",
	"teachers": [{"name": "Joska", "age": 40, "salary": 5000}, {"name": "Len Csaba", "age": 20, "salary": 5000}],
	"classes": {"IX": {"A": {"student_count": 25}, "B": {"student_count": 15}}},
}
# write a function wich update the school description 
# it should take a school and a new description parameter and return the updated school
def new_description_to_school(school, new_description):
	newnew_description = {"description" : new_description}
	school["description"] = new_description
	return school

bod_peter_updated= new_description_to_school(
	school= bod_peter,
	new_description = "Egy szar iskola")

import json
print(json.dumps(bod_peter_updated, indent=4))