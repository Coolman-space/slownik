from database.database_connection import DatabaseConnection


def create_word_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS words(english_form text, knowing_form text, level_complicate integer, level_knowing integer)')



def add_new_word(english_form, knowing_form, level_com):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO words VALUES("{english_form}","{knowing_form}","{level_com}", 0)')


def get_all_words():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM words')

        words = [{'english_form': row[0],
                  'knowing_form': row[1],
                  'level_complicate': int(row[2]),
                  'level_knowing': row[3]} for row in cursor.fetchall()
                 ]

        return words


def delete_word(english_form):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM words WHERE english_form=?', (english_form,))
