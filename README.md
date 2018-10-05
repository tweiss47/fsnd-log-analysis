# Udacity FSND Project: Logs Analysis

This project consists of three files.
1. `report.py` a python script that will run three database reports.
2. `out.txt` sample output from an execution of `report.py`.
3. `README.md` this file, which describes the project.

Script file `report.py` will run 3 reports against the postgresql database
`news`. The database needs to be installed on the local system. The script is
written in python3. If python3 is invoked using the command `python` rather
than `python3` adjust the instructions accordingly.

Invoke by calling python directly.

```
$ python3 report.py
```

Or invoke as a shell script.

```
$ chmod u+x report.py
$ report.py
```

## Implementation Notes

The standard `news` database was modified to include two views to simplify
database queries.

The `article_summary` view below allowed both the article and author reports
to share almost an identical structure.

```
create view article_summary as
	select articles.title, authors.name as author, articles.slug
	from articles, authors
where articles.author = authors.id;
```

The `status_summary` view below simplified statistics gathering for the
failure report.

```
create view status_summary as
	select
		date_trunc('day',time) as day,
		count(*) as total,
		count(*) filter (where status != '200 OK') as errors
	from log group by day;
```
