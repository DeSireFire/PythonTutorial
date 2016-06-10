mysql> use jiangxueqin;
Database changed
mysql> use laowang;
Database changed
mysql> select ifnull(t1.num,0),t2.dname
from (
	select count(*) num,deptno
	from EMP e
	where e.sal>1000
	group by e.deptno
) t1
right outer join DEPT t2
on t1.deptno = t2.deptno;
+------------------+------------+
| ifnull(t1.num,0) | dname      |
+------------------+------------+
|                3 | ACCOUNTING |
|                4 | RESEARCH   |
|                5 | SALES      |
|                0 | OPERATIONS |
+------------------+------------+
4 rows in set

mysql> select count(*) num,deptno
	from EMP e
	where e.sal>1000
	group by e.deptno;
+-----+--------+
| num | deptno |
+-----+--------+
|   3 |     10 |
|   4 |     20 |
|   5 |     30 |
+-----+--------+
3 rows in set

mysql> /*最高的工资的人的信息*/;
Query OK, 0 rows affected

mysql> select max(sal) from EMP;
+----------+
| max(sal) |
+----------+
| 5000     |
+----------+
1 row in set

mysql> select * from EMP where sal  = (select max(sal) from EMP);
+-------+-------+-----------+------+------------+------+------+--------+
| EMPNO | ENAME | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO |
+-------+-------+-----------+------+------------+------+------+--------+
|  7839 | KING  | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |
+-------+-------+-----------+------+------------+------+------+--------+
1 row in set

mysql> /*最高的工资的人的信息*/;
