using System;

namespace 氣泡排序正解
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] n = new int[] { 10, 4, 9, 1, 30, 5, 7, 25, 6, 3, 2, 8, 0 };
            int i, j, t;

            for (i = n.Length-1; i > 0; i--)
            {
                for (j = 0; j < i; j++)
                {
                    if (n[j] > n[j + 1])
                    {
                        t = n[j];
                        n[j] = n[j + 1];
                        n[j + 1] = t;
                    }
                }              
            }
            for (i=0;i<n.Length;i++)
            {
                Console.Write(n[i] + "/n" +"/r");
            }
            /*
            foreach (int number in n)
            {
                Console.WriteLine("{0} ", number);
            }
            */
            Console.ReadLine();
        }
    }
}
