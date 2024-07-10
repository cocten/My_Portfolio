using System;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            int i,j,n,max=0,n1,n2,n3;
            int [] X = new int[100];
            int[] Y = new int[100];
            int[,] D = new int[100,100];

            Console.Write("請輸入有幾個點:");
            n = int.Parse(Console.ReadLine());

            for (i = 1; i <=n ; i++)
            {
                Console.Write("請輸入第" + i + "點的x軸:");
                X[i] = int.Parse(Console.ReadLine());
                Console.Write("請輸入第" + i + "點的y軸:");
                Y[i] = int.Parse(Console.ReadLine());
            }

            for (i = 1; i <= n; i++)
            {
                for (j = i; j <= n; j++)
                {
                    D[i, j] = ((X[i] - X[j + 1]) * (X[i] - X[j + 1])) + ((Y[i] - Y[j + 1]) * (Y[i] - Y[j + 1]));
                    //Console.Write(D[i, j]+"  ");
                    if (D[i, j] > max)
                    {
                        max = D[i, j];
                    }
                }
                //Console.WriteLine("\n");
            }
            /*
            n1 = ((N[2] - N[1]) * (N[2] - N[1])) + ((N1[2] - N1[1]) * (N1[2] - N1[1]));
            n2 = ((N[3] - N[1]) * (N[3] - N[1])) + ((N1[3] - N1[1]) * (N1[3] - N1[1]));
            n3 = ((N[3] - N[2]) * (N[3] - N[2])) + ((N1[3] - N1[2]) * (N1[3] - N1[2]));
            
            if (n1 > n2 && n1 > n3)
            {
                max = n1;
            }
            else if (n2 > n1 && n2 > n3)
            {
                max = n2;
            }
            else
            {
                max = n3;
            }
            */
            Console.WriteLine();
            Console.WriteLine("最長距離是:"+max);
            Console.ReadLine();
        }
    }
}
