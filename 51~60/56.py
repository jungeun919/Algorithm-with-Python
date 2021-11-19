# 다음의 딕셔너리가 주어졌을 때 한국의 면적과 가장 비슷한 국가와 그 차이를 출력하세요.

nationWidth = {
	'korea': 220877, 
	'Rusia': 17098242, 
	'China': 9596961, 
	'France': 543965, 
	'Japan': 377915,
	'England' : 242900,
}

width = nationWidth['korea'] # 220877
nationWidth.pop('korea')

list = list(nationWidth.items())
print(list)

gap = max(nationWidth.values()) # 17098242

item = ''
for i in list:
    if gap > abs(i[1] - width):
        gap = abs(i[1] - width)
        item = i
print(item[0], item[1] - width)