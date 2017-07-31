drop table if exists audiences cascade; 
drop table if exists buildings cascade;
drop table if exists performances cascade;
drop table if exists reservation cascade;

create table performances(
perform_id varchar(10) primary key,
name   varchar(40),
type   varchar(15),
price  int(10),
booked int(3));

create table buildings(
bldg_id   varchar(10) primary key,
name      varchar(40),
location  varchar(30),
capacity  int(10),
perform_id  varchar(10),
constraint fk foreign key(perform_id) references performances(perform_id));

create table audiences(
aud_id varchar(10) primary key,
name   varchar(30),
gender varchar(4),
age	   int(9));

create table reservation(
aud_id     varchar(10),
perform_id varchar(10),
seat_num   int(15));


insert into performances values("1", "Coldplay Concert", "Concert", 100000, 3);
insert into performances values("2", "Jekyll & Hyde", "Musical", 70000, 2);


insert into buildings values("1", "Seoul Arts Center", "Seoul", 5, "1");
insert into buildings values("2", "Grand Peace Palace", "Seoul", 3, "1");


insert into audiences values("1", "Park Junghyuk", "M", 15);
insert into audiences values("2", "Kim Taeuk", "F", 30);
insert into audiences values("3", "Choi Jihun", "M", 56);


select * from buildings;
