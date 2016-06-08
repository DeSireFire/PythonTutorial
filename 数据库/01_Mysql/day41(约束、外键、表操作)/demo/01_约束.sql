drop table  if exists student;
create table student( 
	sid int primary key auto_increment, 
	sname varchar(20) unique not null, 
	ssex char(1) not null, 
	sage int default 18, 
	sscore decimal(4,1), 
	sdate date,
	cid int,
  constraint fk_student_cid foreign key(cid) references class(id) on delete cascade
);

drop table  if exists student;
create table student( 
	sid int primary key auto_increment, 
	sname varchar(20) unique not null, 
	ssex bit not null
);
/*
alter table student
add constraint fk_student_cid foreign key(cid) references class(id);
*/

/*
���������
�ȴ����������ٴ��������
ɾ����ʱ����ɾ�������ɾ������
*/
drop table  if exists class;
create table class(
	id int primary key auto_increment, 
	sname varchar(20) unique
);


select * from student;
select * from class;


