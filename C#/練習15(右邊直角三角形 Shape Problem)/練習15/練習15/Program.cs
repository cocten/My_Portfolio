using System;

namespace 練習15
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, j, h;

            Console.Write("請輸入一整數H(1~20):");
            h = int.Parse(Console.ReadLine());

            if (h >= 1 && h <= 20)
            {
                for (i = 1; i <= h; i++)
                {
                    for (j = 1; j <= h; j++)
                    {
                        if (j <= h - i)
                            Console.Write(" ");
                        else
                            Console.Write("*");
                    }
                    Console.WriteLine("\n");
                }
            }           
            else
            {
               Console.WriteLine("輸入錯誤");
            }
               

            Console.Read();
        }
    }
}
