def path_num(sx, sy, dx, dy, times):
    if dx < 0 or dx > 8:
        return 0
    if dy < 0 or dy > 8:
        return 0
    if times == 1:
        return 1
    else:
        count_path = 0
        count_path += path_num(sx, sy, sx + 2, sy + 1, times - 1)
        count_path += path_num(sx, sy, sx + 2, sy - 1, times - 1)
        count_path += path_num(sx, sy, sx - 2, sy + 1, times - 1)
        count_path += path_num(sx, sy, sx - 2, sy - 1, times - 1)
        count_path += path_num(sx, sy, sx + 1, sy + 2, times - 1)
        count_path += path_num(sx, sy, sx + 1, sy - 2, times - 1)
        count_path += path_num(sx, sy, sx - 1, sy + 2, times - 1)
        count_path += path_num(sx, sy, sx - 1, sy - 2, times - 1)
        return count_path


times = int(input())
s = raw_input().split(' ')
dx, dy = int(s[0]), int(s[1])
print path_num(0, 0, dx, dy, times)
