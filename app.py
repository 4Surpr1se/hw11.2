from flask import Flask, render_template
import utils

app = Flask(__name__)

worker_list = utils.load_candidates_from_json('candidates.json')


@app.route("/")
def page_index():
    return render_template('list.html', items=worker_list)


@app.route('/candidate/<int:id>')
def id_user(id):
    candidate = utils.get_candidate(id)
    return render_template('single.html', i=candidate)


@app.route('/search/<candidate_name>')
def name(candidate_name):
    output_text = ''
    condidate_list = utils.get_candidates_by_name(candidate_name)
    for l in condidate_list:
        output_text += render_template('search.html', i=l)
    return f'<h1>найдено кандидатов {len(condidate_list)}</h2><br>{output_text}'


@app.route('/skill/<skill_name>')
def skill(skill_name):
    output_text = ''
    condidate_list = utils.get_candidates_by_skill(skill_name)
    for l in condidate_list:
        output_text += render_template('skill.html', i=l)
    return f'<h1>найдено кандидатов {len(condidate_list)}</h2><br>{output_text}'


app.run()
