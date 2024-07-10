import java.util.*;

class test
{
	public static void main(String [] args)
	{
		Random r1=new Random();
		int rec1=r1.nextInt(10)+1;
		int rec2=r1.nextInt(10)+1;
		
		System.out.println("目前人類生命回復"+rec1);
		System.out.println("目前怪獸生命回復"+rec2);
	}	
} 