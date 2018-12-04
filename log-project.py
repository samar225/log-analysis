#! /usr/bin/env python
import psycopg2
import datetime

DBNAME = "news"

if __name__ == '__main__':

    try:
        conn = psycopg2.connect(database=DBNAME)
    except psycopg2.DatabaseError, e:
        print("<error message>")

    curr = conn.cursor()

    curr.execute("select title, count(*) as views " +
                 "from log join articles " +
                 "on log.path = concat('/article/', articles.slug) " +
                 "group by title " +
                 "order by views desc" +
                 " limit 3;")

    result = curr.fetchall()

    print("What are the most popular three articles of all time?")

    for i in range(len(result)):

        print('"' + str(result[i][0]) + '"' + '--' +
              str(result[i][1]) + 'views')

    print ''

    curr.execute("select authors.name , count (path) as sum" +
                 " from articles" +
                 " INNER JOIN log" +
                 " on log.path = concat('/article/', articles.slug)" +
                 " INNER JOIN authors" +
                 " on articles.author = authors.id" +
                 " group by name " +
                 " order by sum desc limit 3;")

    result = curr.fetchall()

    print("What are the most popular three authors of all time?")

    for i in range(len(result)):

        print str(result[i][0]), '--', str(result[i][1]), 'views'

    print ''

    curr.execute(" SELECT date(time) , " +
                 "COUNT(status) as b , " +
                 "(SELECT COUNT(status) FROM log WHERE status" +
                 "  not like '200 OK') as  a " +
                 "FROM log " +
                 "where( (select (a/b)*100 from log )  >1.0 ) " +
                 "GROUP BY date(time) , status " +
                 "limit 1;")

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


conn.close()
