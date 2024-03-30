# n명 중에서 2명을 뽑아 짝으로 만드는 모든 경우를 찾는 알고리즘

def print_pairs(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(a[i], "-", a[j])

name = ['Tom', 'Jerry', 'Mike']
print(print_pairs(name))