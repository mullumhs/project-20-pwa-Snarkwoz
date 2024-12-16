from flask import render_template, request, redirect, url_for, flash
from models import db, Game

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):
    # Checks for a search and displays all games
    @app.route('/', methods=['GET'])
    def get_items():
        search_query = request.args.get('search')
        if search_query:
            games = Game.query.filter(Game.title.ilike(f'%{search_query}%')).all()
        else:
            games = Game.query.all()
        return render_template('index.html', games=games)


    @app.route('/add', methods=['POST','GET'])
    # Create a new game 
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
            return render_template('add.html')


    @app.route('/update', methods=['POST','GET'])
    # Updates a game
    def update_item():
        if request.method == 'POST':
            id = request.args.get('id')
            game = Game.query.get_or_404(id)
            game.title = request.form['title']
            game.publisher = request.form['publisher']
            game.genre = request.form['genre']
            game.image_url = request.form['image_url']
            game.rating = float(request.form['rating'])
            game.year = int(request.form['year'])
            game.description = request.form['description']
            db.session.commit()
            return redirect(url_for('get_items'))
        
        else:
            id = request.args.get('id')
            game = Game.query.get_or_404(id)
            return render_template('edit.html', game=game)
        


    @app.route('/delete', methods=['GET'])
    # Deletes a game
    def delete_item():
        id = request.args.get('id')
        game = Game.query.get_or_404(id)
        db.session.delete(game)
        db.session.commit()
        return redirect(url_for('get_items'))