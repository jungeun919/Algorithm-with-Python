# 친구 리스트에서 자신의 모든 친구를 찾는 알고리즘

def print_all_friends(g, start):
    qu = [] # 앞으로 처리해야 할 사람들을 큐에 저장
    done = set() # 이미 큐에 추가한 사람들을 집합에 기록 (중복 방지)

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

# 친구 관계 리스트
friend_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends(friend_info, 'Summer')
print()
print_all_friends(friend_info, 'Jerry')