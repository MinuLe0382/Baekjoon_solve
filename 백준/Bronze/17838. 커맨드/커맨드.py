def solution(line):
    return int(
        len(line) == 7
        and len(set(line[0:2] + line[4])) == 1
        and len(set(line[2:4] + line[5:7])) == 1
        and line[0] != line[6]
    )

for _ in range(int(input())):
    print(solution(input()))