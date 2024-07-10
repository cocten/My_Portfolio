using System;

namespace 練習12
{
    class Program
    {
        static void Main(string[] args)
        {
            int n,i,c=0,u;
            bool judge;

            Console.Write("請輸入指定Ugly Number(1<=N<=300):");
            n = int.Parse(Console.ReadLine());
            i = 1;
            while (true)
            {
                u = i;
                judge = true; 
                while (u!= 1)
                {
                    if (u % 5 == 0)
                    {
                        u /= 5;
                    }
                    else if (u % 3 == 0)
                    {
                        u /= 3;
                    }
                    else if (u% 2 == 0)
                    {
                        u /= 2;
                    }                    
                    else
                    {
                        judge = false;
                        break;
                    }                    
                }               
                if (judge==true)
                {
                    c = c + 1;                    
                }                                
                if (c == n) break;
                i++;
            }

            Console.WriteLine("第"+n+ "個Ugly Number為:"+i);
            Console.ReadLine();
        }
    }
}
