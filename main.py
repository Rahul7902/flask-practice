from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/overview')
def overview():
    return render_template('overview.html', title='Overview')

@app.route('/watsonx')
def watsonx():
    return render_template('watsonx.html', title='WatsonX')

@app.route('/agents')
def agents():
    return render_template('explore_ai_agents.html', title='Agents')

@app.route('/granite_models')
def granite_models():
    return render_template('granite.html', title='Granite Models')

@app.route('/hybrid_clouds')
def hybrid_clouds():
    return render_template('hybrid_clouds.html', title='Hybrid Clouds')

@app.route('/products')
def products():
    return render_template('watsonx.html', title='Products')

@app.route('/consulting')
def consulting():
    return render_template('consulting.html', title='Consulting')

@app.route('/support')
def support():
    return render_template('support.html', title='Support')

@app.route('/think')
def think():
    return render_template('think.html', title='Think')

@app.route('/explore_ai_agents')
def explore_ai_agents():
    return render_template('explore_ai_agents.html', title='Explore AI Agents')

@app.route('/work_in_progress')
def work_in_progress():
    return render_template('work_in_progress.html', title='WIP')

# @app.route('/')

if __name__ == '__main__':
    app.run(debug=True)