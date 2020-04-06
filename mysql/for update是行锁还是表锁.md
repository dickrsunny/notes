- 例如
  ~~~sql
  select t where a='...' for udpate
  ~~~
  mysql进行row lock还是table lock只取决于是否能使用索引，能则为行锁，否则为表锁；未查到数据则无锁。