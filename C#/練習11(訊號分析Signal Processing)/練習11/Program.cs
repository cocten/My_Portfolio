using System;

namespace 練習11
{
    class Program
    {
        static void Main(string[] args)
        {
            int t=0,max=0,ctr;
            String  n;
            char[] s;
            char x;

            Console.Write("輸入訊號:");
            n = Console.ReadLine();
            s = n.ToCharArray();
            x = s[0];
            for (ctr = 0; ctr <(s.Length-1); ctr++)
            {
                // Console.WriteLine("{0}: {1}", ctr, s[ctr]);
                if (s[ctr] == s[ctr+1])
                {                    
                    t = t + 1;
                }
                else
                {                  
                    if (t > max)
                    {
                        max = t;
                        x =  s[ctr];
                    }
                   t = 1;
                }               
            }
           
            Console.WriteLine("最長的文字為:"+x);
            Console.WriteLine("長度為:"+max);           
            Console.ReadLine();
        }
    }
}
