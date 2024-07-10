using System;

namespace 練習5
{
    class Program
    {
        static void Main(string[] args)
        {
            int i,N;
            int  a = 1,b=1,c=(a+b);
            Console.Write("請輸入一個整數N: ");
            N = int.Parse(Console.ReadLine());

           
            Console.Write(a+" " +b);
            
            for (i =2; i < N; i++)
            {
                c = a + b;
                Console.Write(" "+c);
                a = b;
                b = c;
            }

            Console.WriteLine();
            Console.Write("列數總和:"+(a+b+c-1)+"  "+ "平均:" + ((a + b + c-1)/(double)N));
            Console.ReadLine();
        }
    }
}
