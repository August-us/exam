zhishu=[2]
def divPrime(num):
    lt = []
    while num != 1:
        for i in range(2, int(num + 1)):
        # for i in zhishu:
            if num % i == 0:  # i是num的一个质因数
                lt.append(i)
                num = num / i  # 将num除以i，剩下的部分继续分解
                break
    return set(lt)
n=int(input())

import time
start=time.time()
st='''
997,100,889,252,515,30,693,516,484,443,73,632,928,473,375,63,947,260,790,746,485,281,792,701,679,476,977,983,842,20,424,861,95,776,626,14,665,28,153,976,985,696,224,154,484,959,597,952,364,728,840,438,76,956,232,900,800,48,703,429,150,678,897,277,449,151,256,468,769,519,96,872,43,876,261,667,386,200,324,33,600,946,106,508,627,156,762,498,21,893,872,838,496,751,910,38,925,835,749,953,615,555,913,770,577,426,382,30,57,682,405,510,135,515,196,987,353,850,459,485,564,294,425,975,534,384,933,253,749,345,140,774,578,963,22,94,702,337,860,511,794,345,553,419,742,345,56,803,880,939,635,129,778,585,996,688,415,911,36,812,446,620,145,587,884,353,764,959,706,808,499,451,869,820,891,635,928,553,687,649,578,83,169,875,656,336,997,730,883,524,106,884,284,260,318,400,433,519,986,428,899,941,510,808,930,864,726,84,907,33,95,187,974,959,138,848,684,757,141,678,490,49,781,83,721,388,73,41,973,560,685,186,1,691,266,109,650,3,294,731,523,359,429,670,835,32,702,475,187,603,326,595,862,14,688,679,100,483,291,569,506,545,879,443,615,502,257,352,271,623,811,890,232,614,162,393,726,147,423,282,323,389,629,223,545,935,561,214,383,11,620,388,958,997,383,719,482,823,584,85,370,104,599,402,745,406,11,820,228,169,124,646,944,455,746,728,229,384,886,121,744,124,419,286,227,578,922,496,352,498,570,144,221,561,458,960,777,285,197,454,863,50,558,172,28,327,554,189,249,679,721,328,581,866,887,929,23,867,445,511,138,907,586,370,487,358,76,937,829,312,330,152,569,348,406,572,439,235,764,935,589,52,593,803,119,248,459,556,192,293,546,224,878,156,65,969,197,988,423,873,524,735,233,257,295,315,295,109,746,225,437,251,273,31,661,188,686,741,679,691,756,429,539,180,634,180,645,813,199,105,326,36,726,315,949,758,712,60,345,850,43,950,129,189,673,833,11,750,944,756,871,228,705,277,859,61,696,598,633,81,881,47,5,182,182,795,553,770,547,56,43,18,562,940,892,605,439,480,885,94,500,793,531,963,275,940,307,956,699,122,695,963,280,820,514,475,850,564,267,470,45,128,27,538,393,297,523,354,22,931,861,888,922,218,742,556,717,156,205,853,691,199,771,387,523,67,442,353,494,694,939,884,631,603,854,620,632,680,663,56,885,178,442,200,202,123,70,486,863,284,888,993,593,461,100,249,31,96,242,667,863,997,473,590,32,680,805,289,615,676,472,760,712,238,453,257,158,823,471,603,981,842,22,204,468,407,274,565,65,194,533,59,370,507,773,147,967,904,317,92,195,944,371,753,796,657,174,921,568,275,527,575,39,389,629,416,74,675,66,483,748,630,979,910,247,880,611,756,747,368,978,73,103,979,230,259,192,710,521,88,83,148,92,553,277,207,79,979,94,847,396,409,913,825,583,206,381,829,185,837,232,305,348,794,504,822,491,167,249,930,739,154,666,598,724,862,693,313,410,942,912,507,71,517,765,557,704,358,765,223,307,650,271,62,648,156,111,79,50,494,166,689,373,154,329,125,485,61,426,256,798,22,635,203,45,40,418,986,838,189,363,604,899,26,495,616,455,579,68,86,462,93,283,5,793,509,968,211,789,882,686,962,203,67,361,584,31,697,492,854,569,192,726,458,947,562,934,455,613,789,138,594,670,502,929,71,945,544,712,888,209,786,868,313,611,158,646,173,683,888,465,681,349,197,834,843,860,277,523,540,107,979,137,159,725,235,115,349,597,25,37,601,306,366,485,588,17,69,93,550,579,88,386,239,530,684,946,878,538,920,605,823,345,42,759,953,479,241,45,583,418,822,121,829,546,357,186,6,588,188,599,28,167,289,928,997,482,869,482,709,41,353,749,968,169,710,182,558,335,36,956,151,968,938,684,10,231,989,401,655,395,386,95,113,347,174,393,170,221,380,815,214,266,407,787,59,542,380,876,843,868,356,508,524,673,439,215,466,508,249,431,120,878,348,302,687,329,365,681,128,420,562,796,962,139,918,587,151,302,745,888,120,213,335,63,442,835,263,28,417,157,893,581,854,715,539,680,651,872,354,963,655,74,641,845,869,841,213,929,580,945,422,455,874,223,46,549,581,819,295,30,104,380,461,769,479,218,518,246,91,976,191,415,558,938,579,38,141,939,244,15,514,85,875,490,747,439,730,378,405,287,810,169,820,709,726,913,266,766,73

'''
can=list(map(int,st.split(',')))
can=list(map(divPrime,can))
visited=[False for i in range(n)]

def bfs(v):
    result = []
    visited[v] = True
    result.append(v)
    k=0
    while k<len(result):
        i=result[k]
        for j in range(n):
            if not visited[j] and can[i].intersection(can[j]):
                result.append(j)
                visited[j]=True
        k+=1
    return len(result)

max_=0
ord=set()
for i in range(n):
    if visited[i]:
        continue
    max_=max(max_,bfs(i))
print(max_)
print(time.time()-start)
input()
'''
n个结点的数字，有公约数的数字表示有边连接，求最大连通子图的数目
6
20 50 22 74 9 63
'''