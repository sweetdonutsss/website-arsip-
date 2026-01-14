from flask import Flask, render_template, request, jsonify
from data import data_perusahaan

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    keyword = ""

    if request.method == "POST":
        keyword = request.form.get("keyword", "")
        hasil = {
            k: v for k, v in data_perusahaan.items()
            if keyword.lower() in k.lower()
        }

    return render_template("index.html", hasil=hasil, keyword=keyword)


@app.route("/perusahaan/<nama>")
def detail(nama):
    perusahaan = data_perusahaan.get(nama)
    return render_template("detail.html", nama=nama, perusahaan=perusahaan)


@app.route("/autocomplete")
def autocomplete():
    q = request.args.get("q", "").lower()
    hasil = [k for k in data_perusahaan.keys() if q in k.lower()]
    return jsonify(hasil)


# ✅ WAJIB UNTUK JALAN DI LOKAL
if __name__ == "__main__":
    app.run(debug=True)
