# /app.py
import mercadopago
from flask import Flask, jsonify, render_template


app = Flask(__name__)

urlsite = "https:/ozenvitta.onrender.com"


@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/sucess')
def sucesso():
    return render_template("sucesso.html")

@app.route('/sucess2')
def sucesso():
    return render_template("sucesso2.html")

@app.route('/sucess3')
def sucesso():
    return render_template("sucesso3.html")

@app.route('/sucess4')
def sucesso():
    return render_template("sucesso4.html")

@app.route('/failure')
def falha():
    return render_template("falha.html")

@app.route('/checkout')
def enviar_pag_checkout():
    link_pagamento = create_preference()
    return render_template("checkout.html", link_pagamento=link_pagamento)


@app.route('/checkout2')
def enviar_pag_checkout2():
    link_pagamento = create_preference2()
    return render_template("checkout2.html", link_pagamento=link_pagamento)

@app.route('/checkout3')
def enviar_pag_checkout3():
    link_pagamento = create_preference3()
    return render_template("checkout3.html", link_pagamento=link_pagamento)

@app.route('/checkout4')
def enviar_pag_checkout4():
    link_pagamento = create_preference4()
    return render_template("checkout4.html", link_pagamento=link_pagamento)

######
def create_preference():

    sdk = mercadopago.SDK("APP_USR-5715772148343132-112520-1462b5edd9366b7fe84b39beb42f0257-1833487732")

    payment_data = {
        "items": [
            {
                "id": "1",
                "title": "1 Pote",  # Nome do produto
                "quantity": 1,                # Quantidade
                "unit_price": 99.99,          # Preço unitário
            }
        ],
        "back_urls": {
            "success": urlsite+"/success",  # URL de sucesso
            "failure": urlsite+"/failure",  # URL de falha
            "pending": urlsite+"/pending",  # URL de pendente
        },
        "auto_return": "approved",  # Retorno automático quando o pagamento for aprovado
    }

    try:
        result = sdk.preference().create(payment_data)
        payment = result["response"]
        link_pagamento = payment["init_point"]

        print(link_pagamento)

        return link_pagamento ####

    except Exception as e:
        return jsonify({"error": str(e)}), 500
#######
def create_preference2():

    sdk = mercadopago.SDK("APP_USR-5715772148343132-112520-1462b5edd9366b7fe84b39beb42f0257-1833487732")

    payment_data = {
        "items": [
            {
                "id": "2",
                "title": "3 Potes",  # Nome do produto
                "quantity": 1,                # Quantidade
                "unit_price": 147.00,          # Preço unitário
            }
        ],
        "back_urls": {
            "success": urlsite+"/success2",  # URL de sucesso
            "failure": urlsite+"/failure",  # URL de falha
            "pending": urlsite+"/pending",  # URL de pendente
        },
        "auto_return": "approved",  # Retorno automático quando o pagamento for aprovado
    }

    try:
        result = sdk.preference().create(payment_data)
        payment = result["response"]
        link_pagamento = payment["init_point"]

        print(link_pagamento)

        return link_pagamento ####

    except Exception as e:
        return jsonify({"error": str(e)}), 500
###########
def create_preference3():

    sdk = mercadopago.SDK("APP_USR-5715772148343132-112520-1462b5edd9366b7fe84b39beb42f0257-1833487732")

    payment_data = {
        "items": [
            {
                "id": "3",
                "title": "5 Potes",  # Nome do produto
                "quantity": 1,                # Quantidade
                "unit_price": 197.00,          # Preço unitário
            }
        ],
        "back_urls": {
            "success": urlsite+"/success3",  # URL de sucesso
            "failure": urlsite+"/failure",  # URL de falha
            "pending": urlsite+"/pending",  # URL de pendente
        },
        "auto_return": "approved",  # Retorno automático quando o pagamento for aprovado
    }

    try:
        result = sdk.preference().create(payment_data)
        payment = result["response"]
        link_pagamento = payment["init_point"]

        print(link_pagamento)

        return link_pagamento ####

    except Exception as e:
        return jsonify({"error": str(e)}), 500
########
def create_preference4():

    sdk = mercadopago.SDK("APP_USR-5715772148343132-112520-1462b5edd9366b7fe84b39beb42f0257-1833487732")

    payment_data = {
        "items": [
            {
                "id": "4",
                "title": "8 Potes",  # Nome do produto
                "quantity": 1,                # Quantidade
                "unit_price": 247.00,          # Preço unitário
            }
        ],
        "back_urls": {
            "success": urlsite+"/success4",  # URL de sucesso
            "failure": urlsite+"/failure",  # URL de falha
            "pending": urlsite+"/pending",  # URL de pendente
        },
        "auto_return": "approved",  # Retorno automático quando o pagamento for aprovado
    }

    try:
        result = sdk.preference().create(payment_data)
        payment = result["response"]
        link_pagamento = payment["init_point"]

        print(link_pagamento)

        return link_pagamento ####

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
