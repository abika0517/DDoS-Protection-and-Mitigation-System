from db import db, Settings, Blacklist, Whitelist
from datetime import datetime
from state import alerts_list   # <-- WE IMPORT ALERTS HERE

request_counters = {}

def detect_attack(ip):
    settings = Settings.query.first()
    if not settings:
        return False

    max_rps = settings.max_rps
    mul = {"low": 2, "medium": 1, "high": 0.5}.get(settings.sensitivity, 1)
    max_limit = max_rps * mul

    # Skip whitelisted
    if Whitelist.query.filter_by(ip=ip).first():
        return False

    # Instantly block blacklisted
    if Blacklist.query.filter_by(ip=ip).first():
        return True

    # Count requests per second
    now = datetime.now().strftime("%H:%M:%S")
    if ip not in request_counters:
        request_counters[ip] = {}
    if now not in request_counters[ip]:
        request_counters[ip][now] = 0

    request_counters[ip][now] += 1

    # This is where attack is detected
    if request_counters[ip][now] > max_limit:

        # ---- STEP 2: ADD ALERT HERE ----
        alerts_list.append(f"{datetime.now().strftime('%H:%M:%S')} - ALERT: {ip} exceeded threshold!")

        # Auto-block if enabled
        if settings.auto_block:
            db.session.merge(Blacklist(ip=ip, reason="Auto-Blocked"))
            db.session.commit()

        return True

    return False
