from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')


    @app.route('/')
    def index():
        return render_template('index.html', TITLE='nitnot')

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='nitnot')

    @app.route('/testdb')
    def testdb():
        import psycopg2

        con = psycopg2.connect('dbname=nitnot user=devuser password=devpassword host=postgres')
        cur = con.cursor()

        cur.execute('select * from page;')

        id, title = cur.fetchone()
        con.close()
        return 'output table page: {} - {}'.format(id, title)

    return app

