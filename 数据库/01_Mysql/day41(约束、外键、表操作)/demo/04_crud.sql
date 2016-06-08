
create table s2( 
	sid int primary key auto_increment, 
	sname varchar(20) unique not null, 
	ssex char(1) not null, 
	sage int default 18, 
	sscore decimal(4,1), 
	sdate date,
	isdelete bit
);

create table s3( 
	sid varchar(36) primary key, 
	sname varchar(20) unique not null, 
	ssex char(1) not null, 
	sage int default 18, 
	sscore decimal(4,1), 
	sdate date
);
select * from s2;
select * from s3;
select sid,sname,ssex,sage,sscore,sdate from s2 where isdelete = 1;

select t.sid,t.sname 名字 
from s2 t
where t.isdelete = 1;

insert into s2(sname,ssex,sage,sscore,sdate) values('老王','1',18,1,'1999-10-2');

insert into s3 values(uuid(),'老王2','1',18,1,'1999-10-2');

insert into s2(sname,ssex,sdate) values('老王4','1','1999-10-2');

insert into s2(sname,ssex,sage,sscore,sdate) values
('a','1',18,1,'1999-10-2'),
('b','1',18,1,'1999-10-2'),
('c','1',18,1,'1999-10-2');

UPDATE s2
SET ssex = '0';

update s2
set sname = '老2王',ssex='1',sscore=2.256
where sid=2;

delete from s2
where sid>8;

update s2
set isdelete = 0
where sname like '老王%';

alter table s2 add isdelete bit default 1;




