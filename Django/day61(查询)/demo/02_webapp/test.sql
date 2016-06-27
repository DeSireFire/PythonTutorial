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
