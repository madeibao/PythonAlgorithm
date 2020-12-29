

1000000.00 0.0490 360 



# #贷款额为a，月利率为i，年利率为I，还款月数为n
# a = 500000.00
# I = 0.11495
# i = I/12
# n = 60

# a,i, n= int(input().spli(" "))

# 房贷等额本息算法

''''
# 计算房贷等额本息法应还款的额度并输出结果
def averageCapitalPlusInterest(principal, principalRatio, anualInterestRate, month):
    # principal表示房价总额,principalRatio表示房贷百分比,anualInterestRate表示房贷年利率,month表示房贷月份
    mortgage = np.around(principal * principalRatio, 2)  # 计算需要贷款的金额
    monthlyPayment = np.around(mortgage * averageCapitalPlusInterestRate(month, monthlyInterestRate(anualInterestRate)),
                               2)  # 计算每月应还款金额
    totalInt = np.around(totalInterest(mortgage, monthlyPayment, month), 2)
    mortgageIntoTenThousand = np.around(mortgage / 10000, 2)  # 将贷款总金额转化为万元

    print("每月应还:", monthlyPayment, "元")  # 输出结果
    totalPayment = np.around(monthlyPayment * month, 2)  # 还款总额

    res = []
    res.append(monthlyPayment)
    res.append(monthlyPayment)
    res.append(principal+totalPayment)

    return res




# 计算每月利率
def monthlyInterestRate(anualInterestRate):
    return (anualInterestRate / 12) / 100  # 年利率/12


# 计算比例系数
def averageCapitalPlusInterestRate(month, monthlyInterestRate):
    R = monthlyInterestRate
    N = month
    I = R * math.pow(1 + R, N) / (math.pow(1 + R, N) - 1)
    return I


def totalInterest(mortgage, monthlyPayment, month):
    return monthlyPayment * month - mortgage


# 示例
averageCapitalPlusInterest(1000000.00, 1, 4.9, 360)

'''



#coding=utf-8
import numpy as np
import math
 
#房贷等额本金算法
def averageCapital(principal,principalRatio,anualInterestRate,month):
    #principal表示房价总额,principalRatio表示房贷百分比,anualInterestRate表示房贷年利率,month表示房贷月份
    monthlyPayment = np.zeros(month) #初始化每月还款金额
    cont = 0
    mortgage = np.around(principal*principalRatio,2) #计算需要贷款的金额
    mortgageIntoTenThousand = np.around(mortgage/10000,2) #将贷款总金额转化为万元
    print("贷款:",mortgageIntoTenThousand,"万元") #输出结果
    print("年利率:",anualInterestRate,"%")
    print("按揭月数:",month,"月")
    for i in range(0,month):
        monthlyPayment[i] = np.around((mortgage/month)+((mortgage)*monthlyInterestRate(anualInterestRate)) - (i*(mortgage/month)*monthlyInterestRate(anualInterestRate)),2)
        #每月还款金额
        cont += np.around(monthlyPayment[i],2)
        
        print("第",i+1,"月应还款:",monthlyPayment[i],"元") #输出结果
    totalPayment = np.around(sum(monthlyPayment),2) #计算还款总额
    print("还款总额:",totalPayment,"元")
    return totalPayment 
 
#计算每月利率        
def monthlyInterestRate(anualInterestRate):
    return (anualInterestRate/12)/100 #年利率/12
 
averageCapital(1000000,1,4.9,240)