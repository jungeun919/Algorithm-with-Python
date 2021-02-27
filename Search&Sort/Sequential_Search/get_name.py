# 학생 번호에 해당하는 학생 이름 찾기

def get_name(student_num, student_name, find_student):
    # n = len(student_num)
    n = len(student_name)
    for i in range(0, n):
        if find_student == student_num[i]:
            return student_name[i]

    return "?"

sample_num = [39, 14, 67, 105]
sample_name = ["Justin", "John", "Mike", "Summer"]

print(get_name(sample_num, sample_name, 105)) # Summer
print(get_name(sample_num, sample_name, 777)) # ?