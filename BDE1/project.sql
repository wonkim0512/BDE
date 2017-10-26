drop table if exists reservation cascade;
drop table if exists audiences cascade; 
drop table if exists performances cascade;
drop table if exists buildings cascade;


create table buildings(
bldg_id   int(10) primary key auto_increment,
name      varchar(40),
location  varchar(30),
capacity  int(10),
assigned  int(10) default 0);

create table performances(
perform_id int(10) primary key auto_increment,
name   varchar(40),
type   varchar(15),
price  int(10),
booked int(3) default 0,
bldg_id int(10),
constraint performances_fk foreign key(bldg_id) references buildings(bldg_id) on delete cascade);

create table audiences(
aud_id int(10) primary key auto_increment,
name   varchar(30),
gender varchar(4),
age	   int(9),
perform_id int(10),
constraint audiences_fk foreign key(perform_id) references performances(perform_id) on delete cascade);

create table reservation(
aud_id     int(10),
perform_id int(10),
seat_num   int(15),
constraint reservation_fk1 foreign key(aud_id) references audiences(aud_id) on delete cascade,
constraint reservation_fk2 foreign key(perform_id) references performances(perform_id) on delete cascade);


insert into performances(name,type,price) values("Coldplay Concert", "Concert", 100000);
insert into performances(name,type,price) values("Jekyll & Hyde", "Musical", 70000);


insert into buildings(name,location,capacity) values("Seoul Arts Center", "Seoul", 5);
insert into buildings(name,location,capacity) values("Grand Peace Palace", "Seoul", 3);


insert into audiences(name,gender,age) values("Park Junghyuk", "M", 15);
insert into audiences(name,gender,age) values("Kim Taeuk", "F", 30);
insert into audiences(name,gender,age) values("Choi Jihun", "M", 56);


select * from buildings;
select * from audiences;
select * from performances;

select * from buildings join performances using(bldg_id);
select capacity from buildings;

select * from performances where perform_id = 1;
select * from performances where perform_id = 3;
select * from reservation;
select * from reservation natural join audiences where perform_id =1;
select * from audiences;
