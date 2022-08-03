"""
* 2022-08-03

* Five Line Algorithm
class의 시작과 끝 time을 stack에 넣어 동시에 열리는 가장 큰 값을 찾는다.
"""

study = int(input())
classes = [list(map(int, input().split())) for _ in range(study)]

classes_preprocess = []
for start, end in classes:
    classes_preprocess.extend([[1, start], [-1, end]])
classes_sorted = sorted(classes_preprocess, key = lambda x: (x[1], x[0]))

max_classes, local_classes = 0, 0
for case in classes_sorted:
    local_classes += case[0]
    max_classes = max(max_classes, local_classes)
print(max_classes)
