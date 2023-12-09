def find_max(lst):
    stack = []
    max_num = float('-inf')
    for num in lst:
        stack.append(num)
    while stack:
        num = stack.pop()
        if num > max_num:
            max_num = num
        print(f"Current max number: {max_num}")
        if stack and max_num >= stack[-1]:
            continue
        for i in range(len(stack)):
            if stack[i] > max_num:
                stack = stack[i:]
                break
    return max_num
