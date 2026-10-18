"""Trace every number shown in pitch.html (slides and presenter notes) to web.html or dashboard.html.

Rule R1: a figure on a new page must already appear in web.html or dashboard.html, or be computed
by a committed script. This script extracts each numeric token from pitch.html's visible text,
looks for it in the text of the two source pages (allowing 0.80 = 0.8, - = minus sign, and
thousands separators), and lists anything it cannot find. Those are explained in EXPLAINED below
or must be fixed.

Usage: python analysis/qa/check_pitch_figures.py
"""
import html
import re
import sys

# Numbers that are not data from the sources, with the reason they are allowed.
EXPLAINED = {
    "2027/28": "pilot season, shifted one season per the team brief (2026/27 is now a desk dry-run)",
    "2028/29": "four-district season, shifted one season per the team brief",
    "2029/30": "wider-adoption start, shifted one season per the team brief",
    "1": "ordinal (slide numbers, list numbering, key names)",
    "2": "ordinal (slide numbers, list numbering)",
    "4": "ordinal / key name",
    "5": "ordinal / key name",
    "6": "ordinal / key name",
    "9": "ordinal (slide count, key names 1-9)",
}


def visible_text(page):
    page = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", " ", page)
    page = re.sub(r"(?s)<svg.*?</svg>", lambda m: " ".join(re.findall(r">([^<]+)<", m.group(0))), page)
    page = re.sub(r"<[^>]+>", " ", page)
    return html.unescape(page)


def dashboard_text(page):
    # the SPEC JSON holds titles, textbox runs and every table value
    return page


def variants(tok):
    t = tok.replace("−", "-")
    out = {t, t.replace(",", "")}
    for x in list(out):
        if re.fullmatch(r"-?\d+\.\d*?0+", x):
            out.add(x.rstrip("0").rstrip("."))
        out.add(x.lstrip("-"))
    return {v for v in out if v}


pitch = visible_text(open("pitch.html", encoding="utf-8").read())
web = visible_text(open("web.html", encoding="utf-8").read())
dash = dashboard_text(open("dashboard.html", encoding="utf-8").read())
corpus = (web + " " + dash).replace("−", "-")
corpus_nocomma = corpus.replace(",", "")

tokens = sorted(set(re.findall(r"\d{4}/\d{2}|\d{4}-\d{2}-\d{2}|[−-]?\d[\d,]*(?:\.\d+)?%?", pitch)))
missing, explained = [], []
for tok in tokens:
    if tok in EXPLAINED or tok.lstrip("−-") in EXPLAINED:
        explained.append(tok)
        continue
    found = False
    for v in variants(tok):
        pat = r"(?<![\d.])" + re.escape(v) + r"(?![\d])"
        if re.search(pat, corpus) or re.search(pat, corpus_nocomma):
            found = True
            break
    if not found:
        missing.append(tok)

print("%d distinct numeric tokens in pitch.html" % len(tokens))
for tok in explained:
    key = tok if tok in EXPLAINED else tok.lstrip("−-")
    print("  explained  %-10s %s" % (tok, EXPLAINED[key]))
if missing:
    print("NOT FOUND in web.html or dashboard.html: " + ", ".join(missing))
    sys.exit(1)
print("PASS: every other number in pitch.html appears in web.html or dashboard.html")
