import numpy as np
import copy
import math


def main():                                             # 掃き出し法による逆行列演算(きっと精度よい)
    n = int(input("Input size of matrix>>"))
    Denom = np.array([[1 for i in range(n)] for j in range(n)])
    Numer = np.array([[0 for i in range(n)] for j in range(n)])
    IdenD = np.array([[1 for i in range(n)] for j in range(n)])
    IdenN = np.array([[0 for i in range(n)] for j in range(n)])

    print("Input number>>")
    i = 0
    while (i < n):
        j = 0
        while (j < n):
            Numer[i, j] = float(input("numerator("+str(i)+","+str(j)+"):"))
            Denom[i, j] = float(input("denominator("+str(i)+","+str(j)+"):"))
            j += 1
        i += 1

    for i in range(n):
        IdenN[i][i] = 1

    i = 0
    while (i < n):
        j = 0
        search_nonzero(i, n, Denom, Numer, IdenD, IdenN)
        memD = Denom[i, i]
        memN = Numer[i, i]
        Denom[i, :] *= memN
        Numer[i, :] *= memD
        IdenD[i, :] *= memN
        IdenN[i, :] *= memD
        reduct(j, n, Denom, Numer)
        reduct(j, n, IdenD, IdenN)

        while (j < n):
            if (i == j):
                pass
            else:
                k = 0
                memD = Denom[j, i]
                memN = Numer[j, i]
                while (k < n):
                    subtract(i, j, k, memD, memN, Denom, Numer)
                    subtract(i, j, k, memD, memN, IdenD, IdenN)
                    k += 1
            reduct(j, n, Denom, Numer)
            reduct(j, n, IdenD, IdenN)

            j += 1

        i += 1


def search_nonzero(i, n, Denom, Numer, IdenD, IdenN):   # (i,i)成分として0でない行を取得
    if (Numer[i, i] != 0):
        return
    else:
        j = i + 1
        while (j < n):
            if (Numer[j, i] != 0):
                replace(i, j, Denom)
                replace(i, j, Numer)
                replace(i, j, IdenD)
                replace(i, j, IdenN)
                return
            j += 1
        error()


def replace(i, j, array):                               # 行の入れ替え
    mem = copy.deepcopy(array[i, :])
    array[i, :] = array[j, :]
    array[j, :] = mem


def reduct(j, n, Denom, Numer):                         # 約分
    i = 0
    while (i < n):
        gcd = math.gcd(Denom[j, i], Numer[j, i])
        Denom[j, i] /= gcd
        Numer[j, i] /= gcd
        i += 1


def subtract(i, j, k, memD, memN, Denom, Numer):        # 行の引き算
    subDenom = Denom[i, k] * memD
    subNumer = Numer[i, k] * memN
    num = lcm(Denom[j, k], subDenom)
    Numer[j, k] = Numer[j, k] * num / Denom[j, k] - subNumer * num / subDenom
    Denom[j, k] = num


def lcm(a, b):                                          # 最小公倍数
    return a*b/math.gcd(a, b)


def error():
    print("There is no inverse matrix.")
    exit()


if __name__ == "__main__":
    main()
