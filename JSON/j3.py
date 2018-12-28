# 序列化
import json
student = [{"name": "zgs", "age":18},
           {"name": "lele", "age": 24}
          ]
json_str = json.dumps(student)
print(type(json_str))
print(json_str)