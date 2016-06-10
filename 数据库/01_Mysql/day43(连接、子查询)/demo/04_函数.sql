mysql> select concat('a',1);
+---------------+
| concat('a',1) |
+---------------+
| a1            |
+---------------+
1 row in set

mysql> select concat('1
',1);
+---------------+
| concat('1',1) |
+---------------+
| 11            |
+---------------+
1 row in set

mysql> select concat('1','2','3
');
+---------------------+
| concat('1','2','3') |
+---------------------+
| 123                 |
+---------------------+
1 row in set

mysql> select * from EMP;
+-------+--------+-----------+------+------------+------+------+--------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO |
+-------+--------+-----------+------+------------+------+------+--------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |
+-------+--------+-----------+------+------------+------+------+--------+
14 rows in set

mysql> select empno,concat(ename,':',job) from EMP;
+-------+-----------------------+
| empno | concat(ename,':',job) |
+-------+-----------------------+
|  7369 | SMITH:CLERK           |
|  7499 | ALLEN:SALESMAN        |
|  7521 | WARD:SALESMAN         |
|  7566 | JONES:MANAGER         |
|  7654 | MARTIN:SALESMAN       |
|  7698 | BLAKE:MANAGER         |
|  7782 | CLARK:MANAGER         |
|  7788 | SCOTT:ANALYST         |
|  7839 | KING:PRESIDENT        |
|  7844 | TURNER:SALESMAN       |
|  7876 | ADAMS:CLERK           |
|  7900 | JAMES:CLERK           |
|  7902 | FORD:ANALYST          |
|  7934 | MILLER:CLERK          |
+-------+-----------------------+
14 rows in set

mysql> select empno,concat(ename,':',job) ret
 from EMP;
+-------+-----------------+
| empno | ret             |
+-------+-----------------+
|  7369 | SMITH:CLERK     |
|  7499 | ALLEN:SALESMAN  |
|  7521 | WARD:SALESMAN   |
|  7566 | JONES:MANAGER   |
|  7654 | MARTIN:SALESMAN |
|  7698 | BLAKE:MANAGER   |
|  7782 | CLARK:MANAGER   |
|  7788 | SCOTT:ANALYST   |
|  7839 | KING:PRESIDENT  |
|  7844 | TURNER:SALESMAN |
|  7876 | ADAMS:CLERK     |
|  7900 | JAMES:CLERK     |
|  7902 | FORD:ANALYST    |
|  7934 | MILLER:CLERK    |
+-------+-----------------+
14 rows in set

mysql> select length('哈哈a
');
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'select length('哈哈a
')' at line 3
mysql> select length('哈哈a');
+-----------------+
| length('哈哈a') |
+-----------------+
|               7 |
+-----------------+
1 row in set

mysql> desc s1;
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| sid   | int(11)     | NO   | PRI | NULL    | auto_increment |
| sname | varchar(20) | YES  |     | NULL    |                |
| cid   | int(11)     | YES  |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
3 rows in set

mysql> insert into s1(sname) values('老王老王老王老王老王老王');
Query OK, 1 row affected

mysql> select * from s1;
+-----+--------------------------+------+
| sid | sname                    | cid  |
+-----+--------------------------+------+
|   1 | 老王老王老王老王老王老王 | NULL |
+-----+--------------------------+------+
1 row in set

mysql> select length(sname) from s1;
+---------------+
| length(sname) |
+---------------+
|            36 |
+---------------+
1 row in set

mysql> select floor(3.2);
+------------+
| floor(3.2) |
+------------+
|          3 |
+------------+
1 row in set

mysql> select floor(-
3.2);
+-------------+
| floor(-3.2) |
+-------------+
|          -4 |
+-------------+
1 row in set

mysql> select floor(-3
);
+-----------+
| floor(-3) |
+-----------+
|        -3 |
+-----------+
1 row in set

mysql> create table c2(id int,birthday date);
Query OK, 0 rows affected

mysql> insert into c2 values(1,'2017-9-12');
Query OK, 1 row affected

mysql> select * from c2;
+----+------------+
| id | birthday   |
+----+------------+
|  1 | 2017-09-12 |
+----+------------+
1 row in set

mysql> create table c3(id int,birthday datetime
);
Query OK, 0 rows affected

mysql> insert into c3 values(1,'2017-9-12 15:12:50
');
Query OK, 1 row affected

mysql> select * from c3
;
+----+---------------------+
| id | birthday            |
+----+---------------------+
|  1 | 2017-09-12 15:12:50 |
+----+---------------------+
1 row in set

mysql> insert into c2 values(2
,'2017年9月12日');
1292 - Incorrect date value: '2017年9月12日' for column 'birthday' at row 1
1292 - Incorrect date value: '2017年9月12日' for column 'birthday' at row 1
    -> ；
    -> ;
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '1292 - Incorrect date value: '2017年9月12日' for column 'birthday' at row 1
' at line 1
mysql> insert into c2 values(2,'2017年9月12日');
1292 - Incorrect date value: '2017年9月12日' for column 'birthday' at row 1
mysql> insert into c2 values(2,str_to_date('2017年9月12日','
%Y年%m月%d日'));
Query OK, 1 row affected

mysql> select * from c2;
+----+------------+
| id | birthday   |
+----+------------+
|  1 | 2017-09-12 |
|  2 | 2017-09-12 |
+----+------------+
2 rows in set

mysql> select id,birthday from c2;
+----+------------+
| id | birthday   |
+----+------------+
|  1 | 2017-09-12 |
|  2 | 2017-09-12 |
+----+------------+
2 rows in set

mysql> select id,date_format(birthday,'%Y年%m月%d日
') from c2;
+----+--------------------------------------+
| id | date_format(birthday,'%Y年%m月%d日') |
+----+--------------------------------------+
|  1 | 2017年09月12日                       |
|  2 | 2017年09月12日                       |
+----+--------------------------------------+
2 rows in set

mysql> insert into c2 values('3','2017-9-13
');
Query OK, 1 row affected

mysql> /*数据库中，所有的都可以当做字符串自动解析*/;
Query OK, 0 rows affected

mysql> insert into c2 values('a
','2017-9-13');
1366 - Incorrect integer value: 'a' for column 'id' at row 1
1366 - Incorrect integer value: 'a
' for column 'id' at row 1
    -> ;
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '1366 - Incorrect integer value: 'a' for column 'id' at row 1' at line 1
mysql> 
