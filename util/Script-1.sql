CREATE TABLE if not exists item (
       id     SERIAL       PRIMARY KEY,
       name   VARCHAR(120) NOT NULL,
       type   VARCHAR(50)  NOT NULL,
       weight REAL NOT NULL,
       volume REAL NOT NULL
    );
    
create index idx_item_name on item(name);
   
create table if not exists setor(
	id SERIAL primary key,
	name VARCHAR(120) not null
);

create index idx_setor_name on setor(name);

create table if not exists prateleira(
	id SERIAL primary key,
	max_volume real not null,
	max_weight real not null,
	setor serial,
	
	constraint fk_prat_setor foreign key(setor) references setor(id)
);

create index idx_prat_setor on prateleira(setor);  

create table if not exists item_estoque (
	id         SERIAL primary key,
	item_id    SERIAL not null,
	quantity   int    not null default 0, 
	prateleira SERIAL not null,
	

	constraint fk_item_estoque_item foreign key(item_id)    references item(id),
	constraint fk_item_estoque_prat foreign key(prateleira) references prateleira(id)
);


insert into setor(name) values ('padaria');
insert into setor(name) values ('doces');
insert into setor(name) values ('bebidas');
insert into setor(name) values ('eletrodomesticos');

insert into prateleira(max_volume, max_weight, setor) values (100.0, 50.0, 1);
insert into prateleira(max_volume, max_weight, setor) values (200.0, 125.0, 1);

insert into prateleira(max_volume, max_weight, setor) values (100.0, 25.0, 2);
insert into prateleira(max_volume, max_weight, setor) values (50.0, 50.0, 2);

insert into prateleira(max_volume, max_weight, setor) values (150.0, 300.0, 3);
insert into prateleira(max_volume, max_weight, setor) values (400.0, 300.0, 3);

insert into prateleira(max_volume, max_weight, setor) values (100.0, 100.0, 4);

insert into item(name, type, weight, volume) values ('Pão Frances', 'COMIDAS', 1, 3);
insert into item(name, type, weight, volume) values ('Sonho', 'COMIDAS', 2, 3);
insert into item(name, type, weight, volume) values ('Pão Cervejinha', 'COMIDAS', 1, 3);

insert into item(name, type, weight, volume) values ('Doce de Leite', 'COMIDAS', 3, 6);

insert into item(name, type, weight, volume) values ('Fogão', 'ELETRODOMESTICO', 50, 100);
insert into item(name, type, weight, volume) values ('Microondas', 'ELETRODOMESTICO', 30, 75);
insert into item(name, type, weight, volume) values ('Lava & Seca', 'ELETRODOMESTICO', 80, 100);


insert into item(name, type, weight, volume) values ('Tequila', 'BEBIDAS', 2, 7);
insert into item(name, type, weight, volume) values ('Coca-Cola', 'BEBIDAS', 3, 7);

--pao frances
insert into item_estoque(item_id, quantity, prateleira) values (1, 10, 1);
--cervejinha
insert into item_estoque(item_id, quantity, prateleira) values (3, 30, 2);

--sonho
insert into item_estoque(item_id, quantity, prateleira) values (2, 10, 3);
--doce de leite
insert into item_estoque(item_id, quantity, prateleira) values (4, 8, 4);

-- fogao
insert into item_estoque(item_id, prateleira) values (5, 5);
--microondas
insert into item_estoque(item_id, prateleira) values (6, 6);
--lava e seca
insert into item_estoque(item_id, prateleira) values (7, 5);

--tequila
insert into item_estoque(item_id, prateleira) values (8, 7);
--coca cola
insert into item_estoque(item_id, prateleira) values (9, 7);



select i.name as nome_produto, i.type as tipo, e.quantity as quantidade, p.id as prateleira, s.name as setor
	from item_estoque e
	inner join item i       on i.id = e.item_id
	inner join prateleira p on p.id = e.prateleira
	inner join setor s      on s.id = p.setor;

