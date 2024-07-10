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
			System.out.println("PK前人類生命值"+h1.getLife());
			System.out.println("PK前怪物生命值"+o1.getLife());
			System.out.println();
			System.out.println("-------PK開始-------");
			
			o1.attack(h1);
			h1.attack(o1);
			System.out.println();
			
			
			System.out.println("-------送進魔法屋治療---------");
			MagicHouse.Recovery(h1);
			MagicHouse.Recovery(o1);
			System.out.println();
			
			
			System.out.println("-------- 生命值 -------");
			System.out.println( "目前人類生命值"+ h1.getLife() );		
			System.out.println( "目前怪獸生命值"+ o1.getLife() );
			System.out.println();

			
			System.out.print("按Enter繼續");
			System.in.read();System.in.read();			
			System.out.println();System.out.println();
			Round++;			
		}while( h1.getLife() > 0 && o1.getLife() > 0 );
		
		if( h1.getLife()==0 && o1.getLife()==0)	System.out.println("平手");
		
		else if( h1.getLife()==0 )System.out.println("怪獸贏");
		
		else System.out.println("人類贏");	
		
		
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
		
		System.out.println("怪獸被攻擊，生命損失"+att);
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
		
		System.out.println("人類被攻擊，生命損失"+att);
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
			System.out.println("人類生命回復"+rec1);
			c1.Life+=rec1;
			if(c1.Life>100) c1.Life=100;
			c1.increaseLife(c1.Life);
		}
		if(c1 instanceof Orc)
		{
			System.out.println("怪獸生命回復"+rec2);
			c1.Life+=rec2;
			if(c1.Life>100) c1.Life=100;
			c1.increaseLife(c1.Life);
		}
		}
		
	}
}