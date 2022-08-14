from app import create_app
from app.business.database import get

app = create_app()


@app.route('/')
def start():  # put application's code here
    get()
    return "tela inicial"

if __name__ == '__main__':
    app.run()
