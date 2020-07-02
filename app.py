import random

from flask import Flask, render_template, abort, request, url_for
from projects import projects as project_list
import os

from flask_mail import Mail, Message

app = Flask(__name__)

# App Config
app.url_map.strict_slashes = False  # Allows trailing slashes in URL

# Mail Config
app.config['MAIL_SERVER'] = 'smtp.zoho.eu'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'admin@emmakirbydesign.co.uk'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


@app.context_processor
def header_image():
    def random_image():
        index_photos = [url_for('static', filename='img/what-we-do/ex2.jpeg'),
                        url_for('static', filename='img/what-we-do/example.jpeg'),
                        url_for('static', filename='img/projects/winter-and-summer-barns-with-pool/-WHuAFgq.jpg'),
                        url_for('static', filename='img/projects/winter-and-summer-barns-with-pool/c8DQ7kLU.jpg'),
                        url_for('static', filename='img/projects/winter-and-summer-barns-with-pool/5WFU54Oo.jpg'),
                        url_for('static', filename='img/projects/winter-and-summer-barns-with-pool/eLWg40Q1.jpg'),
                        url_for('static', filename='img/projects/winter-and-summer-barns-with-pool/pGa9GPQw.jpg'),
                        url_for('static', filename='img/projects/winter-and-summer-barns-with-pool/y7k8dvwj.jpg'),
                        url_for('static', filename='img/projects/soho-farmhouse/1Sk3gCOZ.jpeg'),
                        url_for('static', filename='img/projects/soho-farmhouse/CM2DAZkL.jpeg'),
                        url_for('static', filename='img/projects/soho-farmhouse/6seWC6EI.jpeg'),
                        url_for('static', filename='img/projects/soho-farmhouse/uXlZjUMM.jpeg'),
                        url_for('static', filename='img/projects/village-house-interiors-pool-and-pool-house/hjtyCIv0.jpeg'),
                        url_for('static', filename='img/projects/village-house-interiors-pool-and-pool-house/u0xthdMZ.jpeg'),
                        url_for('static', filename='img/projects/village-house-interiors-pool-and-pool-house/JASEW__k.jpeg')]
        return random.choice(index_photos)
    return dict(random_image=random_image)


@app.route('/')
def index():
    return render_template('homepage/index.html')


@app.route('/about-us')
def about_us():
    return render_template('about-us/about-us.html', title='About Us')


@app.route('/what-we-do')
def what_we_do():
    return render_template('what-we-do/what-we-do.html', title='What We Do')


@app.route('/projects')
def projects():
    return render_template('projects/projects.html', title='Projects', projects=project_list)


@app.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        msg = Message('Service Inquiry', sender=(request.form.get('name'), 'no-reply@emmakirbydesign.co.uk'), recipients=['admin@emmakirbydesign.co.uk'], reply_to=request.form.get('email'))
        msg.html = request.form.get('message')
        mail.send(msg)
        return '1'

    return render_template('contact-us/contact-us.html', title='Contact Us')


@app.route('/projects/<project_page>')
def project(project_page):

    result = None
    for p in project_list:
        if p.url == project_page:
            result = p

    if not result:
        return abort(404)

    return render_template('project/project.html', project=result, title=result.title)


@app.route('/privacy')
def privacy():
    return render_template('base/privacy.html', title='Privacy')


@app.route('/terms')
def terms():
    return render_template('base/terms.html', title='Terms')


if __name__ == '__main__':
    app.run()
