/*外键设置方法1*/
drop table  if exists s1;
create table s1(
	sid int primary key auto_increment, 
	sname varchar(20),
  cid int,
  constraint fk_s1_cid foreign key(cid) references c1(cid)
);

drop table  if exists c1;
create table c1(
	cid int primary key auto_increment, 
	cname varchar(20)
);

/*外键设置方法2  推荐使用*/
drop table  if exists s1;
create table s1(
	sid int primary key auto_increment, 
	sname varchar(20),
  cid int,
  foreign key(cid) references c1(cid)
);

drop table  if exists c1;
create table c1(
	cid int primary key auto_increment, 
	cname varchar(20)
);

/*外键设置方法3*/
drop table  if exists s1;
create table s1(
	sid int primary key auto_increment, 
	sname varchar(20),
  cid int
);
alter table s1
add constraint fk_s1_cid 
foreign key (cid) references c1(cid);



drop table  if exists c1;
create table c1(
	cid int primary key auto_increment, 
	cname varchar(20)
);




desc c1;
desc s1;