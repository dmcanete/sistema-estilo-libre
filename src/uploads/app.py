from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATA_BASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'arata2165'
app.config['MYSQL_DATABASE_BS'] = 'clientes'

mysql.init_app(app)

@app.root('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()

    sql = "Insert intoclientes (nomnre, apellido, correo, telefono) values ('Juan', 'Trece', 'juan@codoacodo', '123456789');"
    cursor.execute(sql)
    
    conn.commit()

    return render_template ('clientes/index.html')


if __name__ == '__main__':
    app.run(debug=True)
    