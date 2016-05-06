stu_a = {
        "name":"A",
        "age":21,
        "gender":1,
        "hometown":"河北"
}
stu_b = {
        "name":"B",
        "age":22,
        "gender":0,
        "hometown":"山东"
}
stu_c = {
        "name":"C",
        "age":20,
        "gender":1,
        "hometown":"安徽"
}
stu_d = {
        "name":"D",
        "age":20,
        "gender":1,
        "hometown":"安徽"
}
def stu_intro(stu):
        """自我介绍"""
        for key, value in stu.items():
                print("key=%s, value=%d"%(key,value))

stu_intro(stu_a)
stu_intro(stu_b)
stu_intro(stu_c)
stu_intro(stu_d)


'''
class Student:
	name,
	age,
	gender,
	hometown
	def stu_intro(stu):
		print("%s,%s,%s,%s"%(name,age,gender,hometown))


stu_a = Student("a",18,1,'xx')
stu_a.stu_intro()

stu_b = Student("B",18,1,'xx')
stu_b.stu_intro()


stu_c = Student("c",18,1,'xx')
stu_c.stu_intro()
'''

'''
	1、代码量减少
	2、阅读性更高，符合思考习惯
'''