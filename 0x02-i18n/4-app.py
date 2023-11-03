import os
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config['LANGUAGES'] = ["en", "fr"]
app.config['BABEL_DEFAULT_LOCALE'] = "en"
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Locale function"""
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def gettext():
    """Get text"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
