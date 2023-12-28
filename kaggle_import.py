import psycopg2
from datetime import datetime
import csv

username = 'postgres'
password = 'anna2002'
database = 'Skrylnyk_Anna_DB'



import_rage = 500

csv_file_path = "filmtv_movies.csv"

def main():
    conn = psycopg2.connect(user=username, password=password, dbname=database)
    cursor = conn.cursor()

    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        StudioID = 0
        ActorID = 0
        DirectorID = 0
        for row in csv_reader:
            StudioID += 1
            MovieID_,Title,ReleaseYear,Genre,Duration,Country,Directors,Actors,avg_vote,CriticsRating,PeopleRating,total_votes,description,notes,humor,rhythm,effort,tension,erotism = row

            cursor.execute("insert into ProductionStudios (StudioID, StudioName, Country, YearFounded) values (%s, %s, %s, %s) returning StudioID",
                           (StudioID, 'Studio Name', 'Country', datetime.now().date()))



            if PeopleRating == '':
                PeopleRating = CriticsRating
            if CriticsRating == '':
                CriticsRating = PeopleRating
            date_str = f'{ReleaseYear}-01-21'
            date_format = '%Y-%m-%d'
            date_obj = datetime.strptime(date_str, date_format)
            cursor.execute("insert into Movies (MovieID_, Title, ReleaseYear, Genre, Duration, Country, PeopleRating, CriticsRating, StudioID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) returning MovieID_",
                           (MovieID_, Title, date_obj, Genre, Duration, Country, PeopleRating, CriticsRating, StudioID))



            Actors = [Actor.strip() for Actor in Actors.split(',')]
            for Actor in Actors:
                initials = [initial.strip() for initial in Actor.split()]
                n = len(initials) // 2
                cursor.execute("insert into Actor (ActorID, FirstName, LastName, BirthYear, Country, MovieID_) VALUES (%s, %s, %s, %s, %s, %s) returning MovieID_",
                               (ActorID, " ".join(initials[:n]), " ".join(initials[n:]), datetime.now().date(), 'Country', MovieID_))
                ActorID += 1



            Directors = [Director.strip() for Director in Directors.split(',')]
            for Director in Directors:
                initials = [initial.strip() for initial in Director.split()]
                n = len(initials) // 2
                cursor.execute("insert into Director (DirectorID, FirstName, LastName, BirthYear, Country, MovieID_) VALUES (%s, %s, %s, %s, %s, %s) returning MovieID_",
                               (DirectorID, " ".join(initials[:n]), " ".join(initials[n:]), datetime.now().date(), 'Country', MovieID_))
                DirectorID += 1
            if StudioID == import_rage:
                break

    conn.commit()

    cursor.close()
    conn.close()

def clear_tables():
    conn = psycopg2.connect(user=username, password=password, dbname=database)
    cursor = conn.cursor()

    cursor.execute("delete from Director")
    cursor.execute("delete from Actor")
    cursor.execute("delete from Movies")
    cursor.execute("delete from ProductionStudios")

    conn.commit()

    cursor.close()
    conn.close()

clear_tables()
main()