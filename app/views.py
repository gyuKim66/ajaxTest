from flask import render_template, request, redirect, url_for, flash
from app import app, db, models
# from .models import Idea
from .forms import IdeaForm
import json
import logging


@app.route('/', methods=["GET", "POST"])
def index():
	form = IdeaForm()

	app.logger.info(' ')
	app.logger.info('From index route handler ....')

	if form.validate_on_submit():
		if db.session.query(models.Idea).filter_by(text= form.idea.data).count() < 1:
			new_idea = models.Idea(text = form.idea.data)
			db.session.add(new_idea)
			db.session.commit()

		flash("Thanks for your bright new idea: " + str(form.idea.data))

	ideas = models.Idea.query.all()


	print()
	print("Number of isea in db: ", len(ideas))
	print()

	return render_template('index.html', form=form, ideas=ideas)


@app.route('/vote', methods=["POST"])
def vote():

	app.logger.info(' ')
	app.logger.info('From vote route handler ....')

	data = json.loads(request.data)
	idea_id = int(data.get('idea_id'))
	idea = models.Idea.query.get(idea_id)

	if data.get('vote_type') == 'up':
		idea.upvotes += 1
	else:
		idea.downvotes += 1
	
	db.session.commit()

	dict1 = {'status':'OK', 'upvotes': idea.upvotes, 'downvotes': idea.downvotes}
	return json.dumps(dict1)


