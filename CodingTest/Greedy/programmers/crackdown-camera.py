# 과속 카메라, 그리디

# 진출점을 기준으로 오름차순 정렬을 하고 첫번째 진출점에 카메라 설치.
# 다음 차량의 진입점이 카메라 설치 지점보다 앞이면 단속카메라를 만남. 아니면 새로운 카메라 설치.
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    camera = [routes[0][1]]
    for route in routes[1:]:
        i, o = route
        if camera[-1] < i:
            camera.append(o)
    return len(camera)
