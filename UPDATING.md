# Updating the map

Everything on the map is built from the files in `source/`. Never edit `index.html` by hand; edit the records and run the build.

```
python3 source/build.py
```

This rewrites `index.html` (the whole map in one file) and `downloads/kurdistan-strike-map-records.csv`. Commit both. GitHub Pages publishes the new map within a couple of minutes.

## Adding new attacks

1. **Find events.** Check these sources for state attacks on any part of Kurdistan and for state-caused ecocide since the newest date on the map (the build prints it):
   ANF (English, Kurmancî, Türkçe), Nûçe TV, Sterk TV, Rudaw, Kurdistan24, Hengaw, Kurdistan Human Rights Network (KHRN), Community Peacemaker Teams (CPT), Rojava Information Center, North Press, Kolbernews, SOHR.
   Do not get around paywalls or bot blocks.
2. **Skip duplicates.** An event already on the map with the same date (±1 day) and place is a duplicate. Add the new source to it instead (`source/records/extra_sources.json`, with the record's `id`).
3. **Write the records** into a new file `source/records/YYYY-MM-DD.json` (the date you add them), as a JSON list:

```json
{"record": "attack", "date": "2026-08-19", "actor": "Iran", "type": "border shooting",
 "place": "Perdespiyan border line, Serdeşt (Sardasht)", "governorate": "West Azerbaijan", "country": "Iran",
 "lat": 36.15, "lon": 45.48, "precision": "approximate", "killed": 1, "injured": null, "civilian": true, "impact": null,
 "summary": "Nûçe TV, citing Kolber News, reported that Iranian state forces fired on kolbers on the Perdespiyan border line of Serdeşt, killing Yûsif Mamepûr, 30, from Werdê village.",
 "sources": [{"title": "Nûçe TV: Îranê kolbereke Kurd kuşt", "url": "https://nucetv.net/irane-kolbereke-kurd-kust"}]}
```

   - `record`: `attack` or `ecocide`.
   - `actor`: `Turkey`, `Iran`, `Syria`, `Iraq`, `US`, `Israel` or `US-Israel`.
   - `country` is the state whose borders the place is in: `Iraq` (Başûr), `Syria` (Rojava), `Turkey` (Bakur), `Iran` (Rojhilat).
   - Attack `type`: `drone`, `airstrike`, `missile`, `artillery`, `ground assault`, `border shooting`, `chemical`, `massacre`, `campaign`.
   - Ecocide uses `category` instead: `forest fire`, `deforestation`, `agriculture`, `water`, `infrastructure`, `dam`, `land`.
   - `killed`/`injured`: numbers, or `null` if unknown. `civilian`: `true` only if a source says civilians were harmed; `false`, or `null` if unclear.
   - `precision`: `exact` for a known village or site, `approximate` otherwise.
   - Every record needs at least one source link that was actually opened.

4. **Translate.** Each record's id is `sha1("{date}|{place}|{actor}|{summary[:60]}")[:10]` (see `rid()` in `build.py`). Add translations in two new files in `source/records/tr/`:
   - `YYYY-MM-DD_ku_tr.json`: `{id: {place_ku, summary_ku, impact_ku, place_tr, summary_tr, impact_tr}}`, following `source/STYLE.md`.
   - `YYYY-MM-DD_ckb.json`: `{id: {place_ckb, summary_ckb, impact_ckb}}`, following `source/STYLE_CKB.md`.
   The build lists any record missing a translation.
5. **Build, check, commit.** Run the build. Confirm it reports every record translated in all languages. Then commit `source/`, `index.html` and `downloads/`.

## Language rules (all languages)

- Kurdish place names first, with the state's name in brackets: Hewlêr (Erbil), Amed (Diyarbakır), Sine (Sanandaj).
- Name attackers as states: "the Turkish state", "Iranian state forces".
- Never write "northern Iraq", "northern Syria" or "southeast Turkey" in the map's own voice; say Başûr, Rojava, Bakur, Rojhilat.
- Use "terrorist", "militant", "neutralised" or "security operation" only inside a quote, saying whose words they are.
- Kolbars are kolbars, not smugglers.
- Military operation names go in quotes as the state's own label.
- Only call people civilians when a source does. Give ranges where sources disagree. If the state denies an attack or the attacker is disputed, say so.

## Files

| Path | What it is |
|---|---|
| `source/records/*.json` | The records, one list per file |
| `source/records/tr/*.json` | Translations, keyed by record id |
| `source/records/extra_sources.json` | Extra source links attached to existing records |
| `source/template.html` | The map's page, styles and code |
| `source/acled_strikes.json` | ACLED weekly province totals (the dashed circles) |
| `source/geo/`, `source/terrain/` | Base map and terrain shading |
| `source/about_ckb.html`, `source/totals.html` | Sorani and English "About" text |
| `downloads/` | The dataset as CSV, rebuilt each time |
