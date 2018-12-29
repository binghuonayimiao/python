import json
json_str = '{"name":"zgs", "age":18}'
student = json.loads(json_str)
print(type(student))
print(student)
print(student["name"])
