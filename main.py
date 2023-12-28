import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'anna2002'
database = 'Skrylnyk_Anna_DB'
host = 'localhost'
port = '5432'

queries = [
    '''
    CREATE OR REPLACE VIEW count_of_genre AS
    SELECT
        Genre,
        COUNT(*) AS MovieCount
    FROM
        Movies
    GROUP BY
        Genre
    ORDER BY
	    MovieCount;
    ''',
    '''
    CREATE OR REPLACE VIEW count_of_genre AS
    SELECT
        Genre,
        COUNT(*) AS MovieCount
    FROM
        Movies
    GROUP BY
        Genre
    ORDER BY
	    MovieCount;
    ''',
    '''
    CREATE OR REPLACE VIEW avgfilm_rating_by_actor AS
    SELECT AVG(AvgRating), ActorCount FROM (
    	SELECT
    	    m.MovieID_,
    	    COUNT(a.ActorID) AS ActorCount,
    	    AVG(m.PeopleRating + m.CriticsRating)/2 AS AvgRating
    	FROM
    	    Movies m
    	    LEFT JOIN Actor a ON m.MovieID_ = a.MovieID_
    	GROUP BY
    	    m.MovieID_) as subquery
    	GROUP BY ActorCount
        ORDER BY ActorCount;
    '''
]

def visualize(result_1, result_2, result_3):
    film_genre = []
    total = []

    for row in result_1:
        film_genre.append(row[0])
        total.append(row[1])

    x_range = range(len(film_genre))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, total, label='Total')
    bar_ax.bar_label(bar, label_type='center', fmt='%d')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(film_genre, rotation=90)
    bar_ax.set_xlabel('Назви жанрів')
    bar_ax.set_yticks(bar_ax.get_yticks())
    bar_ax.set_yticklabels(str(int(float(label))) for label in bar_ax.get_yticks())
    bar_ax.set_ylabel('Кількість, шт.')
    bar_ax.set_title('Кількість фільмів, що належать до жанрів')

    pie_ax.pie(total, labels=film_genre, autopct='%1.01f%%')
    pie_ax.set_title('Частка фільмів кожного жанру')

    rating = []
    count = []

    for row in result_3:
        rating.append(round(row[0], 3))
        count.append(row[1])

    graph_ax.plot(count, rating, color='blue', marker='o')

    for cnt, rat in zip(count, rating):
        graph_ax.annotate(rat, xy=(cnt, rat), color='blue',
                           textcoords='offset points')

    graph_ax.set_xlabel('Кількість акторів')
    graph_ax.set_ylabel('Рейтинг')
    graph_ax.set_title('Графік залежності середнього рейтингу фільмів від кількості його акторів')

    mng = plt.get_current_fig_manager()
    mng.resize(1800, 900)

    plt.show()

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn.cursor() as cursor:
    for query in queries:
        cursor.execute(query)

    cursor.execute("select * from count_of_genre")
    result_1 = cursor.fetchall()
    cursor.execute("select * from count_of_genre")
    result_2 = cursor.fetchall()
    cursor.execute("select * from avgfilm_rating_by_actor")
    result_3 = cursor.fetchall()
    visualize(result_1, result_2, result_3)