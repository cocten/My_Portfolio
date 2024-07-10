using System;

namespace 練習7
{
    class Program
    {
        static void Main(string[] args)
        {
            bool flag;
            int n,total=0;
            double gcd=1;
            int[] N = new int[100];

            Console.Write("結盟的國家數目:");
            n = int.Parse(Console.ReadLine());
            Console.Write("各國參與的忍者人數:");

            for (int i = 0; i < n; i++)
            {
                N[i] = int.Parse(Console.ReadLine());
                total = total + N[i];
            }
        
            for (int i = 1; i <= N[0];i++)
            {
               
                flag = true;//---true
                for (int j=1; j<=n; j++)
                {
                    if (N[j]%i != 0 )//----!=0
                    {
                        flag = false; //change from true to false 
                    }
                }

                if (flag == true)
                {
                    gcd = i;   //if true      gcd=i;
                   // Console.WriteLine("GCD="+gcd);//else
                }
            }

            Console.WriteLine();
            Console.Write("可分成"+gcd+"對，每隊人數是"+(total/(double)gcd)+"人");           
            Console.ReadLine();
        }
    }
}
