mysql> create table bankuser(id int,money int);
Query OK, 0 rows affected
mysql> drop table bankuser;
Query OK, 0 rows affected
mysql> create table bankuser(id int,name varchar(20
),money int);
Query OK, 0 rows affected
1050 - Table 'bankuser' already exists
    -> ;
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'Query OK, 0 rows affected' at line 1
mysql> desc bankuser;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
| money | int(11)     | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set

mysql> insert into bankuser values(1,'刘德华',1000);
Query OK, 1 row affected
mysql> insert into bankuser values(1,'马德华',1
);
Query OK, 1 row affected
Query OK, 1 row affected
    -> ;
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'Query OK, 1 row affected' at line 1
mysql> select * from bankuser;
+----+--------+-------+
| id | name   | money |
+----+--------+-------+
|  1 | 刘德华 |  1000 |
|  1 | 马德华 |     1 |
|  1 | 马德华 |     1 |
+----+--------+-------+
3 rows in set

mysql> delete from bankuser where id=1;
Query OK, 3 rows affected
mysql> insert into bankuser values(1,'刘德华',1000);
Query OK, 1 row affected
mysql> insert into bankuser values(2,'马德华',1
);
Query OK, 1 row affected
Query OK, 1 row affected
    -> ;
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'Query OK, 1 row affected' at line 1
mysql> select * from bankuser;
+----+--------+-------+
| id | name   | money |
+----+--------+-------+
|  1 | 刘德华 |  1000 |
|  2 | 马德华 |     1 |
|  2 | 马德华 |     1 |
+----+--------+-------+
3 rows in set

mysql> delete from bankuser where id=2;
Query OK, 2 rows affected
mysql> insert into bankuser values(2,'马德华',1);
Query OK, 1 row affected
mysql> select * from bankuser;
+----+--------+-------+
| id | name   | money |
+----+--------+-------+
|  1 | 刘德华 |  1000 |
|  2 | 马德华 |     1 |
+----+--------+-------+
2 rows in set

mysql> begin
    -> ;
Query OK, 0 rows affected

mysql> update bankuser set money = money-100 where id=1;
Query OK, 1 row affected
Rows matched: 1  Changed: 1  Warnings: 0
mysql> update bankuser set money = money+100 where id=2;
Query OK, 1 row affected
Rows matched: 1  Changed: 1  Warnings: 0
mysql> select * from bankuser;
+----+--------+-------+
| id | name   | money |
+----+--------+-------+
|  1 | 刘德华 |   900 |
|  2 | 马德华 |   101 |
+----+--------+-------+
2 rows in set

mysql> rollback;
Query OK, 0 rows affected

mysql> select * from bankuser;
+----+--------+-------+
| id | name   | money |
+----+--------+-------+
|  1 | 刘德华 |  1000 |
|  2 | 马德华 |     1 |
+----+--------+-------+
2 rows in set

mysql> update bankuser set money = money-100 where id=1;
Query OK, 1 row affected
Rows matched: 1  Changed: 1  Warnings: 0
mysql> update bankuser set money = money+100 where id=2;
Query OK, 1 row affected
Rows matched: 1  Changed: 1  Warnings: 0
mysql> select * from bankuser;
+----+--------+-------+
| id | name   | money |
+----+--------+-------+
|  1 | 刘德华 |   900 |
|  2 | 马德华 |   101 |
+----+--------+-------+
2 rows in set

mysql> commit;
Query OK, 0 rows affected

mysql> select * from bankuser;
+----+--------+-------+
| id | name   | money |
+----+--------+-------+
|  1 | 刘德华 |   900 |
|  2 | 马德华 |   101 |
+----+--------+-------+
2 rows in set

mysql> rollback;
Query OK, 0 rows affected

mysql> select * from bankuser;
+----+--------+-------+
| id | name   | money |
+----+--------+-------+
|  1 | 刘德华 |   900 |
|  2 | 马德华 |   101 |
+----+--------+-------+
2 rows in set

mysql> begin;
Query OK, 0 rows affected

mysql> commit;
Query OK, 0 rows affected

mysql> rollback;
Query OK, 0 rows affected

mysql> begin;
Query OK, 0 rows affected

mysql> select * from bankuser;
