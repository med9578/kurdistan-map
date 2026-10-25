# Translation guide: Kurdistan Strike Map records

You are translating records from a map of state attacks on Kurdistan and the ecocide that comes with them. Every record must exist in Kurmanji (Latin script, Hawar alphabet) and in Turkish.

## What to translate
For each record, translate three fields: `place`, `summary` and `impact` (`impact` may be empty; keep it empty).
Output keys: `place_ku`, `summary_ku`, `impact_ku`, `place_tr`, `summary_tr`, `impact_tr`.

## Accuracy
- Translate faithfully. Never add, drop or soften facts. Keep every number, date, name, range ("9–13"), and attribution ("according to SOHR", "Hengaw reported", "Turkey denied") exactly.
- Keep organisation names as they are (Airwars, Hengaw, KHRN, CPT, SOHR, HRW, Amnesty, PAX, SDF, YBS, PKK, PJAK, KDPI/PDKI, Komala, PAK, IRGC; in Kurmanji you may write SPA, in Turkish you may write DSG for SDF, but keep the English acronym in brackets the first time if you change it). Keep quoted state claims as quotes.
- Keep person names in their original spelling.

## Decolonial language rules (very important)
- Name the attacker as a state: Kurmanji "dewleta Tirk", "dewleta Îranê", "dewleta Sûriyeyê", "dewleta Iraqê", "DYA", "Îsraîl"; Turkish "Türk devleti", "İran devleti", "Suriye devleti", "Irak devleti", "ABD", "İsrail". "Turkish army drone" → "SÎHA ya artêşa Tirk" / "Türk ordusuna ait SİHA".
- Kurdish place names come first. Use the Kurdish name where the English text gives one or where a common Kurdish name exists, with the state-language name in brackets the first time if it helps: Hewlêr (Erbil), Silêmanî (Süleymaniye/Sulaymaniyah), Duhok, Zaxo, Amêdî, Şengal (Sincar/Sinjar), Mexmûr, Kerkûk, Qamişlo, Kobanê, Hesekê, Efrîn, Serêkaniyê, Girê Spî, Dêrik, Til Temir, Minbic, Amed (Diyarbakır), Colemêrg (Hakkari), Şirnex (Şırnak), Wan (Van), Dersim (Tunceli), Mêrdîn (Mardin), Sine (Senendec/Sanandaj), Kirmaşan (Kermanşah), Mehabad, Ûrmiye (Urmiye), Bane, Merîwan, Serdeşt, Pîranşar, Şino, Bokan, Seqiz, Cwanro. Kurdistan is one land: never divide it into parts. Do not use Başûr, Bakur, Rojava or Rojhilat as region names (directions such as "rojhilatê Mûsilê", east of Mosul, are fine, and so are organisation names like Rojava Information Center). Use "Kurdistan" or Kurdish city and province names; where the border itself matters, name it as a state border (e.g. "the Iraqi–Iranian state border"). Kurmanji: Kurdistan / Kurdistanê, "sînorê dewletên Iraq û Îranê"; Turkish: Kürdistan, "Irak–İran devlet sınırı".
- Never use "Kuzey Irak", "Kuzey Suriye", "Güneydoğu" (Turkish) or "Bakurê Iraqê"/"Bakurê Sûriyeyê" (Kurmanji) as your own words. "Kurdistan Region" → Kurmanji "Herêma Kurdistanê" / Turkish "Kürdistan Bölgesi" only when it names the KRG institution; for the land use "Kurdistan" (Kurmanji "Kurdistan", Turkish "Kürdistan").
- State framing words appear ONLY inside attributed quotes, exactly as the English record has them: terrorist (terorîst / terörist), neutralised (bêbandor kirin / etkisiz hale getirme), militant, security operation, regime used as a slur, "smugglers" for kolbars. Kolbar stays "kolber" (Kurmanji) and "kolber" (Turkish).
- Military operation names stay in quotation marks as the state's own labels: "Peace Spring" → Kurmanji "Kaniya Aştiyê" ('Peace Spring'), Turkish "Barış Pınarı"; "Claw-Lock" → "Pençe-Kilit"; "Claw-Sword" → "Pençe-Kılıç"; "Claw-Eagle" → "Pençe-Kartal"; "Claw-Tiger" → "Pençe-Kaplan"; "Claw-Lightning"/"Claw-Thunderbolt" → "Pençe-Şimşek"/"Pençe-Yıldırım". Always in quotes and framed as what the state named it.
- "civilians" = sivîl (Kurmanji) / sivil (Turkish). "fighters" = şervan / savaşçı. "guerrillas" = gerîla / gerilla. "occupied" = dagirkirî / işgal altındaki.
- Ecocide = ekosîd (Kurmanji) / ekokırım (Turkish).

## Register
Plain, clear news register. Short sentences. Kurmanji: standard written Kurmanji (as used by ANF Kurmancî / Rûdaw Kurmancî), correct ezafe and case endings. Turkish: standard written Turkish (as used by bianet / Mezopotamya Ajansı).

## Output
Write a single JSON object mapping each record `id` to its six fields, e.g.
{"a1b2c3d4e5": {"place_ku": "...", "summary_ku": "...", "impact_ku": "", "place_tr": "...", "summary_tr": "...", "impact_tr": ""}, ...}
Every id in your chunk must be present. Validate the JSON with python before finishing.
