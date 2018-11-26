import psycopg2
import datetime

DBNAME = "news"

if __name__ == '__main__':

    conn = psycopg2.connect(database=DBNAME)

    curr = conn.cursor()

    curr.execute("SELECT articles.title ," +
                 " count (path) as sum FROM articles JOIN log" +
                 " ON  log.path LIKE '%' || articles.slug || '%'" +
                 " group by title order by sum desc limit 3;")

    result = curr.fetchall()

    print("What are the most popular three articles of all time?")

    for i in range(len(result)):

        print( '"'+result[i][0]+'"'+ '--' + result[i][1] + 'views')

    print ''

    curr.execute("select authors.name , count (path) as sum " +
                 "from articles " +
                 " INNER JOIN log " +
                 "ON  log.path LIKE '%' || articles.slug || '%' " +
                 "INNER JOIN authors " +
                 "on articles.author = authors.id " +
                 "group by name " +
                 "order by sum desc limit 3;")

    result = curr.fetchall()

    print("What are the most popular three authors of all time?")

    for i in range(len(result)):

        print result[i][0], '--', result[i][1], 'views'

    print ''

    curr.execute(" SELECT date(time) , " +
                 " ( COUNT(*)*100.00/(SELECT COUNT(*) FROM log WHERE status  like '404 %') )  AS Percentage " +
                 "FROM log " +
                 "where status like '404 %' " +
                 "GROUP BY date(time) , status " +
                 "order by Percentage desc " +
                 "limit 1;")

    result = curr.fetchall()

    print("What are the most popular three articles of all time?")
    for i in range(len(result)):
        d =  result[i][0] 
        s= d.strftime('%B %d,%Y')
        e=format(result[i][1] , '.2f')

    for i in range(len(result)):
        t = datetime.datetime.strptime(s, '%B %d,%Y')
        dd = t.strftime('%B %d,%Y')

    for i in range(len(result)):

        print( dd +'--' + e+ '% errors')

    print ''


conn.close()
