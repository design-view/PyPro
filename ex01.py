def solution(arr):
    answer = []
    arr.remove(min(arr))
    if(len(arr)==0):
        arr.append(-1)
    return arr

print(solution([5,4,3,2,7]))