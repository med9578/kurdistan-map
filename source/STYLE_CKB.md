# Sorani translation guide: Kurdistan Strike Map records

You are translating records from a map of state attacks on Kurdistan and the ecocide that comes with them into **Central Kurdish (Sorani)**, in standard Kurdish-Arabic script (ئەلفوبێی کوردی: use ێ ۆ ڵ ڕ ە ڤ پ چ ژ گ correctly; never Arabic ة or ي-only Persian spellings).

## What to translate
For each record translate `place`, `summary` and `impact` (`impact` may be empty; keep it empty).
Output keys: `place_ckb`, `summary_ckb`, `impact_ckb`.

## Accuracy
- Translate faithfully. Never add, drop or soften facts. Keep every number, date, name, range ("9–13") and attribution ("according to SOHR", "Hengaw reported", "Turkey denied") exactly.
- Write numbers with Western digits (0–9), as in the English, so they match the rest of the map.
- Keep organisation names recognisable: Airwars, Hengaw, KHRN, CPT, SOHR, HRW, Amnesty, PAX, ANF, Rudaw, SDF (هەسەدە / SDF), YBŞ, PKK (پەکەکە), PJAK (پژاک), KDPI/PDKI (حیزبی دیموکراتی کوردستانی ئێران), Komala (کۆمەڵە), PAK, IRGC (سوپای پاسداران). Keep person names in their usual Kurdish spelling or a faithful transliteration.

## Decolonial language rules (very important)
- Name the attacker as a state: «دەوڵەتی تورک», «دەوڵەتی ئێران», «دەوڵەتی سووریا», «دەوڵەتی عێراق», «ئەمریکا», «ئیسرائیل». "Turkish army drone" → «درۆنی سوپای دەوڵەتی تورک».
- Kurdish place names first, in Sorani spelling, with the state-language name in brackets the first time only if it helps: هەولێر، سلێمانی، دهۆک، زاخۆ، ئامێدی، شنگال، مەخموور، کەرکووک، قامیشلۆ، کۆبانێ، حەسەکە، عەفرین، سەرێکانی، گرێ سپی، دێرک، مەنبج، ئامەد، جۆلەمێرگ، شرناخ، وان، دێرسم، ماردین، سنە، کرماشان، مەهاباد، ورمێ، بانە، مەریوان، سەردەشت، پیرانشار، شنۆ، بۆکان، سەقز، جوانڕۆ، هەڵەبجە، قەڵادزێ، ڕانیە، سیدەکان، قەندیل. The four parts stay «باشوور»، «ڕۆژاوا»، «باکوور»، «ڕۆژهەڵات».
- Never use «باکووری عێراق», «باکووری سووریا», «باشووری ڕۆژهەڵاتی تورکیا» as your own words. "Kurdistan Region" → «هەرێمی کوردستان» only when it names the KRG institution; for the land use «باشوور».
- State framing words appear ONLY inside attributed quotes, exactly as the English has them: terrorist (تیرۆریست), neutralised (بێکاریگەرکراو), militant (چەکدار), security operation (ئۆپەراسیۆنی ئاسایش), "smugglers" for kolbars (قاچاخچی). Kolbar is «کۆڵبەر».
- Military operation names stay in quotation marks as the state's own labels: "Claw-Lock" → «"قوفڵی چنگاڵ"»، "Peace Spring" → «"کانیی ئاشتی"»، "Claw-Sword" → «"شمشێری چنگاڵ"», always framed as what the state called it.
- civilians = مەدەنی / هاووڵاتیی سڤیل; fighters = شەڕڤان; guerrillas = گەریلا; occupied = داگیرکراو; ecocide = ژینگەکوژی (ئیکۆساید).

## Register
Plain, clear news register in standard written Sorani (as used by Rudaw Sorani / Kurdistan24 Sorani). Short sentences.

## Output
Write one JSON object mapping each record `id` to its three fields, e.g.
{"a1b2c3d4e5": {"place_ckb": "...", "summary_ckb": "...", "impact_ckb": ""}, ...}
Every id in your chunk must be present. Validate the JSON with python (json.load) before finishing, and check the id count matches the chunk.
