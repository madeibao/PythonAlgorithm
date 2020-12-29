
题目描述
请编写一个函数（允许增加子函数），计算n x m的棋盘格子（n为横向的格子数，m为竖向的格子数）沿着各自边缘线从左上角走到右下角，
总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
输入描述:
输入两个正整数

输出描述:
返回结果

示例1
输入
复制
2
2
输出
复制
6

#----------------------------------------------------------------

while True:
    try:
        def getnum(n,m):
            if n==0 and m==0:
                return  0
            if n==0 or m==0:
                return 1
            return getnum(n-1, m)+getnum(n, m-1)

        a, b = map(int,input().strip().split(" "))
        print(getnum(a,b))


    except:
        break




import java.util.Scanner;
public class Main {

    public static String legal(String[] nums) {
        for(int i=0;i<nums.length;i++) {
            if(Integer.parseInt(nums[i])>=0&&Integer.parseInt(nums[i])<=255 ) {
                continue;
            }
            else {
                return "NO";
            }
        }
        return "YES";
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()) {
            String str= sc.nextLine();
            String[] str2 = str.split("\\.");
            System.out.println(legal(str2));
        }
    }
}