alter user root@'%' identified with caching_sha2_password by rootpassword;
alter user projectmanager@'%' identified with caching_sha2_password by projectmanagerpassword;
grant all privileges on *.* to root@'%' with grant option;
grant all privileges on *.* to projectmanager@'%' with grant option;
flush privileges;
