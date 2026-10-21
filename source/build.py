"""Builds index.html (the whole map in one file) and the downloadable data in downloads/.

Run from the repository root:  python3 source/build.py
Inputs live in source/: template.html, records/*.json (one list of records per file),
records/tr/*.json (translations keyed by record id), geo/, terrain/, acled_strikes.json.
"""
import json, base64, os, glob, hashlib, csv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source")
REC = os.path.join(SRC, "records")
ARTIFACT_URL = "https://claude.ai/artifact/796jNHKRSBvtxbLDxMNCus"

def rid(d):
    return hashlib.sha1(f"{d['date']}|{d['place']}|{d['actor']}|{d['summary'][:60]}".encode()).hexdigest()[:10]

# records: every file in records/ except the extra-source lists
rows = []
for p in sorted(glob.glob(os.path.join(REC, "*.json"))):
    if os.path.basename(p) == "extra_sources.json":
        continue
    for d in json.load(open(p)):
        if "kind" not in d:
            d["kind"] = "eco" if d.get("record") == "ecocide" or "category" in d and "type" not in d else "strike"
        rows.append(d)

bad = [d for d in rows if not isinstance(d.get("lat"), (int, float)) or not isinstance(d.get("lon"), (int, float))]
for d in bad: print("no coords, skipped:", d.get("place"))
rows = [d for d in rows if d not in bad]

seen, unique = set(), []
for d in rows:
    d["lat"] = round(d["lat"], 3); d["lon"] = round(d["lon"], 3)
    d["date"] = str(d.get("date", ""))
    k = rid(d)
    if k in seen:
        continue
    seen.add(k); unique.append(d)
    d["uid"] = k
    if d["date"][:4].isdigit() and int(d["date"][:4]) < 2017: d["layer"] = "history"
    if d.get("kind") == "strike" and d.get("killed") == 0 and d.get("injured") == 0:
        d["nocas"] = True; d["civilian"] = None
rows = unique

tr = {}
for p in sorted(glob.glob(os.path.join(REC, "tr", "*.json"))):
    for k, v in json.load(open(p)).items(): tr.setdefault(k, {}).update(v)
extra = {}
ep = os.path.join(REC, "extra_sources.json")
if os.path.exists(ep):
    for e in json.load(open(ep)): extra.setdefault(e["id"], []).append(e)
for d in rows:
    for f, v in tr.get(d["uid"], {}).items():
        if v: d[f] = v
    for e in extra.get(d["uid"], []):
        if all(s.get("url") != e["url"] for s in d.get("sources", [])):
            d.setdefault("sources", []).append({"title": e["title"], "url": e["url"]})

for lang in ("ku", "tr", "ckb"):
    missing = [d["uid"] for d in rows if not d.get("summary_" + lang)]
    print(f"{lang}: {len(rows) - len(missing)}/{len(rows)} translated" + (f" (missing: {', '.join(missing[:10])})" if missing else ""))
print("records:", len(rows), "newest:", max(d["date"] for d in rows))

b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
geo = {k: json.load(open(os.path.join(SRC, "geo", k + ".json"))) for k in ("c0", "c1", "riv", "lak", "rd")}
read = lambda name: open(os.path.join(SRC, name)).read()

t = read("template.html")
t = t.replace("/*__LEAFLET_CSS__*/", read("leaflet.css"))
t = t.replace("/*__TOTALS__*/", read("totals.html"))
t = t.replace("<!--__ABOUT_CKB__-->", read("about_ckb.html"))
t = t.replace("/*__DATA__*/", json.dumps(rows, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
t = t.replace("/*__ACLED__*/", read("acled_strikes.json"))
t = t.replace("/*__RELIEF_GRAY__*/", b64(os.path.join(SRC, "terrain", "relief_gray.jpg")))
t = t.replace("/*__RELIEF_NAT__*/", b64(os.path.join(SRC, "terrain", "natural.jpg")))
t = t.replace("/*__GEO__*/", json.dumps(geo, separators=(",", ":")))
# share links point at wherever the page is hosted
t = t.replace(f'const BASE_URL = "{ARTIFACT_URL}";',
              f'const BASE_URL = location.protocol.startsWith("http") ? location.href.split("#")[0] : "{ARTIFACT_URL}";')
i = t.index('<div class="app">')
head = ('<!doctype html>\n<html lang="ku">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="theme-color" content="#0a0a0a">\n'
        '<meta name="description" content="Nexşeya êrîşên dewletan û ekosîdê li ser Kurdistanê · نەخشەی هێرشەکان بۆ سەر کوردستان · Kürdistan saldırı haritası · Map of state attacks and ecocide across Kurdistan">\n'
        '<style>html,body{margin:0}[hidden]{display:none!important}</style>\n')
open(os.path.join(ROOT, "index.html"), "w").write(head + t[:i] + "</head>\n<body>\n" + t[i:] + "\n</body>\n</html>\n")
print("index.html:", round(os.path.getsize(os.path.join(ROOT, "index.html")) / 1e6, 2), "MB")

# downloads
out = os.path.join(ROOT, "downloads"); os.makedirs(out, exist_ok=True)
part = {"Iraq": "Başûr", "Syria": "Rojava", "Turkey": "Bakur", "Iran": "Rojhilat"}
who = {"Iraq-PMF": "Iraqi state (PMF)", "US": "US", "Israel": "Israel", "US-Israel": "US and Israel", "Turkey": "Turkish state",
       "Iran": "Iranian state", "Syria": "Syrian state", "Iraq": "Iraqi state"}
cols = ["id", "date", "period", "part_of_kurdistan", "country", "governorate", "place", "place_ku", "place_ckb", "place_tr", "lat", "lon",
        "precision", "record_type", "attacker", "type_or_category", "killed", "injured", "civilians_harmed", "layer",
        "summary", "summary_ku", "summary_ckb", "summary_tr", "impact", "impact_ku", "impact_ckb", "impact_tr", "sources"]
with open(os.path.join(out, "kurdistan-strike-map-records.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for d in sorted(rows, key=lambda d: d["date"]):
        eco = d["kind"] == "eco"
        w.writerow({"id": d["uid"], "date": d["date"], "period": d.get("period", ""), "part_of_kurdistan": part.get(d["country"], ""),
            "country": d["country"], "governorate": d.get("governorate", ""), "place": d["place"], "place_ku": d.get("place_ku", ""),
            "place_ckb": d.get("place_ckb", ""), "place_tr": d.get("place_tr", ""), "lat": d["lat"], "lon": d["lon"],
            "precision": d.get("precision", ""), "record_type": "ecocide" if eco else "attack", "attacker": who.get(d.get("actor", ""), d.get("actor", "")),
            "type_or_category": d.get("category", "") if eco else d.get("type", ""),
            "killed": "" if d.get("killed") is None else d["killed"], "injured": "" if d.get("injured") is None else d["injured"],
            "civilians_harmed": "" if eco else {True: "yes", False: "no"}.get(d.get("civilian"), "unclear"),
            "layer": "history (before 2017)" if d.get("layer") == "history" else "",
            "summary": d["summary"], "summary_ku": d.get("summary_ku", ""), "summary_ckb": d.get("summary_ckb", ""), "summary_tr": d.get("summary_tr", ""),
            "impact": d.get("impact") or "", "impact_ku": d.get("impact_ku", ""), "impact_ckb": d.get("impact_ckb", ""), "impact_tr": d.get("impact_tr", ""),
            "sources": " | ".join(f'{s.get("title", "")} <{s.get("url", "")}>' for s in d.get("sources", []))})
print("downloads/kurdistan-strike-map-records.csv written")
