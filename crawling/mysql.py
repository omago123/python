import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='0000',
                             database='bamin',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `client`"
        cursor.execute(sql)
        result = cursor.fetchall()
        for re in result:
            print(re["client_name"])