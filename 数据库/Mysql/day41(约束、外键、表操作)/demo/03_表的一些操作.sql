create table dog(
	did int primary key auto_increment, 
	dname varchar(20)
);

desc dog;

rename table cat to dog;

show tables;

show create table cat;

alter table dog add dage int;

alter table dog drop dage int;

alter table dog modify dage varchar(20);