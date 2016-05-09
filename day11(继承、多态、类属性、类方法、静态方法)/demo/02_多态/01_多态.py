'''
	python是弱类型语言(不需要声明类型，变量的类型是根据右侧的值判断的)
	c#,java都是强类型语言(需要声明类型，一旦类型确定，只能赋值这样类型的值)
	
	比如，要有一个数字，要存储

	python:
			num = 100
			num = 'abc'
	java:
			int num = 100
			num = 'abc'		 X

			String name = 'laowang'
			name = '123'
'''

--java


class Animal{
	public void shout(){
		print('Animal...shout...')
	}
}


class Dog extends Animal{
	public void shout(){
		print('Dog...汪汪...')
	}
}

class Cat extends Animal{
	public void shout(){
		print('Cat...喵喵...')
	}
}

 
class Test{
	public static void main(String[] args){
		Animal a = new Animal()
		test(a)				/*Animal...shout...*/


		a = new Dog()			
		test(a)				/*Dog...汪汪...*/


		a =  new Cat()			
		test(a)				/*Cat...喵喵...*/
		

		

	}
	/*
		这里Animal animal，在调用的时候只能传递 Animal对象，或者子类对象
		父类作为参数，可以传递父类对象，也可以传递子类对象
	*/
	public static void test(Animal animal){
		animal.shout()
	}
}



--python

class Animal:
	def shout():
		print('Animal...shout...')


class Dog(Animal):
	def shout():
		print('Dog...旺旺...')


class Cat(Animal):
	def shout():
		print('Cat...喵喵...')


def test(animal):
	animal.shout()


def main():
	a = Animal()
	test(a)

	a = Dog()
	test(a)

	a = Cat()
	test(a)

main()



'''
C#,java都有接口

接口就是只声明，不实现
在实现类中实现

'''

interface StudentInterface{
	void save(Student stu);
	void deleteById(int id);
	Student selectById(int id);
}

class StudentImplement1 implement StudentInterface{
	public void save(Student stu){
		/*用具体代码实现功能*/
	}
	public void deleteById(int id){
		/*用具体代码实现功能*/
	}
	public Student selectById(int id){
		/*用具体代码实现功能*/
	}
}

class StudentImplement2 implement StudentInterface{
	public void save(Student stu){
		/*用具体代码实现功能*/
	}
	public void deleteById(int id){
		/*用具体代码实现功能*/
	}
	public Student selectById(int id){
		/*用具体代码实现功能*/
	}
}


class Test{
	public static void main(String[] args){
		
		StudentInterface si1 = new StudentImplement1()
		test(si1)

		StudentInterface si2 = new StudentImplement2()
		test(si2)
		

	}
	/*
		接口作为参数，只能传递实现对象
	*/
	public static void test(StudentInterface studentInterface){
		studentInterface.save()
	}
}

--python模拟实现接口

class StudentInterface:
	def save(stu):
		pass
	def deleteById(sid):
		pass
	def selectById(sid):
		pass

	
class StudentImplement(StudentInterface):
	def save(stu):
		print('实现save的功能')

	def deleteById(sid):
		pass
	def selectById(sid):
		pass
