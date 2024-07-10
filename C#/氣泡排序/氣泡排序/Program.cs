using System;

namespace 氣泡排序
{
    class Program
    {
        static void Main(string[] args)
        {           
            int[] n = new int[] { 10, 4, 9, 1, 30, 5, 7, 25, 6, 3, 2, 8,0};
            int i,j,t;

            for (i = 0; i < n.Length - 1; i++)
            {
                for ( j = n.Length - 1; j > i; j--)
                {
                    if (n[j] < n[j - 1])
                    {
                        t = n[j];
                        n[j] = n[j - 1];
                        n[j - 1] = t;
                    }                    
                }
                Console.WriteLine(n[i]);
            }          
            Console.ReadLine();
          
        }
    }
}
