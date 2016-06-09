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

mysql> select * from DEPT;
+--------+------------+----------+
| DEPTNO | DNAME      | LOC      |
+--------+------------+----------+
|     10 | ACCOUNTING | NEW YORK |
|     20 | RESEARCH   | DALLAS   |
|     30 | SALES      | CHICAGO  |
|     40 | OPERATIONS | BOSTON   |
+--------+------------+----------+
4 rows in set

mysql> select * from EMP,DEPT;
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     10 | ACCOUNTING | NEW YORK |
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     30 | SALES      | CHICAGO  |
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     40 | OPERATIONS | BOSTON   |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     10 | ACCOUNTING | NEW YORK |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     20 | RESEARCH   | DALLAS   |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     40 | OPERATIONS | BOSTON   |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     10 | ACCOUNTING | NEW YORK |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     20 | RESEARCH   | DALLAS   |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     40 | OPERATIONS | BOSTON   |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     10 | ACCOUNTING | NEW YORK |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     30 | SALES      | CHICAGO  |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     40 | OPERATIONS | BOSTON   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     10 | ACCOUNTING | NEW YORK |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     20 | RESEARCH   | DALLAS   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     40 | OPERATIONS | BOSTON   |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     10 | ACCOUNTING | NEW YORK |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     20 | RESEARCH   | DALLAS   |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     40 | OPERATIONS | BOSTON   |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     20 | RESEARCH   | DALLAS   |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     30 | SALES      | CHICAGO  |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     40 | OPERATIONS | BOSTON   |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     10 | ACCOUNTING | NEW YORK |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     30 | SALES      | CHICAGO  |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     40 | OPERATIONS | BOSTON   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     20 | RESEARCH   | DALLAS   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     30 | SALES      | CHICAGO  |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     40 | OPERATIONS | BOSTON   |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     10 | ACCOUNTING | NEW YORK |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     20 | RESEARCH   | DALLAS   |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     40 | OPERATIONS | BOSTON   |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     10 | ACCOUNTING | NEW YORK |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     30 | SALES      | CHICAGO  |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     40 | OPERATIONS | BOSTON   |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     10 | ACCOUNTING | NEW YORK |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     20 | RESEARCH   | DALLAS   |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     40 | OPERATIONS | BOSTON   |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     10 | ACCOUNTING | NEW YORK |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     30 | SALES      | CHICAGO  |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     40 | OPERATIONS | BOSTON   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     20 | RESEARCH   | DALLAS   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     30 | SALES      | CHICAGO  |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     40 | OPERATIONS | BOSTON   |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
56 rows in set

mysql> select * from EMP e,DEPT d where e.deptno = d.deptno;
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
14 rows in set

mysql> select * from student t1,subject t2,score t3 where t3.stuid = t1.id and t3.subid = t2.id;
1146 - Table 'laowang.subject' doesn't exist
mysql> tee sql_02.sql
    -> ;
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'tee sql_02.sql' at line 1
mysql> tee xx
    -> ;
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'tee xx' at line 1
mysql> select * from EMP e,DEPT d where e.deptno = d.deptno;
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
14 rows in set

mysql> select * from EMP e inner join DEPT d where e.deptno = d.deptno;
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
14 rows in set

mysql> select * from EMP e inner join DEPT d on
 e.deptno = d.deptno;
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
14 rows in set

mysql> select * from EMP e inner join DEPT d on e.deptno = d.deptno where sal >1000;
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
12 rows in set

mysql> select * from score t1 
inner join student t2 
on t1.stuid = t2.id
inner join subject t3
on t1.subid = t3.id;
1146 - Table 'laowang.score' doesn't exist
mysql> select * from EMP e right outer join DEPT d on e.deptno = d.deptno;
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
| NULL  | NULL   | NULL      | NULL | NULL       | NULL | NULL | NULL   |     40 | OPERATIONS | BOSTON   |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
15 rows in set

mysql> insert into EMP(EMPNO,DEPTNO) values(1111111,null);
Query OK, 1 row affected

mysql> select * from EMP e left
 outer join DEPT d on e.deptno = d.deptno;
+---------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO   | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+---------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|    7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|    7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|    7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|    7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|    7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|    7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|    7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|    7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|    7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|    7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|    7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|    7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|    7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|    7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     30 | SALES      | CHICAGO  |
| 1111111 | NULL   | NULL      | NULL | NULL       | NULL | NULL | NULL   | NULL   | NULL       | NULL     |
+---------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
15 rows in set

mysql> delete from EMP where empno = 1111111;
Query OK, 1 row affected

mysql> select * from EMP e right
 join DEPT d on e.deptno = d.deptno;
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
| NULL  | NULL   | NULL      | NULL | NULL       | NULL | NULL | NULL   |     40 | OPERATIONS | BOSTON   |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
15 rows in set

