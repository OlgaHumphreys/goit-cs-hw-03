select *
from tasks t 
where user_id = 4;

select *
from tasks
where status_id = (
	select id 
	from status
	where name = 'new'
);

update tasks 
set status_id = (
	select id 
	from status
	where name = 'in progress')
where id = 1;

select *
from users
where id not in (
	select user_id
	from tasks)


insert into tasks (title, description, status_id, user_id)
values ('New task', 'Task description', 1, 7)



select *
from tasks
where status_id <> (
	select id
	from status
	where name = 'completed')


delete 
from tasks 
where id = 31


select *
from users
where email like 'john@example.com'


update users 
set name = 'ivan'
where id = 1


select status.name, COUNT(tasks.id)
from status
left join tasks on  status.id = tasks.status_id
group by status.name;


select tasks.*
from tasks
	join users on tasks.user_id  = users.id
where users.email like '%@example.com';


select *
from tasks
where description is null
	or description = '';



select users.name, tasks.title 
from users
	inner join tasks on users.id = tasks.user_id
where tasks.status_id = (
	select id 
	from status
	where name = 'in progress');



select users.name, count(tasks.id)
from users
	left join tasks on users.id = tasks.user_id 
group by users.name
