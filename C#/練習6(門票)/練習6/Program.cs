using System;

namespace 練習6
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, n, x,p=0,p1=0;
            double m;

            Console.Write("請輸入旅遊團人數:");
            n = int.Parse(Console.ReadLine());
            Console.WriteLine();
            for (i=1;i<=n;i++)
            {
                Console.Write("請輸入第" + i + "位年齡:");
                x = int.Parse(Console.ReadLine());
                Console.WriteLine();

                if (x <=6  || x >=65 )
                {
                    p =p+1 ;
                }
                else
                {
                    p1=p1+1;
                }
                
            }

            m = (p * 200 * (double)0.8) + p1*200;
            Console.WriteLine();
            Console.Write("旅遊團人數為"+ n +"人,其中"+ p +"人打八折,供需繳付"+ m +"元");
            Console.ReadLine();
        }
    }
}
