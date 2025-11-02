students = {
    "AUN": {"age": 21, "grade": "A"},
    "ALI": {"age": 22, "grade": "B"},
    "HASSAN": {"age": 20, "grade": "A"},
    "HURRAIZ": {"age": 23, "grade": "C"}
}
for name, info in students.items():
    print(f"{name} is {info['age']} years old and has achieved grade {info['grade']}.")