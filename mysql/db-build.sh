# Create user
create user 'dev'@'%' identified by 'dev@123'; # CREATE USER 'new_user'@'%' IDENTIFIED BY 'password'; ..'@'%' specifies that user can connect from any host.
grant all privileges on *.* to 'dev'@'%'; # GRANT ALL PRIVILEGES ON *.* TO 'new_user'@'%'; ..
flush privileges; # Flush privileges to apply the changes

# Create db
create database mydb;
use mydb;
create table if not exists countries (id int auto_increment primary key, country varchar(255), capital varchar(255), leader varchar(255));
insert into countries (country, capital, leader) values ("Kenya", "Nairobi", "William Ruto");
insert into countries (country, capital, leader) values ("Tanzania", "Dodoma", "Samia Suluhu");
insert into countries (country, capital, leader) values ("Uganda", "Kampala", "Yoweri Museveni");
insert into countries (country, capital, leader) values ("Australia", "Canberra", "Anthony Albanese");
insert into countries (country, capital, leader) values ("USA", "Washington", "Joe Biden");
insert into countries (country, capital, leader) values ("South Africa", "Pretoria", "Cyril Ramaphosa");