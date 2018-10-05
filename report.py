#!/usr/bin/env python3

import psycopg2

# setup a database connection and cursor
db = psycopg2.connect(database='news')
c = db.cursor()

# report on top article page views
select_top_articles = '''
    select articles.title, count(*) as count
    from log, articles
    where '/article/' || articles.slug = log.path
    group by articles.title
    order by count desc limit 3;'''
c.execute(select_top_articles)
rows = c.fetchall()
print('Top 3 Article Page Views')
for row in rows:
    print('{} -- {} views'.format(row[0], row[1]))
print()

# report on per author page views
select_author_count = '''
    select article_summary.author, count(*) as count
    from log, article_summary
    where '/article/' || article_summary.slug = log.path
    group by article_summary.author
    order by count desc;'''
c.execute(select_author_count)
rows = c.fetchall()
print('Page Views Per Author')
for row in rows:
    print('{} -- {} views'.format(row[0], row[1]))
print()

# report on days where failure rate is over 1%
select_failures = '''
    select *
        from (
            select day, round(100.0 * errors / total, 1) as fail_percent
            from status_summary
        ) as s
    where s.fail_percent > 1.0;'''
c.execute(select_failures)
rows = c.fetchall()
print('Days Where Failure Rate is Over 1%')
for row in rows:
    print('{} -- {}% errors'.format(row[0].strftime('%B %d, %Y'), row[1]))
print()

# cleanup database connection
c.close()
db.close()
