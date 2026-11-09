# Updating the map

Everything on the map is built from the files in `source/`. Never edit `index.html` by hand; edit the records and run the build.

```
python3 source/build.py
```

This rewrites `index.html` (the whole map in one file) and `downloads/kurdistan-strike-map-records.csv`. Commit both. GitHub Pages publishes the new map within a couple of minutes.

## Adding new attacks

1. **Find events.** The map covers **any attack on Kurdish people, groups, land or anything Kurdish, by anyone, anywhere**: state military attacks, kolbars shot or beaten at borders, executions, deaths or abuse in custody, violent raids, attacks by mobs and armed groups, attacks on graves and property, and ecocide. Plain arrests without violence are not mapped. Check these sources since the newest date on the map (the build prints it):
   - **Main:** ANF (English, Kurmancî, Türkçe), Nûçe TV, Sterk TV, Rudaw, Kurdistan24, Shafaq News, The New Region, Hengaw, Kurdistan Human Rights Network (KHRN), Community Peacemaker Teams (CPT), Rojava Information Center, North Press, Hawar News, Kolbernews, SOHR.
   - **Rojhilat and kolbars:** Kurdpa ([kolbars](https://kurdpa.net/human-rights/kolbars), [environment](https://kurdpa.net/focus-areas/environment), [monthly reports](https://kurdpa.net/statistics-documents/monthly-reports); trust the date in the URL, the page shows the Kurdish calendar).
   - **Başûr and Rojhilat, daily:** Rojnews ([Kurdistan](https://rojnews.news/?cat=62), [environment](https://rojnews.news/?cat=69)); close to the PKK media network, like ANF.
   - **Bakur ecocide:** Mezopotamya Agency ([Ekoloji](https://mezopotamyaajansi.com/EKOLOJI), [Kurmancî](https://mezopotamyaajansi.com/kr/EKOLOJI), [English](https://mezopotamyaajansi.com/en)), JINNEWS ([ekoloji](https://jinnews.net/kategori/ekoloji)), Yeni Yaşam, Yeni Özgür Politika (mostly reprints), Bianet.
   - **Şingal and the disputed areas:** KirkukNow ([reports](https://www.kirkuknow.com/en/news?category=3)).
   - **Field data:** CPT Iraqi Kurdistan ([cptik.org/data](https://cptik.org/data)), updated every few months.
   - **Soranî cross-checks:** Awene, Channel8.
   - **Party sources** (use as leads, and say so in the record): PDKI's Kurdistanmedia, Komala.
   - Blocked or gone when last checked: BasNews, Esta, HRANA, Iran Human Rights, Enab Baladi, Medya News, the KRG site, Draw Media, Peyamner, NRT.
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
   - `actor`: `Turkey`, `Iran`, `Syria`, `Iraq`, `Iraq-PMF`, `US`, `Israel`, `US-Israel`, or `Other` for anyone else (armed groups, mobs, unknown attackers, other states). With `Other`, the summary must say who the source says the attackers were.
   - `country` is the state whose borders the place is in: `Iraq`, `Syria`, `Turkey` or `Iran`.
   - Attack `type`: `drone`, `airstrike`, `missile`, `artillery`, `ground assault`, `border shooting`, `chemical`, `massacre`, `campaign`, `execution`, `custody death` (death or abuse in custody), `raid` (violent house raid or arrest), `mob attack` (mob or armed group), `property attack` (graves, homes, property).
   - `country` can be another country for attacks on Kurds abroad (for example `Austria`).
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
- Kurdistan is one land. Never divide it into parts: do not use Başûr, Bakur, Rojava or Rojhilat as region names, and never write "northern Iraq", "northern Syria", "southeast Turkey" or "Iraqi/Syrian/Iranian Kurdistan" in the map's own voice. Say "Kurdistan", use Kurdish city and province names, and where the border itself matters name it as a state border ("the Iraqi–Iranian state border").
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
