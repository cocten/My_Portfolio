using System;

namespace 練習16
{
    class Program
    {
        static void Main(string[] args)
        {
            int ctr;
            String n;            
            char[] s;          
            int[] AZ = new int[26];

            Console.Write("輸入一行英文字:");
            n = Console.ReadLine();
            s = n.ToCharArray();            
            for (ctr = 0; ctr < s.Length; ctr++)
            {
                if (s[ctr] == s[ctr])
                {
                    AZ[(int)s[ctr]-97] = AZ[(int)s[ctr] - 97] + 1;                    
                }
                /*
                if (AZ[(int)s[ctr] - 97] > 0)
                {
                    Console.WriteLine(s[ctr] + AZ[(int)s[ctr] - 97]);
                }
                */
            }

            if (AZ[0] > 0)
            {
                Console.WriteLine("a:"+ AZ[0]);
            }
            if (AZ[1] > 0)
            {
                Console.WriteLine("b:"+AZ[1]);
            }
             if (AZ[2] > 0)
            {
                Console.WriteLine("c" + AZ[2]);
            }
             if (AZ[3] > 0)
            {
                Console.WriteLine("d:" + AZ[3]);
            }           
            if (AZ[4] > 0)
            {
                Console.WriteLine("e:" + AZ[4]);
            }
             if (AZ[5] > 0)
            {
                Console.WriteLine("f:" + AZ[5]);
            }
             if (AZ[6] > 0)
            {
                Console.WriteLine("g:" + AZ[6]);
            }
             if (AZ[7] > 0)
            {
                Console.WriteLine("h:" + AZ[7]);
            }
            if (AZ[8] > 0)
            {
                Console.WriteLine("i:" + AZ[8]);
            }
             if (AZ[9] > 0)
            {
                Console.WriteLine("j:" + AZ[9]);
            }
            if (AZ[10] > 0)
            {
                Console.WriteLine("k:" + AZ[10]);
            }
           if (AZ[11] > 0)
            {
                Console.WriteLine("l:" + AZ[11]);
            }
            if (AZ[12] > 0)
            {
                Console.WriteLine("m:" + AZ[12]);
            }
            if (AZ[13] > 0)
            {
                Console.WriteLine("n:" + AZ[13]);
            }
            if (AZ[14] > 0)
            {
                Console.WriteLine("o:" + AZ[14]);
            }
            if (AZ[15] > 0)
            {
                Console.WriteLine("p:" + AZ[15]);
            }
            if (AZ[16] > 0)
            {
                Console.WriteLine("q:" + AZ[16]);
            }
            if (AZ[17] > 0)
            {
                Console.WriteLine("r:" + AZ[17]);
            }
            if (AZ[18] > 0)
            {
                Console.WriteLine("s:" + AZ[18]);
            }
            if (AZ[19] > 0)
            {
                Console.WriteLine("t:" + AZ[19]);
            }
            if (AZ[20] > 0)
            {
                Console.WriteLine("u:" + AZ[20]);
            }
            if (AZ[21] > 0)
            {
                Console.WriteLine("v:" + AZ[21]);
            }
             if (AZ[22] > 0)
            {
                Console.WriteLine("w:" + AZ[22]);
            }
            if (AZ[23] > 0)
            {
                Console.WriteLine("x:" + AZ[23]);
            }
            if (AZ[24] > 0)
            {
                Console.WriteLine("y:" + AZ[24]);
            }
            if (AZ[25] > 0)
            {
                Console.WriteLine("x:" + AZ[25]);
            }
            Console.ReadLine();
        }
    }
}
