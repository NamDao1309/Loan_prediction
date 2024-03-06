-- Select film_id, title, rental_rate, length from sakila.film where length > 150 AND rental_rate = 2.99
-- Select film_id, title, length, rental_rate from sakila.film
-- Select concat(title,'_',release_year) title_release_year, length from sakila.film
-- Select * from sakila.category c;
-- select obj.category_id, obj.name, obj.last_update from sakila.category obj
-- Select a.title, b.film_id from sakila.film a, sakila.film_category b
-- Select * from sakila.film obj where obj.title = 'ANGELS LIFE'
-- Select * from sakila.film a where a.film_id = 30
-- Select * from sakila.film b where b.length > 100 AND rating ='G'
-- Select * from sakila.film c where c.title like 'A%E'
-- Select * from sakila.film d where d.title like 'AU%'
-- Select * from sakila.film e where e.title like '%E'
-- Select * from sakila.country where country like 'Vi%'
-- Select * from sakila.country where country like '%ba%'
-- Select * from sakila.country where country like 'VietNa_'
-- Select * from sakila.film where release_year=2006 and length >60
-- Select * from sakila.film where rating='G' or length>60 or rental_rate > 2.99
-- Select * from sakila.country where not country ='VietNam'
-- Select * from sakila.film limit 10 offset 20
-- Select min(length) from sakila.film
-- select max(length), min(rental_rate) from sakila.film
-- Select count(*) from sakila.film where rating='G'
-- Select Avg(length) from sakila.film where rating = 'G'
-- Select avg(rental_rate) from sakila.film where rating='PG'
-- Select sum(length) from sakila.film where rating='G'
-- Select sum(rental_rate) from sakila.film where rating='G'
-- Select * from sakila.film where original_language_id is null
-- Select * from sakila.film limit 10 offset 2
-- Select * from sakila.film where rating in ('R','PG-13','NC-17','A')


-- Create database Thuchanh
Use Thuchanh;
Create table DOCGIA(MaDG int Not null auto_increment,
					TenDG Text(30) Not Null,
					DiaChi text(50) Not Null,
                    Tuoi int,
                    primary key(MaDG));
alter table DOCGIA Add column GhiChu Text(50);
alter table DOCGIA modify column GhiChu longtext;
alter table DOCGIA DROP column GhiChu;

insert into DOCGIA VALUES('01','Nguyễn Công Thành','Lớp 41NC',22 );
INSERT INTO DOCGIA(MaDG, TenDG, DiaChi) VALUES('02','Nguyễn Phương Lan','Lớp 41NC');
DELETE FROM DOCGIA WHERE MaDG='01';
select * from thuchanh.docgia;
Use Thuchanh;
DELETE FROM thuchanh.docgia WHERE DiaChi like '%41NC';
UPDATE DOCGIA SET Diachi='CVK3I' WHERE MaDG='01';














