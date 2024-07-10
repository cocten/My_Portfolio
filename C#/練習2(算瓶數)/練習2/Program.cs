using System;

namespace 練習2
{
    class Program
    {
        static void Main(string[] args)
        {
            int n;

            Console.Write("請輸入瓶數:");
            n = int.Parse(Console.ReadLine());

            Console.WriteLine("有"+n/12+"打");
            Console.WriteLine("剩"+n%12+"瓶");
            Console.ReadLine();
        }
    }
}
