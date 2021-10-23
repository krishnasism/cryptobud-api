from flask import Flask,request
app = Flask(__name__)
from getcryptoprices import Crypto
@app.route('/')
def blank():
    return 'Were you trying to query something?'

@app.route('/getcryptoprice', methods=["GET"])
def getCryptoPrice():
    try:
        crypto = Crypto()
        crypto.getCryptoPrice
        sym = request.args.get("sym")
        price = crypto.getCryptoPrice(sym)
        return { sym : price }
    except Exception as e:
        return {"ERROR" : str(e) }

if __name__ == "__main__":
    app.run(host ="0.0.0.0", port = 8000) 
