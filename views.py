from flask import render_template, request, redirect, url_for, flash
from models import db, Game

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        games = Game.query.all()
        return render_template('index.html', message='Displaying all items', games=games)



    @app.route('/add', methods=['POST','GET'])
    def create_item():
        if request.method == 'POST':
            new_game = Game(
                title=request.form['title'],
                publisher=request.form['publisher'],
                genre=request.form['genre'],
                image_url=request.form['image_url'],
                rating=float(request.form['rating']),
                year=int(request.form['year']),
                description=request.form['description'])
            db.session.add(new_game)
            db.session.commit()
            return redirect(url_for('get_items'))
        
        else:
            return render_template('add.html', message='Item added successfully')



    @app.route('/update', methods=['POST','GET'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')



    @app.route('/delete', methods=['GET'])
    def delete_item():
        id = request.args.get('id')
        db.session.delete(id)
        return render_template('index.html', message=f'Item deleted successfully')