from flask import Flask, request, Response
import json
app = Flask(__name__)
@app.route('/')
def moikka():
    return 'terve maailma!'

# http://127.0.0.1:3000/summa?luku1=5&luku2=45
@app.route('/summa2')
def summa2():
    print(request.args)
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1 + luku2

    #itse tehty json vastaus

    vastaus = {
        "luku1" : luku1,
        "luku2" : luku2,
        "summa" : summa
    }

    return vastaus

# http://127.0.0.1:3000/kaiku/huhuuu/3

@app.route('/kaiku/<teksti>/<kertaa>')
def kaiku(teksti, kertaa):
    print(teksti, kertaa)
    tulos = ""
    for i in range(int(kertaa)):
        tulos += teksti + ' '

    vastaus = {
        "kaiku": tulos
    }
    return vastaus

@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    try:
        luku1 = float(luku1)
        luku2 = float(luku2)
        summa = luku1 + luku2

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "luku1": luku1,
            "luku2": luku2,
            "summa": summa
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": "virhe.code",
        "teksti": "Virhe.description"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)