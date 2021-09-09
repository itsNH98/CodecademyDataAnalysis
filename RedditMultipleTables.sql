SELECT * FROM users limit 10;
SELECT * FROM posts limit 10;
SELECT * FROM subreddits limit 10;

select count(name)
from subreddits;

select username, max(score)
from users;

select title, max(score)
from posts;

select name, subscriber_count
from subreddits
order by subscriber_count desc
limit 5;

select users.username, count(*) as 'posts_made'
from users
left join posts
  on users.id = posts.user_id
group by users.id
order by 2 desc;

select *
from users
inner join posts
  on posts.user_id = users.id;

select * 
from posts
union 
select * 
from posts2
/*
with popular_posts as (
  select * 
  from posts
  where score > 5000
) 
select subreddits.name, popular_posts.title, popular_posts.score 
from subreddits 
inner join popular_posts
  on subreddits.id = posts.subreddit_id
order by popular_posts.score desc;


SELECT 
  posts.title, 
  subreddits.id AS 'subreddit_name', 
  MAX(posts.score) AS 'highest_score'
FROM posts
INNER JOIN subreddits
  ON posts.subreddit_id = subreddits.id
GROUP BY subreddits.id;

SELECT 
  subreddits.name, 
  AVG(posts.score) AS 'average_score'
FROM subreddits
INNER JOIN posts
ON subreddits.id = posts.subreddit_id
GROUP BY subreddits.name
ORDER BY 2 DESC;





