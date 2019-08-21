def addPoint(n):
    if len(n)!=1 and n[0]=='0' and n[-1]=='0':
        return 0
    if len(n)==1 or n[0]=='0' or n[-1]=='0':
        return 1
    else:
        return len(n)


def main():
    s=input()
    if len(s)==1:
        return 0
    if s[0]=='0' and s[1]=='0':
        if   s[-1]=='0':
            return 0
        else: return 1

    else:
        times=0
        for i in range(len(s)-1):
            times+=addPoint(s[:i+1])*addPoint(s[i+1:])
        return times


if __name__=="__main__":
    print(main())
