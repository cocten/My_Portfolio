import java.util.*;
import java.io.IOException;

class StreetFight
{
	public static void main(String [] args)throws IOException
	{
		int Round=1;		
		Human h1= new Human();
		Orc o1= new Orc();

		do
		{
			System.out.println("*************Round"+Round+"****************");
			System.out.println("PK�e�H���ͩR��"+h1.getLife());
			System.out.println("PK�e�Ǫ��ͩR��"+o1.getLife());
			System.out.println();
			System.out.println("-------PK�}�l-------");
			
			o1.attack(h1);
			h1.attack(o1);
			System.out.println();
			
			
			System.out.println("-------�e�i�]�k�Ϊv��---------");
			MagicHouse.Recovery(h1);
			MagicHouse.Recovery(o1);
			System.out.println();
			
			
			System.out.println("-------- �ͩR�� -------");
			System.out.println( "�ثe�H���ͩR��"+ h1.getLife() );		
			System.out.println( "�ثe���~�ͩR��"+ o1.getLife() );
			System.out.println();

			
			System.out.print("��Enter�~��");
			System.in.read();System.in.read();			
			System.out.println();System.out.println();
			Round++;			
		}while( h1.getLife() > 0 && o1.getLife() > 0 );
		
		if( h1.getLife()==0 && o1.getLife()==0)	System.out.println("����");
		
		else if( h1.getLife()==0 )System.out.println("���~Ĺ");
		
		else System.out.println("�H��Ĺ");	
		
		
	}
}
class Character
{
	int Life;
	public Character()
	{
		Life=100;
	}
	public int getLife()
	{
		return Life;
	}
	public int increaseLife(int recovery)
	{
		Life=recovery;		
		return Life;
	}
	public int decreaseLife(int attack)
	{
		Life=attack;
		return Life;
	}
}

class Human extends Character
{
	public void attack(Orc o1)
	{
		Random r1=new Random();
		int att=r1.nextInt(25)+1;
		
		o1.Life-=att;
		if(o1.Life<0)o1.Life=0;
		o1.decreaseLife(o1.Life);
		
		System.out.println("���~�Q�����A�ͩR�l��"+att);
	}
}

class Orc extends Character
{
	public void attack(Human h1)
	{
		Random r1=new Random();
		int att=r1.nextInt(25)+1;
		
		h1.Life-=att;
		if(h1.Life<0)h1.Life=0;
		h1.decreaseLife(h1.Life);
		
		System.out.println("�H���Q�����A�ͩR�l��"+att);
	}
}

class MagicHouse
{
	public static void Recovery(Character c1)
	{
		Random r1=new Random();
		int rec1=r1.nextInt(10)+1;
		int rec2=r1.nextInt(10)+1;
		
		if(c1.Life!=0)
		{
		if(c1 instanceof Human)
		{
			System.out.println("�H���ͩR�^�_"+rec1);
			c1.Life+=rec1;
			if(c1.Life>100) c1.Life=100;
			c1.increaseLife(c1.Life);
		}
		if(c1 instanceof Orc)
		{
			System.out.println("���~�ͩR�^�_"+rec2);
			c1.Life+=rec2;
			if(c1.Life>100) c1.Life=100;
			c1.increaseLife(c1.Life);
		}
		}
		
	}
}