mysql> /*员工的编号，员工的姓名，员工的部门的编号，员工的部门的名字*/
    -> select * from EMP e,DEPT d where e.deptno = d.deptno;
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
14 rows in set

mysql> select * from EMP e,DEPT d where e.deptno = d.deptno;
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL  | COMM | DEPTNO | DEPTNO | DNAME      | LOC      |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 | 800  | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600 | 300  |     30 |     30 | SALES      | CHICAGO  |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250 | 500  |     30 |     30 | SALES      | CHICAGO  |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250 | 1400 |     30 |     30 | SALES      | CHICAGO  |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850 | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500 | 0    |     30 |     30 | SALES      | CHICAGO  |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 | 950  | NULL |     30 |     30 | SALES      | CHICAGO  |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000 | NULL |     20 |     20 | RESEARCH   | DALLAS   |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300 | NULL |     10 |     10 | ACCOUNTING | NEW YORK |
+-------+--------+-----------+------+------------+------+------+--------+--------+------------+----------+
14 rows in set

mysql> select 
deptno from EMP e,DEPT d where e.deptno = d.deptno;
1052 - Column 'deptno' in field list is ambiguous
1052 - Column 'deptno' in field list is ambiguous
    -> select e.
deptno from EMP e,DEPT d where e.deptno = d.deptno;
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '1052 - Column 'deptno' in field list is ambiguous

select e.deptno from EMP e' at line 1
mysql> select e.deptno from EMP e,DEPT d where e.deptno =
 d.deptno;
+--------+
| deptno |
+--------+
|     20 |
|     30 |
|     30 |
|     20 |
|     30 |
|     30 |
|     10 |
|     20 |
|     10 |
|     30 |
|     20 |
|     30 |
|     20 |
|     10 |
+--------+
14 rows in set

mysql> select e.empno,e.ename,e.deptno,d.dname
 from EMP e,DEPT d where e.deptno = d.deptno;
+-------+--------+--------+------------+
| empno | ename  | deptno | dname      |
+-------+--------+--------+------------+
|  7369 | SMITH  |     20 | RESEARCH   |
|  7499 | ALLEN  |     30 | SALES      |
|  7521 | WARD   |     30 | SALES      |
|  7566 | JONES  |     20 | RESEARCH   |
|  7654 | MARTIN |     30 | SALES      |
|  7698 | BLAKE  |     30 | SALES      |
|  7782 | CLARK  |     10 | ACCOUNTING |
|  7788 | SCOTT  |     20 | RESEARCH   |
|  7839 | KING   |     10 | ACCOUNTING |
|  7844 | TURNER |     30 | SALES      |
|  7876 | ADAMS  |     20 | RESEARCH   |
|  7900 | JAMES  |     30 | SALES      |
|  7902 | FORD   |     20 | RESEARCH   |
|  7934 | MILLER |     10 | ACCOUNTING |
+-------+--------+--------+------------+
14 rows in set

mysql> 1、求各个部门的员工工资大于1000的人数，部门的编号
    -> ；
    -> ;
1064 - You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '1、求各个部门的员工工资大于1000的人数，部门的编号

；' at line 1
mysql> /*1、求各个部门的员工工资大于1000的人数，部门的编号*/;
Query OK, 0 rows affected

mysql> select count(*),deptno
from EMP e
where e.sal>1000
group by e.deptno;
+----------+--------+
| count(*) | deptno |
+----------+--------+
|        3 |     10 |
|        4 |     20 |
|        5 |     30 |
+----------+--------+
3 rows in set

mysql> /*2、将1的结果作为一个表与DEPT外连接，DEPT为主表子查询*/;
Query OK, 0 rows affected

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

mysql> /*求每个员工编号，名字，工资，工资等级*/;
Query OK, 0 rows affected

mysql> select e.empno,e.ename,e.sal,s.grade
from EMP e,SALGRADE s
where e.sal between s.losal and s.hisal;
+-------+--------+------+-------+
| empno | ename  | sal  | grade |
+-------+--------+------+-------+
|  7369 | SMITH  | 800  |     1 |
|  7499 | ALLEN  | 1600 |     3 |
|  7521 | WARD   | 1250 |     2 |
|  7566 | JONES  | 2975 |     4 |
|  7654 | MARTIN | 1250 |     2 |
|  7698 | BLAKE  | 2850 |     4 |
|  7782 | CLARK  | 2450 |     4 |
|  7788 | SCOTT  | 3000 |     4 |
|  7839 | KING   | 5000 |     5 |
|  7844 | TURNER | 1500 |     3 |
|  7876 | ADAMS  | 1100 |     1 |
|  7900 | JAMES  | 950  |     1 |
|  7902 | FORD   | 3000 |     4 |
|  7934 | MILLER | 1300 |     2 |
+-------+--------+------+-------+
14 rows in set

mysql> 
