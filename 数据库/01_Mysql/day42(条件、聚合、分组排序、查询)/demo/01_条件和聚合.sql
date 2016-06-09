mysql> use laowang
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> select * from emp;
ERROR 1146 (42S02): Table 'laowang.emp' doesn't exist
mysql> notee
mysql> select * from EMP e where e.job in('CLERK','SALESMAN')
    -> ;
+-------+--------+----------+------+------------+---------+---------+--------+
| EMPNO | ENAME  | JOB      | MGR  | HIREDATE   | SAL     | COMM    | DEPTNO |
+-------+--------+----------+------+------------+---------+---------+--------+
|  7369 | SMITH  | CLERK    | 7902 | 1980-12-17 |  800.00 |    NULL |     20 |
|  7499 | ALLEN  | SALESMAN | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
|  7654 | MARTIN | SALESMAN | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
|  7844 | TURNER | SALESMAN | 7698 | 1981-09-08 | 1500.00 |    0.00 |     30 |
|  7876 | ADAMS  | CLERK    | 7788 | 1987-07-13 | 1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK    | 7698 | 1981-12-03 |  950.00 |    NULL |     30 |
|  7934 | MILLER | CLERK    | 7782 | 1982-01-23 | 1300.00 |    NULL |     10 |
+-------+--------+----------+------+------------+---------+---------+--------+
8 rows in set (0.00 sec)

mysql> select * from EMP e where e.sal between 800 and 1200;
+-------+-------+-------+------+------------+---------+------+--------+
| EMPNO | ENAME | JOB   | MGR  | HIREDATE   | SAL     | COMM | DEPTNO |
+-------+-------+-------+------+------------+---------+------+--------+
|  7369 | SMITH | CLERK | 7902 | 1980-12-17 |  800.00 | NULL |     20 |
|  7876 | ADAMS | CLERK | 7788 | 1987-07-13 | 1100.00 | NULL |     20 |
|  7900 | JAMES | CLERK | 7698 | 1981-12-03 |  950.00 | NULL |     30 |
+-------+-------+-------+------+------------+---------+------+--------+
3 rows in set (0.00 sec)

mysql> select * from EMP e where e.sal>=800 and e.sal<=1200;
+-------+-------+-------+------+------------+---------+------+--------+
| EMPNO | ENAME | JOB   | MGR  | HIREDATE   | SAL     | COMM | DEPTNO |
+-------+-------+-------+------+------------+---------+------+--------+
|  7369 | SMITH | CLERK | 7902 | 1980-12-17 |  800.00 | NULL |     20 |
|  7876 | ADAMS | CLERK | 7788 | 1987-07-13 | 1100.00 | NULL |     20 |
|  7900 | JAMES | CLERK | 7698 | 1981-12-03 |  950.00 | NULL |     30 |
+-------+-------+-------+------+------------+---------+------+--------+
3 rows in set (0.00 sec)

mysql> select * from EMP;
+-------+--------+-----------+------+------------+---------+---------+--------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL     | COMM    | DEPTNO |
+-------+--------+-----------+------+------------+---------+---------+--------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 |  800.00 |    NULL |     20 |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975.00 |    NULL |     20 |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850.00 |    NULL |     30 |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450.00 |    NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000.00 |    NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500.00 |    0.00 |     30 |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |  950.00 |    NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000.00 |    NULL |     20 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300.00 |    NULL |     10 |
+-------+--------+-----------+------+------------+---------+---------+--------+
14 rows in set (0.00 sec)

mysql> select * from EMP e where e.comm is not null;
+-------+--------+----------+------+------------+---------+---------+--------+
| EMPNO | ENAME  | JOB      | MGR  | HIREDATE   | SAL     | COMM    | DEPTNO |
+-------+--------+----------+------+------------+---------+---------+--------+
|  7499 | ALLEN  | SALESMAN | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
|  7654 | MARTIN | SALESMAN | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
|  7844 | TURNER | SALESMAN | 7698 | 1981-09-08 | 1500.00 |    0.00 |     30 |
+-------+--------+----------+------+------------+---------+---------+--------+
4 rows in set (0.01 sec)

mysql> select * from EMP e where e.comm is not null and e.comm!=0;
+-------+--------+----------+------+------------+---------+---------+--------+
| EMPNO | ENAME  | JOB      | MGR  | HIREDATE   | SAL     | COMM    | DEPTNO |
+-------+--------+----------+------+------------+---------+---------+--------+
|  7499 | ALLEN  | SALESMAN | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
|  7654 | MARTIN | SALESMAN | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
+-------+--------+----------+------+------------+---------+---------+--------+
3 rows in set (0.00 sec)

mysql> select max(sal),min(sal),avg(sal) from EMP 
    -> ;
+----------+----------+-------------+
| max(sal) | min(sal) | avg(sal)    |
+----------+----------+-------------+
|  5000.00 |   800.00 | 2073.214286 |
+----------+----------+-------------+
1 row in set (0.00 sec)

mysql> select max(sal),min(sal),avg(sal),count(*) from EMP
    -> ;
+----------+----------+-------------+----------+
| max(sal) | min(sal) | avg(sal)    | count(*) |
+----------+----------+-------------+----------+
|  5000.00 |   800.00 | 2073.214286 |       14 |
+----------+----------+-------------+----------+
1 row in set (0.00 sec)

