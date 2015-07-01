DROP TABLE IF EXISTS "athletes";
DROP TABLE IF EXISTS "competitions";
DROP TABLE IF EXISTS "results";

create table results(comp_id int, winner varchar(20), medal varchar(10));
create table athletes(name varchar(20) primary key,  nationality varchar(20), gender char(1));
create table competitions(comp_id int primary key, name varchar(20), type varchar(10));


insert into competitions values(3,'biathlon','10000');
insert into results values(3, 'bjoerndalen','gold');
insert into results values (3, 'landertinger','silver');
insert into results values(3, 'soukup','bronze');
insert into athletes values('bjoerndalen','norway','M');
insert into athletes values('landertinger','austria','M');
insert into athletes values('soukup','czech republic','M');


insert into competitions values(4,'skijumping','nh');
insert into results values(4,'stoch','gold');
insert into results values(4,'prevc','silver');
insert into results values(4,'bardal','bronze');
insert into athletes values('stoch','poland','M');
insert into athletes values('prevc','slovenia','M');
insert into athletes values('bardal','norway','M');


insert into competitions values(5,'speedskating','1000');
insert into results values(5,'groothuis','gold');
insert into results values(5,'morrison','silver');
insert into results values(5,'mulder','bronze');
insert into athletes values('groothuis','netherlands','M');
insert into athletes values('morrison','canada','M');
insert into athletes values('mulder','netherlands','M');


insert into competitions values(6,'speedskating','500');
insert into results values(6,'mulder','gold');
insert into results values(6,'smeekens','silver');
insert into results values(6,'mulder','bronze');
insert into athletes values('smeekens','russia','M');

insert into competitions values(7,'shorttrack','1500');
insert into results values(7,'hamelin','gold');
insert into results values(7,'han','silver');
insert into results values(7,'an','bronze');
insert into athletes values('hamelin','canada','M');
insert into athletes values('han','china','M');
insert into athletes values('an','russia','M');


insert into competitions values(9,'icedancing','');
insert into results values(9,'davis','gold');
insert into results values(9,'white','gold');
insert into results values(9,'moir','bronze');
insert into results values(9,'virtue','bronze');
insert into results values(9,'ilinykh','silver');
insert into results values(9,'katsalapov','silver');
insert into athletes values('davis','usa','F');
insert into athletes values('white','usa','M');
insert into athletes values('moir','canada','M');
insert into athletes values('virtue','canada','F');
insert into athletes values('ilinykh','russia','F');
insert into athletes values('katsalapov','russia','M');


insert into competitions values(10,'giantslalom','');
insert into results values(10,'ligety','gold');
insert into results values(10,'missillier','silver');
insert into results values(10,'pinturault','bronze');
insert into athletes values('ligety','usa','M');
insert into athletes values('missillier','france','M');
insert into athletes values('pinturault','france','M');


insert into competitions values(11,'crosscountry','');
insert into results values(11,'bjoergen','gold');
insert into results values(11,'johaug','silver');
insert into results values(11,'steira','bronze');
insert into athletes values('bjoergen','norway','F');
insert into athletes values('johaug','norway','F');
insert into athletes values('steira','norway','F');


insert into competitions values(12,'slalom','');
insert into results values(12,'matt','gold');
insert into results values(12,'hirscher','silver');
insert into results values(12,'kristoffersen','bronze');
insert into athletes values('matt','austria','M');
insert into athletes values('hirscher','austria','M');
insert into athletes values('kristoffersen','norway','M');


insert into competitions values(13,'super-combined','');
insert into results values(13,'hoefl-riesch','gold');
insert into results values(13,'hosp','silver');
insert into results values(13,'mancuso','bronze');
insert into athletes values('hoefl-riesch','germany','F');
insert into athletes values('hosp','austria','F');
insert into athletes values('mancuso','usa','F');


insert into competitions values(15,'skijumping','lh');
insert into results values(15,'vogt','gold');
insert into results values(15,'iraschko-stolz','silver');
insert into results values(15,'mattel','bronze');
insert into athletes values('vogt','germany','F');
insert into athletes values('iraschko-stolz','austria','F');
insert into athletes values('mattel','france','F');


insert into competitions values(16,'biathlon','7500');
insert into results values(16,'kuzmina','gold');
insert into results values(16,'vilukhina','silver');
insert into results values(16,'semerenko','bronze');
insert into athletes values('kuzmina','slovakia','F');
insert into athletes values('vilukhina','russia','F');
insert into athletes values('semerenko','ukraine','F');