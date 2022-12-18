from flask import Flask
from apple_apps_getter import customize_app_data

app = Flask(__name__)

@app.route('/')
def get_apple_apps():
    return customize_app_data('us', 100)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