mysql> 
mysql> select count(*),count(empno),count(comm) from EMP;
+----------+--------------+-------------+
| count(*) | count(empno) | count(comm) |
+----------+--------------+-------------+
|       14 |           14 |           4 |
+----------+--------------+-------------+
1 row in set (0.00 sec)

mysql> select * from EMP;
+-------+--------+-----------+------+------------+---------+---------+--------+
| EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL     | COMM    | DEPTNO |
+-------+--------+-----------+------+------------+---------+---------+--------+
|  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 |  800.00 |    NULL |     20 |
|  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
|  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
|  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975.00 |    NULL |     20 |
|  7654 | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
|  7698 | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850.00 |    NULL |     30 |
|  7782 | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450.00 |    NULL |     10 |
|  7788 | SCOTT  | ANALYST   | 7566 | 1987-07-13 | 3000.00 |    NULL |     20 |
|  7839 | KING   | PRESIDENT | NULL | 1981-11-17 | 5000.00 |    NULL |     10 |
|  7844 | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500.00 |    0.00 |     30 |
|  7876 | ADAMS  | CLERK     | 7788 | 1987-07-13 | 1100.00 |    NULL |     20 |
|  7900 | JAMES  | CLERK     | 7698 | 1981-12-03 |  950.00 |    NULL |     30 |
|  7902 | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000.00 |    NULL |     20 |
|  7934 | MILLER | CLERK     | 7782 | 1982-01-23 | 1300.00 |    NULL |     10 |
+-------+--------+-----------+------+------------+---------+---------+--------+
14 rows in set (0.00 sec)

mysql> select sum(sal+comm) from EMP;
+---------------+
| sum(sal+comm) |
+---------------+
|       7800.00 |
+---------------+
1 row in set (0.00 sec)

mysql> select sum(sal) from EMP;
+----------+
| sum(sal) |
+----------+
| 29025.00 |
+----------+
1 row in set (0.00 sec)

mysql> select sal,comm,sal+comm from EMP;
+---------+---------+----------+
| sal     | comm    | sal+comm |
+---------+---------+----------+
|  800.00 |    NULL |     NULL |
| 1600.00 |  300.00 |  1900.00 |
| 1250.00 |  500.00 |  1750.00 |
| 2975.00 |    NULL |     NULL |
| 1250.00 | 1400.00 |  2650.00 |
| 2850.00 |    NULL |     NULL |
| 2450.00 |    NULL |     NULL |
| 3000.00 |    NULL |     NULL |
| 5000.00 |    NULL |     NULL |
| 1500.00 |    0.00 |  1500.00 |
| 1100.00 |    NULL |     NULL |
|  950.00 |    NULL |     NULL |
| 3000.00 |    NULL |     NULL |
| 1300.00 |    NULL |     NULL |
+---------+---------+----------+
14 rows in set (0.00 sec)

mysql> select ifnull(comm,0) from EMP:
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ':' at line 1
mysql> select ifnull(comm,0) from EMP;
+----------------+
| ifnull(comm,0) |
+----------------+
|           0.00 |
|         300.00 |
|         500.00 |
|           0.00 |
|        1400.00 |
|           0.00 |
|           0.00 |
|           0.00 |
|           0.00 |
|           0.00 |
|           0.00 |
|           0.00 |
|           0.00 |
|           0.00 |
+----------------+
14 rows in set (0.00 sec)

mysql> select sal,comm,sal+ifnull(comm,0) from EMP;
+---------+---------+--------------------+
| sal     | comm    | sal+ifnull(comm,0) |
+---------+---------+--------------------+
|  800.00 |    NULL |             800.00 |
| 1600.00 |  300.00 |            1900.00 |
| 1250.00 |  500.00 |            1750.00 |
| 2975.00 |    NULL |            2975.00 |
| 1250.00 | 1400.00 |            2650.00 |
| 2850.00 |    NULL |            2850.00 |
| 2450.00 |    NULL |            2450.00 |
| 3000.00 |    NULL |            3000.00 |
| 5000.00 |    NULL |            5000.00 |
| 1500.00 |    0.00 |            1500.00 |
| 1100.00 |    NULL |            1100.00 |
|  950.00 |    NULL |             950.00 |
| 3000.00 |    NULL |            3000.00 |
| 1300.00 |    NULL |            1300.00 |
+---------+---------+--------------------+
14 rows in set (0.00 sec)

mysql> select sal,comm,sal+ifnull(comm,0),sum(sal+comm) from EMP;
ERROR 1140 (42000): In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'laowang.EMP.SAL'; this is incompatible with sql_mode=only_full_group_by
mysql> select sum(sal+comm) from EMP;
+---------------+
| sum(sal+comm) |
+---------------+
|       7800.00 |
+---------------+
1 row in set (0.00 sec)

mysql> select sum(sal) from EMP;
+----------+
| sum(sal) |
+----------+
| 29025.00 |
+----------+
1 row in set (0.00 sec)

mysql> select sum(sal+ifnull(comm,0)) from EMP;
+-------------------------+
| sum(sal+ifnull(comm,0)) |
+-------------------------+
|                31225.00 |
+-------------------------+
1 row in set (0.00 sec)

mysql> notee
