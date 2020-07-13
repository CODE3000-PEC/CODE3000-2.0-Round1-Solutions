def maxArea(points):
    area = 0
    start = 0
    end = len(points) - 1
    for _ in range(len(points)): 
        width = abs(start - end)
        if points[start] < points[end]:   
            res = width * points[start]
            start += 1
        else:
            res = width * points[end]
            end -= 1
        if res > area:
            area = res
    return area
n=int(input())
points=list(map(int,input().split()))
print(maxArea(points))
