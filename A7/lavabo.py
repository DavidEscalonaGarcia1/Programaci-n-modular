import time
from datetime import datetime, time as dtime, timedelta

# intervals per anar al lavabo
intervals = [
    (dtime(8,30), dtime(8,50)),
    (dtime(9,10), dtime(9,50)),
    (dtime(11,0), dtime(11,30)),
    (dtime(12,40), dtime(13,20)),
    (dtime(13,40), dtime(14,0)),
]

def seconds_to_text(seconds):
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"

def check_status():
    now = datetime.now()
    now_time = now.time()

    for start, end in intervals:
        start_dt = datetime.combine(now.date(), start)
        end_dt = datetime.combine(now.date(), end)

        if start <= now_time <= end:
            remaining = int((end_dt - now).total_seconds())
            return True, remaining

        if now_time < start:
            remaining = int((start_dt - now).total_seconds())
            return False, remaining

    # si ja han passat tots els intervals
    next_start = datetime.combine(now.date() + timedelta(days=1), intervals[0][0])
    remaining = int((next_start - now).total_seconds())
    return False, remaining

def generate_html(can_go, remaining):
    text = "SI" if can_go else "NO"
    color = "green" if can_go else "red"
    message = (
        f"Falten {seconds_to_text(remaining)} per deixar d'anar al lavabo"
        if can_go
        else f"Falten {seconds_to_text(remaining)} per poder anar al lavabo"
    )

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Puc anar al lavabo?</title>
<style>
body {{
    background:{color};
    color:white;
    font-family:Arial, sans-serif;
    text-align:center;
}}
h1 {{
    font-size:20vw;
    margin-top:15vh;
}}
p {{
    font-size:3vw;
}}
</style>

<script>
// auto refresh cada segon
setTimeout(() => {{
    location.reload();
}}, 1000);
</script>

</head>
<body>
<h1>{text}</h1>
<p>{message}</p>
</body>
</html>
"""
    return html

print("Actualitzant index.html... (Ctrl+C per sortir)")

try:
    while True:
        can_go, remaining = check_status()
        html = generate_html(can_go, remaining)

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

        time.sleep(1)  # màxim 1 actualització per segon

except KeyboardInterrupt:
    print("\nAturat.")