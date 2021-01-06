create database dvs;

use dvds; 

create table dvds(
    serialNum int NOT NULL AUTO_INCREMENT,
    title varchar(250),
    director varchar(250),
    price int,
    PRIMARY KEY(serialNum)
    );

create table customer(
    serialNum int NOT NULL AUTO_INCREMENT,
    title varchar(250),
    name varchar(250),
    price int,
    PRIMARY KEY(serialNum)
    );

insert into dvds (title, director, price) values ('A Quiet Place', 'John Krasinski', 8.00)

insert into dvds (title, director, price) values ('The Hangover', 'Todd Phillips', 7.00)

insert into customer (title, name, price) values ('The Patriot', 'John Smith', 6.00);

insert into customer (title, name, price) values ('The Hangover', 'Sue Volany', 7.00);


update customer set title = 'Saving Private Ryan' where serialNum = 4; 

delete from customer where serialNum = 4; 