mysql> select t1.empno,t1.ename,t2.ename
 from EMP t1,EMP t2 where t1.mgr = t2.empno;
+-------+--------+-------+
| empno | ename  | ename |
+-------+--------+-------+
|  7369 | SMITH  | FORD  |
|  7499 | ALLEN  | BLAKE |
|  7521 | WARD   | BLAKE |
|  7566 | JONES  | KING  |
|  7654 | MARTIN | BLAKE |
|  7698 | BLAKE  | KING  |
|  7782 | CLARK  | KING  |
|  7788 | SCOTT  | JONES |
|  7844 | TURNER | BLAKE |
|  7876 | ADAMS  | SCOTT |
|  7900 | JAMES  | BLAKE |
|  7902 | FORD   | JONES |
|  7934 | MILLER | CLARK |
+-------+--------+-------+
13 rows in set

mysql> select t1.empno,t1.ename,t2.ename from EMP t1 inner join EMP t2 on
 t1.mgr = t2.empno;
+-------+--------+-------+
| empno | ename  | ename |
+-------+--------+-------+
|  7369 | SMITH  | FORD  |
|  7499 | ALLEN  | BLAKE |
|  7521 | WARD   | BLAKE |
|  7566 | JONES  | KING  |
|  7654 | MARTIN | BLAKE |
|  7698 | BLAKE  | KING  |
|  7782 | CLARK  | KING  |
|  7788 | SCOTT  | JONES |
|  7844 | TURNER | BLAKE |
|  7876 | ADAMS  | SCOTT |
|  7900 | JAMES  | BLAKE |
|  7902 | FORD   | JONES |
|  7934 | MILLER | CLARK |
+-------+--------+-------+
13 rows in set

mysql> select t1.empno,t1.ename,t2.ename from EMP t1 left
 join EMP t2 on t1.mgr = t2.empno;
+-------+--------+-------+
| empno | ename  | ename |
+-------+--------+-------+
|  7369 | SMITH  | FORD  |
|  7499 | ALLEN  | BLAKE |
|  7521 | WARD   | BLAKE |
|  7566 | JONES  | KING  |
|  7654 | MARTIN | BLAKE |
|  7698 | BLAKE  | KING  |
|  7782 | CLARK  | KING  |
|  7788 | SCOTT  | JONES |
|  7839 | KING   | NULL  |
|  7844 | TURNER | BLAKE |
|  7876 | ADAMS  | SCOTT |
|  7900 | JAMES  | BLAKE |
|  7902 | FORD   | JONES |
|  7934 | MILLER | CLARK |
+-------+--------+-------+
14 rows in set

mysql> 
