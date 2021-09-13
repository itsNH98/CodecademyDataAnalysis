select * 
from employees;

select * 
from projects;

select first_name, last_name, current_project 
from employees 
where current_project is NULL;

select project_name
from projects 
where project_id not in (
  select current_project
  from employees 
  where current_project is not null
);

select project_name
from projects
inner join employees
  ON projects.project_id = employees.current_project
where current_project is not null
group by project_name 
order by count(employee_id) desc
limit 1;

select project_name 
from projects
inner join employees
  on employees.current_project = projects.project_id
where current_project is not null
group by current_project
having count(current_project)>1;

SELECT (COUNT(*) * 2) - (
  SELECT COUNT(*)
  FROM employees
  WHERE current_project IS NOT NULL
    AND position = 'Developer') AS 'Count'
FROM projects;


select personality, count(*) 
from employees
group by personality
order by count(personality) desc;

select last_name, first_name, personality, project_name
from employees
inner join projects
  on employees.current_project = projects.project_id
where personality = (
  select personality
  from employees
  where current_project is not null
  group by personality
  order by count(personality) desc
  limit 1
);
