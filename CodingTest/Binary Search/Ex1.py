# 떡볶이 떡을 잘라 손님에게 판다.
# 떡 절단기에 높이(H)를 지정하면 줄지어진 떡을 한번에 절단한다.
# 높이가 H보다 긴 떡은 H 위의 부분이 잘리고, 낮은 떡은 잘리지 않는다.
# 예를 들어, 19,14,10,17인 떡에 15cm 절단기로 자르면 15,14,10,15가 되고,
# 손님은 잘린떡의 길이 4,0,0,2 즉 6cm만큼의 길이를 가져간다.
# 손님이 왔을 떄 요청한 길이가 총 M일때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는
# 높이의 최댓값을 구하는 프로그램을 작성하라.

# 절단기의 높이는 0~10억까지의 정수이므로 이진탐색을 해야함.

N, M = map(int, input().split())
tteok = list(map(int, input().split()))
start = 0
end = max(tteok)
result = 0
while start <= end:
    mid = (start + end) // 2
    length = 0
    for i in tteok:
        if i <= mid:
            continue
        length += i - mid
    if length >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
