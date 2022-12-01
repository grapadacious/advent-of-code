def snake_to_caps(s):
    return " ".join(s.split("_")).upper()

def ns_to_human(t):
    t = t / 1_000_000
    unit = "ms"

    if t > 500:
        t = t / 1_000
        unit = "s"

    return f"{round(t, 2)}{unit}"
