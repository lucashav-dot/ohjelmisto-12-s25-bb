from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n is None:
        return False
    try:
        n = int(n)
    except ValueError:
        return False

    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

@app.route('/alkuluku/<number>', methods=['GET'])
def check_prime(number):
    number_int = None
    is_prime_result = False

    try:
        number_int = int(number)
        is_prime_result = is_prime(number_int)
    except ValueError:
        pass

    response_data = {
        "Number": number_int if number_int is not None else number,
        "isPrime": is_prime_result
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)