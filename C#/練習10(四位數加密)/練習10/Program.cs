using System;

namespace 練習10
{
    class Program
    {
        static void Main(string[] args)
        {
            int n,a,b,c,d,t;            

            Console.Write("請輸入四位整數數字的密碼:");
            n = int.Parse(Console.ReadLine());
            a = n / 1000;
            b = (n-(a*1000))/100;
            c = (n - (a * 1000)-(b*100)) / 10;
            d = (n - (a * 1000) - (b * 100) - (c * 10));
            
            //加密
            a = (a + 7) % 10;
            b = (b + 7) % 10;
            c = (c + 7) % 10;
            d = (d + 7) % 10;

            //換位置
            t = a;
            a = c;
            c = t;
            t = b;
            b = d;
            d = t;


            Console.Write("加密後的密碼為:"+a+b+c+d);

            Console.ReadLine();
        }
    }
}
