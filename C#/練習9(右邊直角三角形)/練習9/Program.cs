using System;

namespace 練習9
{
    class Program
    {
        static void Main(string[] args)
        {
            int H;
            Console.Write("請輸入一整數 H：");
            H = int.Parse(Console.ReadLine());
            Console.WriteLine("輸出:");

            if (H >= 1 && H <= 20)
            {
                for (int i = 1; i <= H; i++)
                {
                    for (int j = 1; j <= H; j++)
                    {
                        if (j<=H-i)
                        {
                            Console.Write(" ");
                        }
                        else
                        Console.Write("*");
                    }
                    Console.Write("\n");
                }

            }
            if (H <= 0 || H > 20)
            {
                Console.Write("輸入錯誤");
            }
            Console.ReadLine();
        }
    }
}

        







