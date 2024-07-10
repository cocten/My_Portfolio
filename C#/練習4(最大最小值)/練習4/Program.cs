using System;

namespace 練習4
{
    class Program
    {
        static void Main(string[] args)
        {
            int a,max = 0,min = 9999,i;

            for (i = 1; i <= 5; i++)
            {
                Console.Write("請輸入整數:");
                a = int.Parse(Console.ReadLine());

                if (a >= max)
                {
                    max=a;
                }
                if (a <= min)
                {
                    min=a;
                }
            }

            Console.WriteLine();
            Console.WriteLine("最大值" + max);
            Console.WriteLine("最小值" + min);
            Console.ReadLine();
        }
    }
}
