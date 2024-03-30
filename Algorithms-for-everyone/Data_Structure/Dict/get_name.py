# 딕셔너리로 학생 번호에 해당하는 학생 이름 찾기

def get_name(student_info, find_num):
    if find_num in student_info:
        return student_info[find_num]
    else:
        return "?"

sample_info = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

print(get_name(sample_info, 105)) # Summer
print(get_name(sample_info, 777)) # ?