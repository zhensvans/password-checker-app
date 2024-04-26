from flask import Flask, render_template, request
from password_utils import (analyze_password, calculate_entropy, get_password_suggestions,
                            generate_password, is_password_breached, get_breached_count,
                            get_password_strength)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form['password']
    has_uppercase, has_lowercase, has_digit, has_symbol, has_ten = analyze_password(password)
    entropy = calculate_entropy(password)
    strength = get_password_strength(entropy)
    is_breached = is_password_breached(password)
    count=get_breached_count(password)
    return render_template(
        'result.html',
        has_uppercase=has_uppercase,
        has_lowercase=has_lowercase,
        has_digit=has_digit,
        has_symbol=has_symbol,
        has_ten=has_ten,
        password=password,
        entropy=entropy,
        strength=strength,
        is_breached=is_breached,
        count=count
    )


@app.route('/generate_password', methods=['GET'])
def generate_new_password():
    new_password = generate_password()
    return render_template(
        'generated_password.html',
        new_password=new_password)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, ssl_context=('localhost.crt', 'localhost.key'))
