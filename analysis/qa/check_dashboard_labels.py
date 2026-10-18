"""Confirm that dashboard.html differs from a reference commit only in visible text labels.

Parses the SPEC object from both versions and lists every changed path. The check fails if
anything outside visual titles, field display names or textbox runs changed: table data,
measure definitions, relationships, measure references and the JavaScript are compared too.

Usage: python analysis/qa/check_dashboard_labels.py [reference-commit]   (default 94df245)
"""
import json
import subprocess
import sys

REF = sys.argv[1] if len(sys.argv) > 1 else "94df245"
LABEL_KEYS = {"title", "name", "v"}  # visual title, field display name, textbox run text


def split(html):
    lines = html.split("\n")
    idx = next(i for i, l in enumerate(lines) if l.startswith("var SPEC = "))
    spec = json.loads(lines[idx][len("var SPEC = "):].rstrip().rstrip(";"))
    rest = "\n".join(lines[:idx] + lines[idx + 1:])
    return spec, rest


def walk(a, b, path, out):
    if type(a) is not type(b):
        out.append((path, a, b))
    elif isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            walk(a.get(k), b.get(k), path + [k], out)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append((path, "len %d" % len(a), "len %d" % len(b)))
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, path + [i], out)
    elif a != b:
        out.append((path, a, b))


old = subprocess.run(["git", "show", REF + ":dashboard.html"], capture_output=True, check=True).stdout.decode("utf-8")
new = open("dashboard.html", encoding="utf-8").read()
old_spec, old_rest = split(old)
new_spec, new_rest = split(new)

problems = []
if old_rest != new_rest:
    problems.append("HTML/CSS/JavaScript outside the SPEC line changed")

diffs = []
walk(old_spec, new_spec, [], diffs)
for path, a, b in diffs:
    where = path[0]
    label = path[-1] in LABEL_KEYS and where == "pages"
    # a field display name must not be a measure reference or column name
    if label and path[-1] == "name" and "roles" not in path:
        label = False
    print("%s %s\n    - %r\n    + %r" % ("LABEL" if label else "NOT A LABEL", "/".join(map(str, path)), a, b))
    if not label:
        problems.append("/".join(map(str, path)))

print("\n%d changed fields against %s" % (len(diffs), REF))
if problems:
    print("FAIL: " + "; ".join(problems))
    sys.exit(1)
print("PASS: only visible text labels changed; data, measures, relationships and code are identical")
