from mysql import connector
#'password' : '553051922428536000',
def create_connection( ip='192.168.10.133', db ='parqueadero' ):
    config = {
    'user': 'root',
    'password' : '123456789',
    'host' : ip,
    'database': db
    }
    conn = None
    try:
        conn = connector.connect(**config)
        return conn
    except connector.Error as error:
        print(f"Error conectando: {error.msg}")