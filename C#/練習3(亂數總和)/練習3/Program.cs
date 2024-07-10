using System;

namespace 練習3
{
    class Program
    {
        static void Main(string[] args)
        {
            int x,n,i,total=0;
            Random r1 = new Random();

            Console.Write("請輸入一個數n:");
            n = int.Parse(Console.ReadLine());

            for(i=1;i<=n;i++)
            {
              x = (r1.Next(1,26));
              Console.WriteLine(x);
                if (x%2.0 == 0)
                {
                    total = total + x;
                }              
            }

            Console.WriteLine("總和:" + total);
            Console.ReadLine();
        }
    }
}
