def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)
        
    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = len(prices) - i - 1
            
    return answer