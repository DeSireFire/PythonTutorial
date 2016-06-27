drop table if exists booktest_bookinfo;
create table booktest_bookinfo(
	id int auto_increment primary key,
  btitle varchar(100),
  bpubdate date,
  bread int,
  bcomment int,
	isdelete bit
);

insert into booktest_bookinfo(btitle,bpubdate,bread,bcomment,isdelete) values
('射雕英雄传','1980-5-1',12,34,0),
('天龙八部','1986-7-24',36,40,0),
('笑傲江湖','1995-12-24',20,80,0),
('雪山飞狐','1987-11-11',58,24,0);

select * from booktest_bookinfo;

drop table if exists booktest_heroinfo;
create table booktest_heroinfo(
	id int auto_increment primary key,
  hname varchar(100),
  hgender bit,
  hbookinfo_id int,
  hcontent varchar(200),
	isdelete bit,
  foreign key(hbookinfo_id) references booktest_bookinfo(id)
);


insert into booktest_heroinfo(hname,hgender,hbookinfo_id,hcontent,isDelete) values
('郭靖',1,1,'降龙十八掌',0),
('黄蓉',0,1,'打狗棍法',0),
('黄药师',1,1,'弹指神通',0),
('欧阳锋',1,1,'蛤蟆功',0),
('梅超风',0,1,'九阴白骨爪',0),
('乔峰',1,2,'降龙十八掌',0),
('段誉',1,2,'六脉神剑',0),
('虚竹',1,2,'天山六阳掌',0),
('王语嫣',0,2,'神仙姐姐',0),
('令狐冲',1,3,'独孤九剑',0),
('任盈盈',0,3,'弹琴',0),
('岳不群',1,3,'华山剑法',0),
('东方不败',0,3,'葵花宝典',0),
('胡斐',1,4,'胡家刀法',0),
('苗若兰',0,4,'黄衣',0),
('程灵素',0,4,'医术',0),
('袁紫衣',0,4,'六合拳',0);

select * from booktest_heroinfo;
select * from booktest_bookinfo;







/********************************部门表dept********************************/
/*创建表*/
DROP TABLE  IF EXISTS booktest_dept;  
CREATE TABLE booktest_dept(
	DEPTNO INT PRIMARY KEY,  
	DNAME VARCHAR(14) ,  
	LOC VARCHAR(13) 
);
/*插入数据*/
INSERT INTO booktest_dept VALUES  
(10,'ACCOUNTING','NEW YORK'),  
(20,'RESEARCH','DALLAS'), 
(30,'SALES','CHICAGO'),
(40,'OPERATIONS','BOSTON');  
/*查询数据*/
SELECT * FROM booktest_dept;


/********************************员工表emp********************************/
/*创建表*/
DROP TABLE  IF EXISTS booktest_emp;  
CREATE TABLE booktest_emp(
	EMPNO INT PRIMARY KEY,  
	ENAME VARCHAR(14) ,  
	JOB VARCHAR(9),  
  MGR INT,  
  HIREDATE DATE,  
  SAL DECIMAL(7,2),  
  COMM DECIMAL(7,2),  
  DEPTNO int,
  FOREIGN KEY(DEPTNO) REFERENCES booktest_dept(DEPTNO)
);

/*插入数据*/
INSERT INTO booktest_emp VALUES  
(7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20),
(7499,'ALLEN','SALESMAN',7698,'1981-2-20',1600,300,30), 
(7521,'WARD','SALESMAN',7698,'1981-2-22',1250,500,30),
(7566,'JONES','MANAGER',7839,'1981-4-2',2975,NULL,20),
(7654,'MARTIN','SALESMAN',7698,'1981-9-28',1250,1400,30),
(7698,'BLAKE','MANAGER',7839,'1981-5-1',2850,NULL,30),
(7782,'CLARK','MANAGER',7839,'1981-6-9',2450,NULL,10),
(7788,'SCOTT','ANALYST',7566,'1987-7-13',3000,NULL,20),
(7839,'KING','PRESIDENT',NULL,'1981-11-17',5000,NULL,10),
(7844,'TURNER','SALESMAN',7698,'1981-9-8',1500,0,30),
(7876,'ADAMS','CLERK',7788,'1987-7-13',1100,NULL,20),
(7900,'JAMES','CLERK',7698,'1981-12-3',950,NULL,30),
(7902,'FORD','ANALYST',7566,'1981-12-3',3000,NULL,20),
(7934,'MILLER','CLERK',7782,'1982-1-23',1300,NULL,10);

select * from booktest_emp;
