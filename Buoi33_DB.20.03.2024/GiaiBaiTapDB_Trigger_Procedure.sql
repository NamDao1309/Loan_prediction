create database hang_hoa;
use hang_hoa;

create table  mathang(
	mahang varchar(5) primary key,
    tenhang varchar(50) not null,
    soluong int
);

create table nhatkybanhang(
	stt int primary key,
    ngay datetime,
    nguoimua varchar(30),
    mahang varchar(5),
    soluong int,
    giaban int
);

-- insert du lieu vao
insert into mathang(mahang, tenhang, soluong) values('H1', 'Kem', 10);
insert into mathang(mahang, tenhang, soluong) values('H2', 'Sinh To Xoai', 20);
insert into mathang(mahang, tenhang, soluong) values('H3', 'Cafe nau Da', 30);
insert into mathang(mahang, tenhang, soluong) values('H4', 'Banh My', 40);

insert into nhatkybanhang(stt, ngay, nguoimua, mahang, soluong, giaban)
values(1, "2024:03:20 10:10:10", "Hoang Dao Thuy", 'H2', 15, 30000);

insert into nhatkybanhang(stt, ngay, nguoimua, mahang, soluong, giaban)
values(3, "2024:03:21 11:11:11", "Cao Ba Quat", 'H3', 17, 32000);

insert into nhatkybanhang(stt, ngay, nguoimua, mahang, soluong, giaban)
values(4, "2024:03:22 12:12:12", "Tran Thu Do", 'H5', 19, 45000);


-- cau 1:
delimiter $$

create trigger after_insert_nkbh
after insert on nhatkybanhang
for each row
begin
	update mathang
    set soluong = soluong - inserted.soluong
    where mahang = inserted.mahang;
end $$

delimiter ;	

-- bai 2
delimiter $$
drop procedure if exists CheckDiem $$
create procedure CheckDiem(
	in diem float,
    out xepLoai varchar(255)
)
begin
	if diem > 0 && diem < 5 then
		set xepLoai = 'Kem';
	elseif diem >= 5 && diem < 6 then
		set xepLoai = 'Trung Binh';
	elseif diem >= 6 && diem < 7 then
		set xepLoai = 'Trung Binh Kha';
	elseif diem >=7 && diem < 8 then
		set xepLoai = 'Kha';
	elseif diem >=8 && diem < 9 then
		set xepLoai = 'Gioi';
	else
		set xepLoai = 'Xuat Sac';
	end if;
    select xepLoai;
end $$
delimiter ;

call CheckDiem(9.5, @Loai);
select @Loai;

-- bai 3 
delimiter $$
drop procedure if exists CheckThuTrongTuan $$
create procedure CheckThuTrongTuan(
	IN so int,
    OUT thu varchar(255)
)
begin
	case so
		when 2 then
			set thu = 'Thu hai';
		when 3 then 
			set thu = 'Thu ba';
		when 4  then 
			set thu = 'Thu tu';
		when 5 then
			set thu = 'Thu nam';
		when 6 then
			set thu = 'Thu sau';
		when 7 then
			set thu = 'Thu bay';
		when 8 then
			set thu = 'Chu Nhat';
		else
			set thu = 'Khong phai la thu trong tuan';
	end case;
    select thu;
end $$
delimiter ;

call CheckThuTrongTuan(9, @result);
call CheckThuTrongTuan(7, @result);
call CheckThuTrongTuan(0, @result);
select @result;