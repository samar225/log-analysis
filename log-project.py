#! /usr/bin/env python
import psycopg2
import datetime
import sys

DBNAME = "news"


query1 = '''select title, count(*) as views
            from log join articles
            on log.path = concat('/article/', articles.slug)
            group by title
            order by views desc
            limit 3;'''

query2 = '''select authors.name , count (path) as sum
            from articles
            INNER JOIN log
            on log.path = concat('/article/', articles.slug)
            INNER JOIN authors
            on articles.author = authors.id
            group by name
            order by sum desc limit 3;'''

query3 = '''WITH b as 
            (SELECT date(TIME) AS dateb,
            COUNT(status) AS total FROM log GROUP BY dateb ),
            a AS
            (SELECT date(TIME) AS datea, COUNT(status) AS fail
            FROM log
            WHERE status NOT LIKE '200 OK' GROUP BY datea)
           WITH b as 
             (SELECT date(time) AS dateb,
            COUNT(status) AS total FROM log GROUP BY dateb ),
            a AS
            (SELECT date(time) AS datea, COUNT(status) AS fail
            FROM log
            WHERE status NOT LIKE '200 OK' GROUP BY datea),
            c as
           (select a.datea as datee ,(100.0 * a.fail/b.total ) as per
          from a , b
           where a.datea = b.dateb
           group by datea
           ) 
           (select * from c where c.per >1); 
            '''


def answer1(curr):

    curr.execute(query1)
    result = curr.fetchall()
    print("What are the most popular three articles of all time?")
    for i in range(len(result)):
        print('"' + str(result[i][0]) + '"' + '--' +
              str(result[i][1]) + 'views')

    print ''


def answer2(curr):

    curr.execute(query2)
    result = curr.fetchall()
    print("What are the most popular three authors of all time?")
    for i in range(len(result)):
        print str(result[i][0]), '--', str(result[i][1]), 'views'
    print ''


def answer3(curr):

    curr.execute(query3)
    result = curr.fetchall()
    print("What are the most popular three articles of all time?")
    for i in range(len(result)):
        d = result[i][0]
        s = d.strftime('%B %d,%Y')
        e = format(result[i][1], '.2f')

    for i in range(len(result)):
        t = datetime.datetime.strptime(s, '%B %d,%Y')
        dd = t.strftime('%B %d,%Y')

    for i in range(len(result)):

        print(dd + '--' + e + '% errors')

    print ''


def run():
    """Running report ..."""
    try:
        conn = psycopg2.connect("dbname={}".format(DBNAME))
        curr = conn.cursor()
        print("Running reporting tools...\n")

        answer1(curr)
        print("\n")

        answer2(curr)
        print("\n")

        answer3(curr)
        print("\n")

    except psycopg2.Error as err:
        print "Unable to connect to database"
        sys.exit(1)      # The easier method - exit the program


if __name__ == '__main__':
    run()
else:
    print 'Importing ...'

conn.close()
