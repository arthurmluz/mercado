import secrets
from app import create_app


app = create_app()

""" Initialize the application """
if __name__ == '__main__':
    if secrets.dbuser == 'arthur':
        print("\n>>> ALTERAR VALORES DE ACESSO AO BANCO DE DADOS NO SECRETS.PY <<<")
        print(">>> Valores foram enviados junto ao email de entrega <<<")
        exit(0)
    app.run()
