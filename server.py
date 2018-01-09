from flask import Flask, render_template, Response
import git, json

app = Flask(__name__)
repo = git.Repo( '/home/metis/code/Straylight' )


@app.route('/')
def scoreboard():
    return render_template('scoreboard.html')

@app.route('/scores')
def scores():
    scores = get_scores(repo)
    return Response(json.dumps(scores), mimetype='application/json')


def get_scores(repo):
    scores = []
    shortlog = repo.git.shortlog("-s", "-n", "--all")
    for item in shortlog.splitlines():
        item = item.split("\t")
        item[0] = item[0].replace(" ","")
        scores.append(item)
    return sorted(scores, key=lambda x: int(x[0]), reverse=True)
