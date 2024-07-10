using System;

namespace 練習1
{
    class Program
    {
        static void Main(string[] args)
        {
            int n,a,total=0;

            Console.Write("請輸入一個整數n:");
            n = int.Parse(Console.ReadLine());
            for (a = 1; a <=n; a=a-2)
            {  
                total = total + a;
            }

            Console.WriteLine();
            Console.WriteLine("總和:"+total);
            Console.WriteLine("平均:"+total / (double)n);
            
            Console.ReadLine();
        }
    }
}
