import java.util.*;

public class writestudent
{
	public static void main(String [] args)
	{
		Person p1=new Person(1976,10,18);
		p1.setName("���@��");
		p1.showConstellation();
		System.out.println();
		 
	   	s1.setName("���G��");
	   	s1.setBirthday(1976,7,7);   
	   	s1.setSchool("���^��ޤj��");
        s1.showConstellation();		
 	   	s1.showSchool();
	   	System.out.println();
		
		Man m1= new Man();
	   	m1.setName("���T��");
	   	m1.setBirthday(1999,2,10);
	   	m1.setJOb("�{���]�p�v");
        m1.showConstellation();	
	   	m1.showJob();	
	}
}

class Person
{
	public int year,month,day;
	public String name;
	
	public Person()
	{
		this.year=0;
		this.month=0;
		this.day=0;
	}
	public Person(int year,int month,int day)
	{
		this.year=year;
		this.month=month;
		this.day=day;
	}
	public void setName(String name)
	{
		this.name=name;
	}
	public void setBirthday(int year,int month,int ady)
	{
		this.year=year;
		this.month=month;
		this.day=day;
	}
	public void showConstellation()
	{
		if(month==1&&day>=20)
		{
			System.out.println(name+"�O���~�y");
		}
		else if(month==2&&day<=18)
		{
			System.out.println(name+"�O���~�y");
		}
		else if(month==2&&day>=19)
		{
			System.out.println(name+"�O�����y");
		}
		else if(month==3&&day<=20)
		{
			System.out.println(name+"�O�����y");
		}
		else if(month==3&&day>=21)
		{
			System.out.println(name+"�O�d�Ϯy");
		}
		else if(month==4&&day<=19)
		{
			System.out.println(name+"�O�d�Ϯy");
		}
		else if(month==4&&day>=20)
		{
			System.out.println(name+"�O�����y");
		}
		else if(month==5&&day<=20)
		{
			System.out.println(name+"�O�����y");
		}
		else if(month==5&&day>=21)
		{
			System.out.println(name+"�O���l�y");
		}
		else if(month==6&&day<=21)
		{
			System.out.println(name+"�O���l�y");
		}
		else if(month==6&&day>=22)
		{
			System.out.println(name+"�O���ɮy");
		}
		else if(month==7&&day<=22)
		{
			System.out.println(name+"�O���ɮy");
		}
		else if(month==7&&day>=23)
		{
			System.out.println(name+"�O��l�y");
		}
		else if(month==8&&day<=22)
		{
			System.out.println(name+"�O��l�y");
		}
		else if(month==8&&day>=23)
		{
			System.out.println(name+"�O�B�k�y");
		}
		else if(month==9&&day<=22)
		{
			System.out.println(name+"�O�B�k�y");

		}
		else if(month==9&&day>=23)
		{
			System.out.println(name+"�O�ѯ��y");
		}
		else if(month==10&&day<=23)
		{
			System.out.println(name+"�O�ѯ��y");
		}
		else if(month==10&&day>=24)
		{
			System.out.println(name+"�O���Ȯy");
		}
		else if(month==11&&day<=22)
		{
			System.out.println(name+"�O���Ȯy");
		}
		else if(month==11&&day>=23)
		{
			System.out.println(name+"�O�g��y");
		}
		else if(month==12&&day<=21)
		{
			System.out.println(name+"�O�g��y");
		}
		else if(month==12&&day>=22)
		{
			System.out.println(name+"�O�]�~�y");
		}
		else if(month==1&&day<=19)
		{
			System.out.println(name+"�O�]�~�y");
		}
	}
}

class Student extends Person
{
	private String school;
	
	public void setSchool(String school)
	{
		this.school=school;
	}
	public void showSchool()
	{
		System.out.println(name+"�NŪ"+school);
	}
}

class Man extends Person
{
	private String job;
	
	public void setJOb(String job)
	{
		this.job=job;
	}
	public void showJob()
	{
		System.out.println(name+"�u�@�O"+job);
	}
	
}