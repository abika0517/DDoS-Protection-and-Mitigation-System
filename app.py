from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from db import db, Settings, Blacklist, Whitelist 
from config import Config
from ddos_engine import detect_attack, request_counters
from state import alerts_list
 

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Init DB
with app.app_context():
    db.create_all()
    if not Settings.query.first():
        db.session.add(Settings(max_rps=100, sensitivity="medium", auto_block=False))
        db.session.commit()

def get_client_ip():
    if Config.MODE == "LOCAL":
        return "127.0.0.1"
    return request.remote_addr or "0.0.0.0"

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/settings", methods=["GET", "POST"])
def settings():
    s = Settings.query.first()
    if request.method == "POST":
        s.max_rps = int(request.form["max_rps"])
        s.sensitivity = request.form["sensitivity"]
        s.auto_block = ("auto_block" in request.form)
        db.session.commit()
        return redirect(url_for("settings"))
    return render_template("tuning.html", s=s)

@app.route("/blacklist", methods=["GET","POST"])
def blacklist():
    if request.method == "POST":
        ip = request.form["ip"]
        reason = request.form["reason"]
        db.session.add(Blacklist(ip=ip, reason=reason))
        db.session.commit()
        return redirect(url_for("blacklist"))
    return render_template("blacklist.html", bl=Blacklist.query.all())

@app.route("/blacklist/delete/<ip>")
def blacklist_delete(ip):
    Blacklist.query.filter_by(ip=ip).delete()
    db.session.commit()
    return redirect(url_for("blacklist"))

@app.route("/whitelist", methods=["GET","POST"])
def whitelist():
    if request.method == "POST":
        ip = request.form["ip"]
        purpose = request.form["purpose"]
        db.session.add(Whitelist(ip=ip, purpose=purpose))
        db.session.commit()
        return redirect(url_for("whitelist"))
    return render_template("whitelist.html", wl=Whitelist.query.all())

@app.route("/whitelist/delete/<ip>")
def whitelist_delete(ip):
    Whitelist.query.filter_by(ip=ip).delete()
    db.session.commit()
    return redirect(url_for("whitelist"))

@app.route("/simulate", methods=["POST"])
def simulate():
    ip = get_client_ip()
    blocked = detect_attack(ip)
    return jsonify({"ip": ip, "blocked": blocked})

# ---------- STATS API ----------
@app.route("/stats")
def stats():
    total = sum(sum(v.values()) for v in request_counters.values())

    # Active = IPs that exceeded threshold (detected earlier)
    from state import alerts_list
    active = len(alerts_list)

    blocked = Blacklist.query.count()
    whitelisted = Whitelist.query.count()

    return jsonify({
        "total": total,
        "active": active,
        "blocked": blocked,
        "whitelisted": whitelisted
    })


# ---------- CONNECTIONS API ----------
@app.route("/connections")
def connections():
    data = []
    for ip, timestamps in request_counters.items():
        latest_time = list(timestamps.keys())[-1]
        req = timestamps[latest_time]
        data.append({
            "ip": ip,
            "rps": req,
            "last": latest_time
        })
    return jsonify(data)

# ---------- ALERTS API ----------

@app.route("/alerts")
def get_alerts():
    from state import alerts_list
    return jsonify(alerts_list)

@app.route("/chart-data")
def chart_data():
    from ddos_engine import request_counters
    # Convert per-second data into simple time-series
    series = {}
    for ip, ts in request_counters.items():
        for t, count in ts.items():
            series[t] = series.get(t, 0) + count

    # Sort times
    labels = sorted(series.keys())
    values = [series[t] for t in labels]

    return jsonify({"labels": labels, "values": values})



if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
