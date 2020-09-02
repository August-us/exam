def gcd(a, b):
    while a:
        a,b= b%a ,a
    return b

def ext_euclid(a, b):
    '''
    :param a: 求逆元的数
    :param b:需要取模的质数
    :return:
    r_{i+1}=r_{i-1}-q_i*r_i
    r_{i+1}=as_{i+1}+bt_{i+1}
    '''
    old_s,s=1,0
    # old_t,t=0,1
    old_r,r=a,b
    if b == 0:
        # return 1, 0, a
        return
    else:
        while(r!=0):
            print(r,s)
            q=old_r//r
            old_r,r=r,old_r-q*r
            old_s,s=s,old_s-q*s
            # old_t,t=t,old_t-q*t
            # 这里r=as+bt
    # return old_s, old_t, old_r
    return old_s%b