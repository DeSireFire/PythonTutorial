mysql> select e.ename,d.dname
 from EMP  e inner join DEPT d on e.deptno = d.deptno;
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'select e.ename,d.dname
 from EMP  e inner join DEPT d on e.deptno = d.deptno' at line 3
mysql> select e.ename,d.dname from EMP  e inner join DEPT d on e.deptno = d.deptno;
+--------+------------+
| ename  | dname      |
+--------+------------+
| SMITH  | RESEARCH   |
| ALLEN  | SALES      |
| WARD   | SALES      |
| JONES  | RESEARCH   |
| MARTIN | SALES      |
| BLAKE  | SALES      |
| CLARK  | ACCOUNTING |
| SCOTT  | RESEARCH   |
| KING   | ACCOUNTING |
| TURNER | SALES      |
| ADAMS  | RESEARCH   |
| JAMES  | SALES      |
| FORD   | RESEARCH   |
| MILLER | ACCOUNTING |
+--------+------------+
14 rows in set

mysql> create view myview1 as select e.ename,d.dname from EMP  e inner join DEPT d on e.deptno = d.deptno;
Query OK, 0 rows affected

mysql> select * from myview1
    -> ;
+--------+------------+
| ename  | dname      |
+--------+------------+
| SMITH  | RESEARCH   |
| ALLEN  | SALES      |
| WARD   | SALES      |
| JONES  | RESEARCH   |
| MARTIN | SALES      |
| BLAKE  | SALES      |
| CLARK  | ACCOUNTING |
| SCOTT  | RESEARCH   |
| KING   | ACCOUNTING |
| TURNER | SALES      |
| ADAMS  | RESEARCH   |
| JAMES  | SALES      |
| FORD   | RESEARCH   |
| MILLER | ACCOUNTING |
+--------+------------+
14 rows in set

mysql> select * from c2;
+----+------------+
| id | birthday   |
+----+------------+
|  1 | 2017-09-12 |
|  2 | 2017-09-12 |
|  3 | 2017-09-13 |
+----+------------+
3 rows in set

mysql> create view v2 as
 select * from c2; 
Query OK, 0 rows affected

mysql> delete from  c2 where id=3;
Query OK, 1 row affected

mysql> select * from v2;
+----+------------+
| id | birthday   |
+----+------------+
|  1 | 2017-09-12 |
|  2 | 2017-09-12 |
+----+------------+
2 rows in set

mysql> 
