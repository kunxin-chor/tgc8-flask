from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template('home.template.html')


@app.route('/bmi', methods=["GET"])
def show_bmi_calculator():
    return render_template('bmi_form.template.html')


@app.route('/bmi', methods=["POST"])
def process_bmi_calculator():
    print(request.form)
    weight = request.form.get('weight')
    height = request.form.get('height')
    # whatever we get back from the form is a STRING
    bmi = float(weight) / float(height) * float(height)

    return render_template('bmi_results.template.html', bmi_result=bmi)


@app.route('/survey')
def show_health_survey():
    return render_template('survey.template.html')


@app.route('/survey', methods=["POST"])
def process_health_survey():
    full_name = request.form.get('full-name')
    gender = request.form.get('gender')
    symptoms = request.form.getlist('symptoms')

    return render_template('survey_results.template.html',
                           full_name=full_name,
                           gender=gender,
                           symptoms=symptoms)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
