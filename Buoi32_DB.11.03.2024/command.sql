CREATE DATABASE demo;
USE demo;

create table accounts (
	id  int(10) NOT NULL AUTO_INCREMENT, 	
	username varchar(120) NOT NULL,			
	email varchar(220) NOT NULL,
	country varchar(120),
	PRIMARY KEY (id)
);

create table books (
	id int(10) NOT NULL AUTO_INCREMENT, 	
	tensach varchar(120) NOT NULL,			
	soluong int(10) NOT NULL,
	namxb int(4) NOT NULL,
    nhaxb varchar(30) NOT NULL,
	PRIMARY KEY (id)
);

insert into users(username,email, country) 
values("Hoang Dao Thuy", "thuyhd@gmail.com", "Viet Nam");

insert into users(username,email, country) 
values("Thomas Tom", "tomTH@gmail.com", "American");
insert into users(username,email, country) 
values("Le Trong Tan", "tan@gmail.com", "Viet Nam");

select * from users;

drop table accounts;

delete from accounts where id = 3;

delete from accounts where country = 'Viet Nam';

-- doi ten bang
alter table accounts rename to users;

truncate table users;

-- them cot
alter table users add phone varchar(255);

-- doi ten cot
alter table users change phone mobilephone varchar(255);

select * from users;

-- xoa chot
alter table users drop mobilephone;








-- drop column
alter table accounts drop mobilePhone;

-- order by
select * from accounts order by username desc;
select * from accounts order by id asc;

-- group by
select country from accounts
where length(country) > 3
group by username;


-- inner join
create table courses(
	id_course int(10) auto_increment,
    course_name varchar(150) not null,
    money double not null,
    time_start varchar(20) not null,
    time_finish varchar(20) not null,
    id_student int(10) not null,
    primary key(id_course)
);

create table students(
	id_student int(10),
    full_name varchar(255) not null,
    student_code varchar(255) not null,
    course_th int(10),
    major varchar(20) not null,
    address varchar(255),
    primary key(id_student)
);

insert into courses(course_name, money, time_start, time_finish, id_student) 
values("Java", 3000000, "21/02", "21/04", 23);

insert into courses(course_name, money, time_start, time_finish, id_student) 
values("PHP", 4500000, "20/01", "20/05", 26);

insert into courses(course_name, money, time_start, time_finish, id_student) 
values("Python", 2700000, "19/03", "23/08", 27);

insert into courses(course_name, money, time_start, time_finish, id_student) 
values("Java", 4900000, "12/09", "23/12", 27);

insert into students(id_student, full_name, student_code, 
course_th, major, address) 
values(23, "Hoang Dao Thuy", "JAVA001", 122, "CNTT", "Ha Noi");

insert into students(id_student, full_name, student_code, 
course_th, major, address) 
values(26, "Cao Ba Quat", "PHP001", 127, "KHMT", "Ha Tay");

insert into students(id_student, full_name, student_code, 
course_th, major, address) 
values(30, "Le Trong Tan", "PYTHON01", 301, "KTMT", "Ha Dong");

-- inner join
select 
	s.id_student,
	s.full_name,
    c.course_name
from students s
inner join courses c
on s.id_student = c.id_student;

-- left join
select 
	s.id_student,
	s.full_name,
    c.course_name
from students s
left join courses c
on s.id_student = c.id_student;

-- right join
select 
	s.id_student,
	s.full_name,
    c.course_name
from students s
right join courses c
on s.id_student = c.id_student;

-- order by
select * from courses order by money desc;
select * from courses order by id_student asc;

select * from courses;

select count(*) from courses
group by course_name;

-- VIEWS 
use demo;
create table customers( customerNumber int(10) not null auto_increment,
						customerName varchar(255),
                        contactLastName varchar(255),
                        contactFirstName varchar(255),
                        phone varchar(13),
                        addressLine1 varchar(255),
                        addressLine2 varchar(255),
                        city varchar(15),
                        state varchar(255),
                        postalCode int(10),
                        country varchar(20),
                        salesRepEmployeeNumber int(10),
                        creditLimit double,
                        primary key(customerNumber));
                        
create table payments(customerNumber int(10) not null,
						checkNumber int(10),
                        paymentDate datetime,
                        amount double,
                        primary key(customerNumber));
                        
                        
                        
insert into customers( customerName, contactLastName, contactFirstName,
                        phone, addressLine1, addressLine2, city, state,
                postalCode, country, salesRepEmployeeNumber, creditLimit) 
values("Tran Quoc Tuan", "Tran Quoc", "Tuan", "098653231", "Ha Noi 1",
		"Ha Noi 02", "Dong Bac Bo", NULL ,100000, "Viet Nam", 2123, 400000.0);
        
insert into customers( customerName, contactLastName, contactFirstName,
                        phone, addressLine1, addressLine2, city, state,
                postalCode, country, salesRepEmployeeNumber, creditLimit) 
values("Le Binh Kiem", "Le Binh", "Khiem", "0986532656", "Ha Noi 3",
		"Ha Noi 04", "Dong Bac Bo",NULL, 101000, "Thai Lan", 2126, 4100000);
        
insert into customers( customerName, contactLastName, contactFirstName,
                        phone, addressLine1, addressLine2, city, state,
                postalCode, country, salesRepEmployeeNumber, creditLimit) 
values("Hoang Dao Thuy", "Hoang Dao", "Thuy", "098653788", "Ha Noi 5",
		"Ha Noi 06", "Tay Bac Bo", NULL,  104000, "CamPuchia", 2176, 4700000);


insert into payments(customerNumber, checkNumber, paymentDate, amount)
values(2, 334, "2024:12:10 13:13:13", 5600000);

insert into payments(customerNumber, checkNumber, paymentDate, amount)
values(3, 676, "2024:10:10 10:10:10", 6900000);

insert into payments(customerNumber, checkNumber, paymentDate, amount)
values(4, 334, "2024:09:10 12:12:12", 4500000);