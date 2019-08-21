import sys


def timing(timestamp):
    t = timestamp.split(':')
    r = int(t[0])*3600 + int(t[1])*60 + int(t[2])
    return r


def main():
    number_of_case = int(sys.stdin.readline().strip())

    for i in range(number_of_case):
        timeline = []
        count = int(sys.stdin.readline().strip())
        for j in range(count):
            s = sys.stdin.readline().strip()
            info = s.split(' ')
            day = int(info[0])
            pre_time = (day-1)*3600*24
            dc = int(info[1])
            for k in range(dc):
                timestr = info[2+k].split('-')
                timeline.append(timing(timestr[0])+pre_time)
                timeline.append(timing(timestr[1])+pre_time)
        timeline.sort()
        request = int(sys.stdin.readline().strip())
        for l in range(request):
            r = sys.stdin.readline().strip()
            info = r.split(' ')
            day = int(info[0])
            pre_time = (day-1)*3600*24
            r_time = pre_time+timing(info[1])
            for m in range(len(timeline)):
                if r_time == timeline[m]:
                    print(0)
                    break
                elif r_time < timeline[m]:
                    if m%2 == 1:
                        print(0)
                    else:
                        print(timeline[m] - r_time)
                    break
                else:
                    continue
            if r_time > timeline[-1]:
                pre_time = 3600*24*7 - r_time
                print(pre_time+timeline[0])

if __name__=="__main__":
    main()