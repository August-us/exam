from typing import List
import numpy as np
from time import time


def bonus(n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
    node = [[0, list(),[i]] for i in range(n + 1)]
    coin = [0 for i in range(n + 1)]
    res = []
    start=time()
    for par, chi in leadership:
        node[chi][0] = par
        node[par][1].append(chi)
        par_,chi_=par, chi
        while par_ !=1:
            node[par_][2].append(chi_)
            par_= node[par_][0]
    # coin=np.array(coin)
    for col in operations:
        if col[0] == 1:
            chi=col[1]
            while chi:
                coin[chi] = (coin[chi]+col[2])%1000000007
                chi=node[chi][0]
            continue
        if col[0] == 2:
            chi = col[1]
            if col[1]!=1:
                # coin[node[chi][2]]+=col[2]*len(node[col[1]][2])
                for i in node[chi][2]:
                    coin[i]= (coin[i]+col[2]*len(node[i][2]))%1000000007
                chi = node[chi][0]
                while chi:
                    coin[chi] = (coin[chi] + col[2]*len(node[col[1]][2])) % 1000000007
                    chi = node[chi][0]
            else:
                coin[1]=(coin[1]+col[2]*n)%1000000007
                for i in range(2,n+1):
                    coin[i] = (coin[i] + col[2] * len(node[i][2])) % 1000000007
            continue
        if col[0] == 3:
            res.append(coin[col[1]])
    print(time()-start)
    return res


def bonus_v3(n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
    node = [[0, list(), list()] for i in range(n + 1)]
    coin = [0 for i in range(n + 1)]
    dfs = [0 for i in range(n + 1)]
    res = []

    def sumCoin(n):
        if node[n][1]:
            return coin[n] + sum(map(sumCoin, node[n][1]))
        else:
            return coin[n]

    for par, chi in leadership:
        node[chi][0] = par
        node[par][1].append(chi)
        par_, chi_ = par, chi
        while par_ != 1:
            node[par_][2].append(chi_)
            par_ = node[par_][0]

    for col in operations:
        if col[0] == 1:
            if col[1] == 1:
                print(col[2])
            coin[col[1]] += col[2]
            continue
        if col[0] == 2:
            if col[1] != 1:
                coin[col[1]] += col[2]
                for i in node[col[1]][2]:
                    coin[i] += col[2]
            else:
                for i in range(1, len(coin)):
                    coin[i] += col[2]
            continue
        if col[0] == 3:
            # res_.append(sumCoin(col[1]))
            if col[1] == 1:
                res.append(sum(coin))
            else:
                res.append(sum([coin[n] for n in node[col[1]][2]]) + coin[col[1]])
    r=[0,sum(coin)]
    for i in range(2,n+1):
        r.append(sum([coin[i] for n in node[i][2]]) + coin[i])
    print(r)
    return list(map(lambda x: x % 1000000007, res))

if __name__ == '__main__':
    '''
    N = 6
    leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]]
    operations = [[1, 1, 500], [2, 2, 50], [3, 1],[2, 6, 15], [3, 1]]
     
    N=408
    leadership=[[1, 283], [1, 52], [1, 273], [1, 217], [1, 136], [1, 211], [1, 179], [283, 293], [283, 292], [283, 227], [283, 54],
     [283, 404], [283, 378], [283, 243], [283, 270], [283, 46], [283, 300], [52, 376], [52, 267], [52, 71], [52, 406],
     [273, 9], [273, 148], [273, 51], [273, 102], [217, 110], [217, 370], [217, 125], [217, 357], [136, 360],
     [136, 260], [136, 196], [136, 228], [136, 103], [136, 347], [136, 384], [211, 25], [179, 3], [179, 140], [179, 56],
     [179, 263], [179, 231], [293, 326], [293, 121], [293, 116], [293, 21], [293, 262], [293, 369], [293, 183],
     [292, 75], [292, 303], [292, 330], [227, 397], [227, 35], [227, 279], [227, 345], [227, 139], [227, 391],
     [227, 266], [54, 16], [404, 214], [404, 184], [404, 68], [404, 27], [378, 192], [378, 87], [378, 39], [378, 386],
     [378, 259], [243, 94], [243, 112], [243, 99], [243, 182], [243, 29], [243, 197], [270, 23], [270, 181], [270, 297],
     [46, 351], [46, 362], [46, 22], [46, 61], [300, 408], [376, 332], [267, 349], [267, 80], [267, 367], [267, 226],
     [71, 72], [71, 389], [71, 163], [71, 100], [71, 107], [71, 92], [71, 85], [406, 353], [406, 199], [406, 257],
     [406, 242], [406, 305], [406, 159], [406, 77], [9, 309], [148, 401], [148, 65], [148, 218], [148, 342], [148, 331],
     [148, 339], [51, 290], [51, 150], [51, 60], [51, 137], [51, 160], [51, 252], [51, 364], [51, 335], [51, 343],
     [51, 304], [102, 180], [102, 138], [110, 74], [110, 171], [110, 390], [110, 352], [110, 37], [370, 377],
     [370, 358], [370, 36], [370, 272], [125, 66], [125, 301], [125, 67], [125, 239], [125, 175], [357, 12], [357, 106],
     [357, 282], [357, 240], [360, 144], [360, 393], [360, 317], [360, 195], [260, 264], [260, 13], [260, 281],
     [260, 400], [260, 212], [260, 365], [260, 402], [260, 63], [260, 255], [196, 193], [196, 338], [228, 399],
     [228, 202], [228, 313], [228, 392], [228, 208], [228, 38], [228, 31], [103, 203], [103, 320], [103, 254],
     [103, 275], [103, 34], [347, 149], [347, 222], [347, 114], [347, 157], [347, 325], [347, 6], [347, 154],
     [347, 250], [347, 350], [384, 93], [384, 123], [384, 374], [384, 50], [25, 285], [25, 20], [25, 288], [25, 251],
     [25, 185], [25, 289], [3, 241], [3, 258], [3, 43], [140, 58], [140, 329], [140, 45], [140, 287], [140, 132],
     [140, 170], [140, 355], [140, 311], [140, 47], [140, 168], [56, 321], [56, 388], [56, 32], [56, 302], [56, 190],
     [56, 48], [56, 11], [263, 96], [263, 30], [263, 24], [263, 26], [231, 229], [231, 164], [231, 128], [231, 295],
     [231, 230], [231, 396], [231, 81], [231, 244], [231, 276], [231, 141], [326, 134], [326, 161], [326, 97],
     [326, 286], [326, 88], [326, 221], [326, 405], [326, 8], [326, 156], [121, 113], [121, 15], [121, 348], [121, 104],
     [121, 398], [121, 91], [121, 40], [121, 64], [121, 318], [121, 111], [116, 271], [21, 83], [21, 55], [262, 368],
     [262, 336], [262, 249], [262, 129], [262, 145], [262, 337], [262, 234], [262, 79], [369, 90], [369, 122],
     [369, 395], [369, 108], [369, 341], [369, 334], [369, 316], [369, 69], [369, 278], [183, 151], [183, 315],
     [183, 17], [183, 178], [183, 274], [183, 269], [75, 200], [75, 131], [75, 126], [75, 19], [75, 359], [75, 70],
     [75, 133], [75, 117], [75, 33], [75, 206], [303, 223], [303, 324], [303, 101], [303, 314], [303, 135], [303, 146],
     [330, 191], [330, 194], [330, 253], [330, 307], [330, 225], [330, 299], [330, 382], [330, 82], [397, 167],
     [397, 2], [397, 308], [397, 246], [397, 245], [397, 265], [35, 261], [35, 328], [35, 224], [35, 296], [35, 340],
     [35, 186], [35, 280], [279, 210], [279, 4], [279, 268], [279, 173], [279, 284], [279, 247], [279, 119], [279, 89],
     [279, 205], [345, 10], [345, 124], [345, 366], [345, 7], [345, 98], [345, 209], [345, 394], [345, 385], [345, 188],
     [345, 166], [139, 153], [139, 327], [139, 127], [139, 155], [139, 312], [391, 235], [391, 76], [391, 381],
     [266, 219], [266, 5], [266, 361], [266, 120], [266, 344], [266, 105], [266, 371], [266, 165], [266, 323], [16, 59],
     [16, 237], [16, 291], [16, 109], [214, 383], [214, 142], [214, 220], [214, 215], [184, 78], [184, 238], [184, 57],
     [68, 204], [27, 356], [27, 322], [27, 62], [27, 162], [27, 407], [27, 14], [27, 152], [27, 86], [27, 84], [27, 95],
     [192, 42], [87, 115], [87, 403], [87, 118], [87, 189], [87, 28], [87, 277], [87, 147], [87, 49], [39, 73],
     [386, 213], [386, 387], [386, 306], [386, 346], [386, 143], [386, 363], [386, 41], [386, 373], [259, 216],
     [259, 372], [259, 169], [259, 248], [259, 354], [259, 53], [259, 44], [259, 380], [259, 256], [94, 333], [94, 172],
     [94, 298], [94, 18], [94, 232], [94, 158], [94, 207], [94, 236], [112, 310], [112, 130], [112, 319], [112, 174],
     [99, 177], [99, 233], [99, 187], [99, 198], [99, 375], [99, 201], [99, 176], [99, 294], [99, 379]]
    operations=[[1, 201, 26], [1, 114, 22], [2, 366, 42], [2, 116, 22], [1, 239, 5], [1, 11, 38], [1, 50, 19], [2, 159, 45],
     [1, 242, 12], [1, 338, 44], [1, 221, 33], [2, 268, 21], [3, 186], [1, 171, 46], [2, 41, 15], [2, 84, 1],
     [1, 210, 30], [2, 109, 28], [2, 164, 16], [2, 40, 8], [1, 129, 30], [3, 268], [2, 163, 16], [2, 345, 44],
     [1, 91, 13], [2, 16, 46], [2, 304, 15], [2, 387, 8], [2, 296, 13], [1, 293, 1], [2, 362, 15], [2, 177, 37],
     [1, 11, 50], [1, 372, 34], [3, 1], [3, 268], [1, 339, 43], [2, 353, 45], [2, 121, 19], [3, 1], [1, 125, 8],
     [1, 160, 44], [1, 66, 43], [1, 98, 2], [3, 52], [2, 108, 41], [3, 245], [1, 66, 45], [3, 52], [1, 132, 49],
     [2, 135, 32], [3, 402], [3, 1], [2, 234, 23], [2, 80, 50], [3, 52], [3, 283], [2, 233, 26], [2, 269, 27],
     [1, 388, 45], [2, 139, 40], [2, 118, 17], [2, 329, 37], [2, 200, 27], [3, 1], [1, 9, 23], [2, 367, 32], [3, 52],
     [2, 314, 23], [1, 50, 2], [3, 283], [1, 320, 25], [3, 154], [1, 270, 48], [1, 213, 30], [2, 297, 12], [2, 404, 20],
     [3, 283], [2, 291, 31], [3, 52], [1, 278, 43], [1, 244, 45], [1, 96, 3], [3, 1], [1, 339, 49], [1, 131, 26],
     [2, 75, 9], [1, 80, 39], [3, 264], [1, 69, 7], [1, 394, 37], [2, 17, 16], [1, 290, 44], [1, 95, 35], [3, 52],
     [2, 361, 8], [1, 195, 18], [1, 63, 15], [3, 52], [1, 309, 8], [2, 368, 28], [3, 1], [3, 1], [1, 311, 48], [3, 125],
     [1, 382, 23], [2, 225, 23], [2, 309, 24], [3, 253], [1, 66, 18], [2, 137, 26], [3, 269], [3, 283], [3, 283],
     [1, 346, 10], [1, 340, 19], [1, 105, 13], [1, 303, 25], [1, 376, 30], [3, 52], [1, 275, 36], [1, 9, 3],
     [1, 190, 36], [1, 312, 10], [3, 366], [1, 248, 24], [1, 360, 41], [3, 1], [3, 1], [2, 367, 27], [1, 209, 19],
     [2, 255, 3], [2, 135, 42], [1, 57, 16], [2, 121, 8], [3, 221], [1, 112, 47], [2, 42, 23], [2, 87, 12],
     [1, 293, 27], [1, 309, 28], [1, 33, 7], [1, 196, 39], [3, 314], [1, 164, 12], [2, 2, 31], [3, 52], [1, 80, 40],
     [3, 52], [3, 283], [3, 1], [2, 212, 16], [3, 1], [3, 52], [2, 50, 43], [3, 1], [1, 14, 42], [3, 283], [2, 404, 32],
     [3, 283], [2, 44, 11], [2, 70, 18], [2, 147, 32], [2, 260, 28], [1, 144, 9], [3, 52], [3, 1], [3, 283], [3, 283],
     [1, 329, 20], [1, 45, 13], [3, 52], [1, 340, 33], [2, 14, 11], [1, 288, 31], [1, 262, 46], [1, 145, 42],
     [2, 303, 24], [1, 392, 3], [1, 295, 24], [2, 213, 5], [1, 368, 13], [1, 228, 14], [1, 375, 47], [3, 283], [3, 161],
     [3, 1], [1, 64, 46], [2, 102, 5], [1, 251, 21], [3, 298], [1, 223, 24], [2, 297, 13], [1, 293, 19], [2, 99, 26],
     [2, 395, 21], [3, 52], [3, 52], [3, 52], [2, 221, 50], [3, 1], [2, 116, 41], [2, 246, 24], [1, 233, 39], [3, 1],
     [2, 318, 5], [2, 63, 43], [1, 142, 46], [2, 367, 38], [2, 193, 47], [1, 34, 27], [1, 302, 25], [3, 1],
     [1, 238, 13], [2, 372, 19], [3, 311], [1, 3, 14], [2, 200, 34], [3, 52], [2, 160, 40], [2, 242, 30], [1, 273, 27],
     [1, 375, 9], [3, 52], [1, 66, 15], [1, 103, 8], [3, 52], [1, 400, 48], [2, 327, 46], [1, 379, 25], [2, 164, 4],
     [2, 358, 4], [2, 356, 1], [2, 175, 7], [2, 261, 37], [3, 283], [1, 155, 7], [2, 214, 9], [1, 154, 42], [1, 12, 22],
     [3, 52], [1, 273, 8], [3, 52], [3, 52], [3, 52], [1, 364, 38], [2, 199, 30], [3, 283], [1, 70, 18], [2, 275, 41],
     [2, 373, 3], [2, 260, 2], [2, 31, 11], [2, 326, 1], [2, 244, 34], [3, 323], [2, 209, 27], [1, 163, 5],
     [1, 131, 45], [1, 3, 44], [2, 311, 34], [1, 8, 35], [1, 78, 49], [2, 342, 32], [2, 231, 46], [2, 124, 23],
     [1, 85, 30], [2, 274, 16], [1, 28, 39], [3, 283], [1, 156, 28], [3, 54], [1, 100, 1], [1, 43, 9], [3, 1],
     [2, 85, 3], [3, 149], [3, 1], [3, 187], [2, 107, 12], [1, 374, 9], [3, 52], [3, 52], [3, 283], [3, 1], [3, 283],
     [2, 365, 10], [1, 89, 27], [3, 52], [2, 145, 44], [1, 220, 33], [2, 116, 8], [1, 94, 26], [3, 283], [3, 52],
     [3, 371], [2, 185, 29], [1, 93, 37], [2, 203, 36], [2, 181, 46], [1, 313, 14], [3, 283], [2, 191, 34], [3, 283],
     [1, 206, 6], [3, 235], [1, 56, 31], [2, 361, 11], [1, 244, 27], [2, 241, 12], [1, 214, 41], [2, 358, 20],
     [1, 340, 37], [2, 126, 18], [2, 101, 44], [1, 23, 46], [2, 323, 24], [3, 52], [1, 301, 12], [2, 224, 43],
     [1, 24, 26], [2, 326, 50], [3, 52], [3, 52], [3, 52], [2, 177, 37], [1, 240, 41], [1, 320, 12], [3, 239],
     [2, 369, 31], [1, 372, 19], [2, 179, 23], [2, 180, 23], [1, 170, 10], [1, 252, 1], [2, 42, 39], [2, 124, 13],
     [1, 263, 19], [1, 244, 1], [1, 84, 37], [1, 187, 8], [3, 283], [2, 175, 43], [1, 203, 38], [3, 1], [2, 19, 29],
     [1, 301, 19], [3, 41], [3, 46], [2, 26, 21], [1, 325, 7], [1, 343, 47], [2, 81, 49], [2, 395, 29], [3, 52],
     [3, 283], [2, 114, 47], [2, 6, 38], [1, 219, 37], [2, 154, 23], [1, 188, 6], [1, 116, 25], [2, 385, 7],
     [1, 289, 3], [2, 295, 2], [3, 1], [3, 1], [3, 52], [3, 283], [3, 52], [2, 140, 2], [3, 1], [1, 248, 40],
     [1, 379, 18], [1, 224, 7], [2, 63, 24], [3, 283], [2, 207, 13], [1, 333, 6], [2, 332, 20], [3, 222], [2, 52, 14],
     [1, 158, 4], [3, 52], [1, 271, 35], [1, 75, 10], [2, 322, 11], [2, 315, 3], [2, 26, 7], [1, 10, 11], [2, 401, 50],
     [1, 9, 18], [3, 1], [1, 28, 39], [1, 185, 3], [3, 52], [1, 162, 20], [1, 247, 5], [3, 52], [1, 308, 9],
     [2, 103, 33], [3, 1], [3, 344], [3, 283], [2, 124, 29], [3, 1], [2, 121, 23], [1, 122, 23], [1, 381, 37],
     [2, 185, 35], [2, 285, 5], [2, 190, 25], [2, 122, 25], [1, 293, 38], [1, 75, 41], [2, 138, 15], [1, 202, 9],
     [1, 121, 42], [3, 52], [2, 83, 23], [3, 325], [3, 1], [2, 350, 41], [2, 337, 50], [2, 198, 19], [1, 221, 32],
     [1, 309, 4], [3, 1], [1, 310, 44], [2, 22, 34], [1, 247, 29], [2, 187, 22], [3, 283], [1, 366, 16], [3, 52],
     [3, 52], [1, 8, 36], [2, 83, 18], [1, 134, 36], [2, 291, 27], [2, 352, 16], [2, 281, 27], [1, 397, 15],
     [2, 215, 40], [2, 190, 4], [2, 98, 17], [3, 331], [2, 21, 32], [1, 56, 10], [1, 388, 42], [1, 225, 3],
     [1, 225, 42], [1, 185, 18], [3, 347], [1, 184, 23], [3, 52], [1, 137, 30], [1, 187, 39], [1, 249, 46],
     [1, 137, 16], [1, 160, 7], [2, 148, 11], [1, 384, 13], [2, 389, 27], [2, 308, 16], [2, 384, 39], [2, 235, 1],
     [2, 117, 6], [2, 222, 11], [3, 1], [3, 52], [1, 249, 5], [2, 321, 28], [2, 365, 14], [2, 2, 34], [3, 362], [3, 52],
     [2, 93, 25], [3, 1], [2, 359, 10], [3, 52], [3, 1], [2, 408, 4], [1, 193, 45], [3, 52], [1, 97, 11], [1, 75, 2],
     [3, 1], [3, 52], [3, 283], [3, 273], [3, 105], [1, 95, 14], [3, 1], [3, 100], [2, 176, 33], [2, 121, 26], [3, 52],
     [1, 331, 21], [2, 83, 14]]
     '''
    N = 423
    leadership = [[1, 120], [1, 140], [1, 313], [1, 371], [1, 252], [1, 170], [120, 197], [120, 233], [120, 26],
                  [120, 215], [120, 260], [120, 192], [120, 33], [120, 209], [120, 52], [120, 104], [140, 131],
                  [140, 314], [140, 297], [140, 389], [313, 63], [371, 73], [371, 118], [371, 154], [371, 230],
                  [371, 89], [371, 288], [371, 304], [371, 46], [371, 376], [371, 338], [252, 37], [252, 17],
                  [252, 198], [252, 204], [252, 367], [252, 55], [252, 190], [170, 274], [170, 325], [170, 183],
                  [197, 32], [197, 382], [197, 193], [197, 271], [197, 82], [197, 266], [197, 11], [197, 416],
                  [197, 379], [233, 42], [233, 319], [233, 283], [26, 287], [26, 148], [26, 244], [26, 261], [26, 222],
                  [26, 227], [26, 111], [26, 392], [26, 31], [215, 139], [215, 181], [215, 106], [260, 149], [260, 399],
                  [192, 98], [192, 79], [192, 91], [192, 92], [192, 275], [33, 195], [33, 56], [33, 370], [209, 176],
                  [209, 249], [209, 101], [209, 272], [209, 420], [209, 210], [209, 408], [209, 94], [209, 277],
                  [209, 356], [52, 68], [104, 228], [131, 280], [131, 105], [131, 308], [131, 232], [131, 110],
                  [131, 217], [131, 182], [131, 361], [314, 264], [314, 96], [314, 219], [314, 38], [314, 114],
                  [314, 59], [314, 144], [314, 84], [297, 203], [297, 108], [297, 22], [297, 223], [297, 14],
                  [389, 156], [389, 303], [389, 35], [389, 216], [389, 45], [389, 97], [389, 306], [63, 300], [63, 21],
                  [63, 100], [63, 292], [63, 220], [63, 12], [63, 116], [63, 127], [73, 299], [73, 231], [73, 117],
                  [73, 332], [73, 189], [73, 254], [73, 58], [73, 201], [73, 334], [73, 404], [118, 317], [118, 2],
                  [118, 402], [118, 19], [118, 213], [154, 372], [230, 323], [230, 85], [230, 273], [230, 388],
                  [230, 138], [230, 93], [89, 391], [89, 348], [89, 340], [89, 191], [288, 57], [288, 9], [288, 278],
                  [288, 107], [288, 168], [304, 133], [46, 62], [46, 39], [46, 284], [46, 380], [46, 137], [46, 242],
                  [376, 236], [376, 99], [376, 171], [376, 15], [376, 162], [376, 390], [376, 6], [376, 417],
                  [338, 258], [338, 350], [338, 403], [338, 86], [338, 135], [338, 61], [338, 72], [338, 302],
                  [338, 360], [37, 344], [37, 321], [37, 363], [37, 354], [37, 161], [17, 164], [17, 243], [17, 362],
                  [198, 246], [198, 407], [198, 366], [198, 113], [204, 208], [204, 81], [367, 368], [367, 311],
                  [367, 395], [55, 393], [55, 157], [55, 25], [190, 318], [274, 410], [274, 188], [274, 145],
                  [274, 423], [274, 3], [274, 387], [274, 247], [325, 206], [325, 211], [325, 295], [325, 240],
                  [325, 5], [325, 200], [183, 421], [183, 172], [183, 187], [183, 119], [32, 146], [32, 259], [32, 347],
                  [32, 43], [32, 129], [32, 289], [32, 337], [32, 320], [32, 134], [382, 256], [382, 414], [382, 141],
                  [382, 77], [382, 177], [382, 64], [382, 310], [382, 78], [382, 253], [193, 4], [193, 398], [193, 268],
                  [193, 169], [193, 296], [193, 124], [193, 301], [193, 36], [193, 374], [193, 281], [271, 394],
                  [271, 333], [271, 155], [271, 186], [271, 305], [82, 196], [82, 199], [82, 132], [82, 336], [82, 263],
                  [82, 385], [82, 396], [266, 365], [11, 235], [11, 405], [11, 115], [11, 205], [416, 257], [416, 328],
                  [416, 50], [416, 125], [379, 326], [379, 34], [379, 121], [379, 179], [379, 16], [379, 364],
                  [379, 51], [379, 174], [42, 234], [42, 406], [42, 324], [42, 331], [42, 70], [42, 71], [319, 341],
                  [319, 165], [319, 269], [319, 255], [319, 226], [319, 335], [319, 159], [319, 207], [319, 173],
                  [283, 327], [283, 60], [283, 315], [283, 241], [283, 49], [287, 422], [287, 8], [287, 250],
                  [287, 401], [287, 262], [148, 214], [148, 330], [244, 80], [244, 276], [244, 378], [244, 29],
                  [244, 184], [261, 251], [222, 343], [222, 48], [222, 13], [222, 150], [227, 27], [227, 298],
                  [227, 65], [227, 285], [227, 76], [227, 342], [227, 142], [227, 67], [111, 353], [111, 40],
                  [111, 151], [111, 160], [111, 95], [392, 87], [392, 381], [392, 384], [392, 286], [392, 109],
                  [392, 282], [392, 267], [392, 66], [31, 419], [31, 352], [31, 307], [31, 24], [139, 83], [139, 358],
                  [139, 229], [139, 355], [181, 412], [181, 122], [181, 18], [181, 221], [106, 369], [149, 413],
                  [149, 373], [149, 158], [149, 245], [149, 74], [399, 54], [399, 224], [399, 377], [98, 112],
                  [98, 185], [79, 23], [79, 53], [79, 152], [79, 44], [79, 290], [79, 346], [79, 357], [79, 47],
                  [79, 175], [79, 28], [91, 178], [91, 20], [91, 397], [91, 69], [91, 90], [91, 10], [92, 163],
                  [92, 265], [92, 293], [92, 349], [92, 225], [92, 400], [92, 239], [92, 279], [92, 202], [92, 180],
                  [275, 218], [275, 75], [275, 294], [195, 386], [195, 322], [56, 136], [56, 359], [56, 194], [56, 238],
                  [56, 147], [56, 383], [56, 41], [56, 411], [56, 102], [56, 329], [370, 309], [370, 316], [370, 409],
                  [370, 270], [370, 418], [370, 237], [370, 103], [176, 130], [249, 167], [249, 126], [249, 339],
                  [249, 30], [249, 375], [249, 166], [249, 123], [249, 7], [101, 291], [101, 212], [101, 248],
                  [272, 88], [272, 345], [272, 312], [272, 143], [272, 415], [272, 351], [272, 153], [272, 128]]
    operations = [[1, 306, 17], [1, 62, 2], [1, 332, 37], [2, 414, 12], [3, 140], [3, 140], [1, 350, 30], [3, 140],
                  [2, 396, 7], [2, 8, 21], [1, 339, 20], [2, 154, 21], [1, 108, 15], [3, 1], [1, 244, 3], [3, 120],
                  [2, 78, 23], [3, 120], [3, 120], [3, 140], [3, 1], [2, 407, 40], [1, 102, 23], [3, 1], [1, 120, 5],
                  [1, 321, 38], [1, 98, 35], [2, 207, 43], [2, 354, 40], [1, 329, 33], [3, 1], [3, 140], [1, 30, 17],
                  [2, 404, 34], [3, 120], [3, 120], [1, 234, 22], [2, 321, 45], [3, 140], [1, 74, 36], [3, 140],
                  [3, 120], [2, 186, 22], [2, 14, 7], [2, 89, 25], [1, 157, 11], [3, 120], [1, 126, 16], [1, 113, 30],
                  [1, 351, 27], [2, 106, 21], [2, 145, 23], [1, 280, 6], [2, 65, 21], [2, 355, 15], [3, 1],
                  [1, 407, 32], [1, 171, 30], [1, 198, 40], [3, 1], [2, 357, 3], [2, 136, 4], [1, 193, 3], [3, 1],
                  [2, 36, 38], [3, 120], [2, 188, 17], [3, 140], [2, 1, 19], [2, 174, 33], [1, 151, 14], [3, 140],
                  [3, 111], [2, 312, 5], [2, 337, 26], [1, 230, 4], [2, 19, 9], [1, 354, 24], [3, 120], [2, 366, 22],
                  [3, 371], [3, 1], [1, 332, 37], [1, 222, 13], [3, 140], [1, 283, 21], [3, 271], [3, 1], [1, 149, 36],
                  [1, 412, 30], [1, 200, 23], [1, 297, 46], [2, 7, 22], [3, 140], [2, 54, 4], [3, 120], [1, 324, 50],
                  [3, 1], [2, 138, 44], [3, 1], [1, 246, 9], [1, 316, 11], [2, 167, 23], [1, 244, 37], [2, 182, 41],
                  [1, 128, 4], [3, 1], [2, 412, 14], [3, 1], [1, 37, 37], [1, 7, 19], [2, 60, 33], [3, 140],
                  [1, 85, 24], [2, 61, 5], [2, 316, 19], [2, 341, 31], [3, 1], [3, 255], [1, 234, 31], [3, 120],
                  [1, 142, 50], [3, 140], [3, 1], [2, 289, 39], [1, 307, 6], [3, 120], [1, 34, 41], [1, 106, 43],
                  [2, 405, 2], [3, 140], [1, 204, 18], [1, 107, 15], [2, 333, 7], [3, 1], [2, 232, 8], [3, 1], [3, 140],
                  [3, 120], [1, 366, 1], [2, 373, 49], [2, 178, 27], [3, 120], [2, 70, 19], [2, 100, 36], [2, 165, 11],
                  [2, 249, 13], [2, 320, 16], [2, 218, 9], [3, 179], [1, 70, 31], [3, 1], [3, 1], [3, 120],
                  [1, 156, 32], [1, 395, 42], [1, 395, 39], [2, 396, 25], [3, 140], [1, 240, 45], [3, 1], [3, 120],
                  [2, 73, 29], [2, 423, 14], [2, 214, 28], [2, 387, 11], [3, 148], [3, 140], [3, 120], [1, 242, 42],
                  [2, 11, 29], [3, 140], [1, 213, 17], [1, 203, 30], [3, 1], [1, 165, 15], [1, 64, 1], [1, 36, 7],
                  [1, 409, 41], [3, 120], [3, 140], [2, 313, 6], [3, 1], [1, 25, 46], [1, 273, 38], [3, 140], [3, 140],
                  [1, 278, 35], [3, 1], [3, 1], [1, 291, 29], [1, 56, 40], [2, 153, 42], [2, 153, 31], [1, 126, 4],
                  [2, 277, 25], [1, 73, 37], [2, 341, 12], [2, 411, 40], [1, 266, 47], [1, 220, 32], [3, 120],
                  [2, 254, 39], [1, 272, 14], [1, 423, 12], [1, 22, 3], [3, 248], [1, 20, 6], [2, 95, 25], [1, 389, 19],
                  [3, 1], [2, 258, 46], [2, 359, 12], [3, 140], [2, 396, 9], [3, 140], [3, 120], [1, 48, 14],
                  [2, 141, 8], [1, 93, 15], [1, 130, 3], [3, 140], [2, 177, 8], [3, 1], [2, 124, 33], [2, 38, 50],
                  [3, 120], [2, 356, 21], [2, 34, 1], [1, 110, 4], [3, 120], [1, 44, 44], [2, 144, 21], [3, 1],
                  [3, 356], [1, 146, 32], [1, 229, 22], [1, 257, 2], [1, 139, 12], [3, 370], [3, 120], [3, 140],
                  [3, 120], [2, 327, 5], [2, 89, 35], [1, 419, 36], [3, 396], [2, 218, 5], [1, 292, 48], [3, 1],
                  [3, 140], [3, 140], [3, 121], [2, 363, 48], [1, 301, 34], [1, 239, 49], [2, 187, 18], [1, 304, 20],
                  [3, 1], [2, 81, 9], [1, 388, 14], [3, 364], [3, 293], [1, 366, 28], [1, 204, 15], [1, 413, 11],
                  [1, 186, 10], [2, 169, 27], [1, 157, 26], [3, 1], [2, 344, 31], [2, 234, 4], [1, 330, 41], [3, 1],
                  [1, 130, 7], [2, 61, 33], [2, 323, 41], [2, 71, 19], [3, 1], [1, 258, 20], [1, 108, 9], [3, 140],
                  [3, 120], [2, 60, 14], [1, 122, 26], [3, 140], [3, 120], [2, 356, 7], [1, 2, 8], [2, 353, 23],
                  [1, 280, 40], [3, 1], [1, 300, 8], [2, 345, 9], [1, 239, 40], [1, 149, 12], [2, 161, 40],
                  [2, 224, 27], [3, 140], [3, 140], [2, 140, 26], [1, 263, 44], [3, 1], [3, 140], [3, 140],
                  [1, 135, 23], [2, 316, 23], [1, 138, 34], [2, 129, 34], [3, 230], [2, 118, 44], [2, 423, 29],
                  [2, 191, 1], [3, 1], [2, 248, 33], [3, 1], [1, 362, 44], [1, 265, 4], [2, 178, 29], [2, 178, 44],
                  [2, 202, 22], [3, 120], [3, 203], [2, 305, 42], [3, 120], [1, 355, 50], [2, 168, 3], [1, 221, 37],
                  [1, 297, 49], [1, 336, 12], [3, 1], [3, 140], [2, 231, 46], [2, 241, 41], [3, 140], [1, 228, 50],
                  [3, 42], [2, 269, 17], [3, 1], [1, 231, 50], [3, 120], [3, 1], [1, 347, 33], [2, 295, 47],
                  [2, 202, 9], [3, 164], [1, 106, 33], [3, 140], [2, 343, 25], [1, 6, 18], [3, 120], [1, 343, 31],
                  [1, 419, 39], [3, 1], [1, 383, 10], [2, 188, 30], [3, 27], [1, 337, 9], [3, 120], [2, 138, 37],
                  [3, 184], [2, 88, 18], [1, 410, 14], [2, 272, 40], [1, 285, 46], [2, 260, 4], [1, 371, 9],
                  [1, 71, 46], [1, 215, 35], [1, 93, 10], [1, 174, 38], [2, 206, 47], [1, 168, 34], [3, 140], [3, 140],
                  [1, 367, 13], [3, 1], [3, 120], [1, 61, 19], [1, 280, 23], [1, 233, 34], [2, 138, 27], [1, 390, 49],
                  [2, 278, 39], [3, 1], [2, 267, 29], [1, 23, 34], [2, 285, 1], [2, 59, 37], [3, 140], [2, 135, 14],
                  [3, 10], [1, 109, 25], [2, 422, 38], [2, 226, 15], [3, 1], [1, 411, 45], [2, 144, 7], [2, 177, 43],
                  [2, 60, 9], [3, 1], [1, 256, 19], [2, 155, 1], [2, 50, 44], [1, 283, 41], [3, 120], [1, 161, 3],
                  [1, 49, 33], [3, 120], [2, 66, 21], [2, 5, 39], [2, 328, 22], [3, 357], [2, 311, 44], [2, 98, 3],
                  [2, 279, 31], [3, 1], [2, 261, 11], [3, 140], [2, 338, 39], [2, 339, 33], [2, 111, 50], [3, 46],
                  [2, 211, 23], [2, 40, 47], [2, 234, 42], [3, 120], [1, 47, 26], [2, 419, 27], [3, 87], [2, 280, 25],
                  [3, 120], [2, 415, 8], [3, 120], [2, 139, 5], [3, 34], [3, 270], [3, 80], [1, 189, 15], [2, 57, 10],
                  [1, 55, 49], [1, 229, 38], [3, 1], [2, 125, 6], [3, 140], [1, 280, 10], [3, 373], [3, 118], [3, 120],
                  [1, 397, 18], [3, 296], [1, 146, 41], [3, 120], [1, 57, 3], [1, 286, 16], [1, 29, 27], [2, 159, 17],
                  [2, 274, 4], [1, 360, 34], [2, 111, 16], [3, 120], [3, 140], [3, 120], [3, 104], [1, 229, 23],
                  [2, 269, 27], [3, 120], [1, 285, 33], [2, 48, 2], [3, 120], [2, 34, 49], [1, 213, 23], [1, 220, 44],
                  [2, 266, 5], [2, 265, 44], [1, 247, 42], [3, 140], [3, 120], [2, 76, 21], [1, 153, 20], [3, 1],
                  [3, 120], [2, 213, 30], [2, 161, 13], [3, 1], [3, 1], [1, 30, 49], [1, 313, 45], [1, 373, 6],
                  [2, 391, 44], [2, 223, 10], [2, 2, 24], [1, 363, 20], [2, 63, 50], [2, 219, 33], [3, 140], [2, 5, 12],
                  [1, 391, 40], [1, 136, 19], [1, 198, 28]]
    print(bonus(N,leadership,operations))
    # print(bonus_v3(N,leadership,operations))

    input()

