#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def get_error_percent():

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view errors_count as"
              " select totals.date, 100.0 * error_views / total_views as"
              " error_percentage"
              " from (select date(time) as date, count(*) as total_views"
              " from log group by date(time)) as totals,"
              " (select date(time) as date, count(*) as error_views"
              " from log where status != '200 OK' group by date(time)) "
              "as errors where totals.date = errors.date order by totals.date")
    c.execute("select date, error_percentage"
              " from errors_count where error_percentage > 1.0;")
    results = c.fetchall()
    print("The date(s) with a percent of error higher than 1% were:")
    for x in results:
        print(str(x[0]) + " -- " + str(x[1]))
    db.close()


def get_popular_author():

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view auth_count as"
              " select author, count(log.id) as count"
              " from log join articles on articles.slug = SUBSTRING(path,10)"
              " group by author order by count;")
    c.execute("select name, count"
              " from authors join auth_count on id = author"
              " order by count desc;")
    results = c.fetchall()
    print("Authors in order of popularity by views:")
    for x in results:
        print(x[0] + " -- " + str(x[1]))
    db.close()


def get_popular_article():

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, count(log.id) as count"
              " from log join articles on articles.slug = SUBSTRING(path,10)"
              " group by title"
              " order by count desc limit 3;")
    results = c.fetchall()
    print("Articles in order of popularity by views:")
    for x in results:
        print(x[0] + " -- " + str(x[1]))
    db.close()


if __name__ == "__main__":

    get_popular_article()

    get_popular_author()

    get_error_percent()
