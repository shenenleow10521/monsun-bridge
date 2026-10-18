# Pitch changes, 18 Oct 2026

Everything changed for the final-round pitch, so the team can mirror the dashboard label edits in the `.pbix` and check the new pitch page before 19 Oct.

`web.html` and `index.html` are unchanged. `dashboard.html` changed only in visible text labels: `python analysis/qa/check_dashboard_labels.py` parses the data model before and after and confirms that the tables, measures, relationships and JavaScript are identical.

## 1. Files

| File | Status | What it is |
|---|---|---|
| `pitch.html` | new | A 9-step presenter page you step through with the keyboard. It uses web.html's colours, fonts, components, map polygons and images, and loads nothing from the internet. |
| `dashboard.html` | text labels only | 17 label fields on pages 00, 01, 02, 05 and 07 (section 3). |
| `analysis/qa/check_dashboard_labels.py` | new | Proves the dashboard diff is labels only (prints PASS or FAIL). |
| `analysis/qa/check_pitch_figures.py` | new | Traces every number in pitch.html (slides and notes) to web.html or dashboard.html (rule R1). |
| `analysis/qa/gate_wilson_check.py` | new | Checks a possible reason for the 43/100 gate (see QA_NOTES card 2). |
| `CHANGES_PITCH.md`, `QA_NOTES.md` | new | This file and the judge Q&A cards. |

Run all three checks from the repo root with Python 3 (standard library only).

## 2. pitch.html

### Keys

| Key | Action |
|---|---|
| → · Space · PageDown · ↓ | next step |
| ← · PageUp · ↑ | previous step |
| Home | back to step 1 and reset the timer |
| 1 to 9 | jump to a step (useful in Q&A) |
| F | full screen |
| N | presenter notes (the slide shrinks to fit above them) |
| T | show or hide the elapsed timer. It starts on your first → or on T, turns amber at 8:00 and red at 10:00, and shows when the current step should end. |
| ? | key help |

Step 4 shows the real `dashboard.html` at full resolution in a layer that nearly fills the screen. The layer has a large **⤢ Full screen** button, buttons for dashboard pages 00 to 07, and ◂ ▸ buttons to move between slides.

- **Keyboard inside the dashboard.** Click inside it and ← → change dashboard pages, using the dashboard's own keys. A pill says when the dashboard has the keys. Click the dark bar above the dashboard to give them back to the slides.
- **Opening from a file (file://).** When pitch.html is opened by double-click, the page buttons reload the dashboard on the chosen page, which resets its slicers. Over a local server (`python -m http.server`) they switch pages instantly and keep slicer state.

### Step plan (7:50 in total; the bell rings at 8:00)

| # | Step | Time | Window | What the judges see (source) |
|---|---|---|---|---|
| 1 | Hook | 0:40 | 0:00 to 0:40 | Animated east-coast map with wind field and pulsing islands. Lead number: east-coast landings 0.639 vs 0.977 west-coast control, a −35.4% gap. METMalaysia's 133-day window. Live countdown and month strip. The team in one line. (web.html hero, 04, 06b) |
| 2 | Who is exposed | 0:40 | to 1:20 | Pilot map, and the 01b district table with a worker-month bar in each row (Besut in gold). Callouts: 41% in Besut, 0.392% of national tourism jobs. (web.html 01b, 04) |
| 3 | Trust | 0:35 | to 1:55 | Four big numbers (118, 7, 3, 0). An "evidence ladder" of four coloured blocks from measured to assumed: 133 days, −35.4%, 13,703, RM 887. (web.html 03, 04) |
| 4 | Live demo | 2:10 | to 4:05 | dashboard.html at full resolution. The demo-path page buttons (00, 02, 03, 04, 06) are outlined in gold. |
| 5 | Skill Bridge | 0:50 | to 4:55 | Ranking bars, with excluded fishing jobs hatched red and marked "→ 0 allocation". Before/after bars for the seasonal exclusion (28% to fishing, then 0). Score waterfall ("explainable by construction"), with seasonal fit hatched as an analyst setting. Two short honesty notes. (web.html 05b, 05c, 06b, 08; dashboard Transition, SkillEvidence and P3) |
| 6 | Fishing test | 0:40 | to 5:35 | Dumbbell chart 0.639 vs 0.977, −35.4%, 95% CI. Seasonal profile chart. A "p-value ladder": four two-sided tests as dots on a log scale against the 1% level, with the headline p = 0.0083 emphasised and the failing coast-pair test in red. (web.html 06, 06b) |
| 7 | Cost | 0:45 | to 6:20 | Cost equation: stacked RM 1,100 + 1,320 + 242 bar = RM 2,662 ÷ 3 = RM 887. Default-scenario numbers, and a coverage bar (8,223 of 52,655, about 16%). Break-even placement bars against a one-third line. RM 315.5M marked as an upper bound. (web.html 07) |
| 8 | Where ML earns its place | 0:50 | to 7:10 | Six visual cards in pipeline order: (1) verified-data flow 7 → 3 → 118 → 0; (2) mini TF-IDF similarity heatmap (5 × 8, from web.html 05a); (3) mini ranking with fishing marked ✕; (4) nowcast bars 0.731 ✓ vs 1.050 ✗ against the naive line; (5) stress-test bars 0 / 0 / 4 of 20; (6) the two maps. Then a dashed PROPOSED band, "not built yet", with 4 items. (web.html 03, 05a, 05b, 08; dashboard P3, P7) |
| 9 | Rollout and ask | 0:40 | to 7:50 | Four-stage timeline with gates (pilot gate wording exact). Dark "Our ask of DOSM" band with three asks. SDG 8 and SDG 14 badges. (web.html 02b, 10, 11; dashboard P7) |

Removed compared with web.html: every collapsible details block, the advisor and team cards (the team is one line on step 1), the TAM/SAM/SOM section, and the closing statistics. Each slide now shows 50 to 150 words, most of them chart labels; all explanation is in the presenter notes (N).

### How the slides map to the judging criteria

| Criterion (weight) | Where it is earned |
|---|---|
| C1 Presentation (20%) | A story arc carried by the headlines: problem (1) → who (2) → why trust it (3) → see it live (4) → the bridge (5) → why not fishing (6) → what it costs (7) → how ML is used (8) → plan and ask (9). One visual idea per slide, timed notes, and a timer that turns amber at the 8:00 bell. |
| C2 Live dashboard demo (25%) | Step 4: the real dashboard at near full screen, a big full-screen button, gold-outlined demo path, and a timed click script in the notes. Slides 5 to 7 repeat the key numbers in case the demo fails. |
| C3 Analysis (20%) | Control-group design and CI (6), four tests including the failing one (6), exact score decomposition (5), the weakest input named on the slide (5), stress test (8), pre-season forecast not claimed (8), and Modelled/Scenario grades on every estimate. |
| C4 Impact and feasibility (25%) | Exposure and pilot targeting (2), unit cost, coverage and break-even placement rate (7), a gated rollout that starts with a dry-run this season (9), a concrete ask of DOSM (9), SDG 8 and 14 (6, 9). |
| C5 Creativity, AI/ML, geospatial, automation (10%) | Step 8 shows all four (NLP matching, multi-criteria ranking, time-series nowcast, robustness, maps, checksummed pipeline). The explainable-AI framing is on step 5, the animated geospatial hero on step 1, and the proposed LLM/embedding roadmap is labelled as not built. |

### Design polish (impeccable skill, v4.6.0 rules)

Applied from the skill's polish playbook and craft-floor rules (pbakaus/impeccable, read from its public repo). The skill's launcher binary was not run; its written guidance was applied by hand.

- **No eyebrows or section numbers above headlines.** The "02 Who is exposed"-style kickers are gone; each headline carries the slide. "DOSM Datathon 2026 final" moved into the team line, and "Proposed, subject to partner agreement" moved below the timeline as a note.
- **No thick coloured side borders on callouts.** Colour now lives in the words (the 41% in gold, the "Weakest input" lead-in in Scenario purple). Gates use a 1px rule.
- **Slide 8 is an open grid** with 2px top rules instead of six boxed cards, and no tag labels.
- **Slide 3's four stat tiles** became one typographic line.
- **Authored SVG icons** (chevrons, expand, check, cross) replace the ◂ ▸ ⤢ ✓ ✗ ✕ glyphs.
- **No zero-offset glow halos** on the month strip, the headline p-value dot or the full-screen button.
- **One authored motion moment.** The hero title rise, wind field and island pulses stay; every chart renders in its final state, and slides cross-fade with an exponential ease-out.
- **Contrast.** Text colours were darkened slightly so all small text passes 4.5:1 on the paper background: ink3 #56687A, storm #B5301F, obs #17773F, der #106E95, mod #A84A0C, goldd #8A5E08 (each about 5.1:1 or better).
- **Browser surfaces.** Themed text selection, a gold focus ring and a themed notes scrollbar.
- **Measure.** Prose lines are capped at about 70 characters.
- **Intentional exception.** The hero wordmark stays at 170px, above the skill's 6rem display cap, because it is web.html's own identity.

### Consistency rules applied (Task 2)

| Rule | In pitch.html | In dashboard.html |
|---|---|---|
| (a) The islands never "close" | "Island operators suspend, boat services stop", and the table header is "Island where boat services stop". The hook notes warn the presenter. | P01 subtitle, the P01 ledger note and the P07 negative-result note reworded (section 3). |
| (b) No "pays for itself" or "returns what it costs" | Step 7 heading reads "Break-even placement rate (participant earnings = programme cost)". | P00 subtitle and claim 4, P05 subtitle and the P05 break-even chart title. |
| (c) The p = 0.0025 tile | Step 6 lists it as "2023 per-state Mann-Whitney"; the headline stays p = 0.0083 (permutation). | The P00 and P07 tiles are renamed "2023 per-state Mann-Whitney test"; the value is unchanged. |
| (d) RM 315.5M | "RM 315.5M, is an upper bound: it assumes one tourism-linked worker per household". | P00 and P05 cards and the P02 and P05 chart titles now say "upper bound". |
| (e) Pilot timing | 2026/27 desk dry-run with district officers (no participants), live Besut pilot 2027/28, four districts 2028/29, wider adoption 2029/30 onward. | Nothing to change: the dashboard has no season-dated pilot text. |
| (f) Gate | "At least 43 of 100 placed, under the pre-specified pilot rule." Character for character the same as web.html. | Not present in the dashboard. |

### Wording that is new in pitch.html (please confirm)

- **Lead-number grade.** The brief asked for an OBSERVED lead number. 0.639 and 0.977 are graded **Derived** everywhere in the repo (web.html 06b; the dashboard's "DERIVED from 720 monthly landings"), so pitch.html keeps the Derived chip and says "Measured in official DOF monthly landings". If you relabel it Observed, it will contradict the ledger. The 133-day window next to it is Observed.
- **2026/27 dry-run text.** "With district officers: rehearse worker verification, vacancy confirmation and the data flow on paper. No participants enrolled."
- **The three asks of DOSM.** (1) A district-level tourism-employment table for the four districts, to replace the tourism planning share, which the dashboard's P07 limitation 3 calls "the largest modelled step". (2) A quarterly slot for the worker-month exposure indicator; web.html 02b already proposes a quarterly role for DOSM. (3) A seat at the 2026/27 desk dry-run.
- **Marine Operations Assistant framing.** Its MASCO tasks (the dashboard SkillEvidence table, PDF p. 133) include "repair and service marine engines" and "manage boat registration documents". The slide calls this "off-season maintenance work", as the brief asked.
- **MASCO wording.** The ML step says "task text from the official MASCO 2020 classification" and avoids "verbatim", because the repo contradicts itself on that point (section 5).

## 3. dashboard.html label edits: mirror these in the .pbix

"Title" is the visual's title. "Field name" is the display name of the field in the card. In Power BI a card usually shows the field name, so rename both.

| Page | Visual (HTML id) | Field | Before | After |
|---|---|---|---|---|
| 00 Executive Summary | header textbox (`header0x`) | subtitle | One screen: what is at stake, what it costs, and the two thresholds at which it pays for itself. | One screen: what is at stake, what it costs, and the break-even placement rate (participant earnings = programme cost). |
| 00 | card (`p0_income`) | title and field name | Household income exposed | Income exposed, upper bound (shortened so it fits the narrow card) |
| 00 | card (`p0_p`), value p = 0.0025 | title and field name | Fisheries test (exact p) | 2023 per-state Mann-Whitney test |
| 00 | "The four claims" textbox (`p0_claim`) | claim 4, second sentence | The programme returns what it costs once roughly a third of participants are placed at the published national median wage for their destination occupation group. | Break-even placement rate (participant earnings = programme cost): about a third of participants, at the national median wage for their destination group. |
| 01 Monsoon Clock | header textbox (`header0`) | subtitle | When does the east-coast tourism window close, and why does the national series not show it? | When does the monsoon stop east-coast island tourism, and why does the national series not show it? |
| 01 | "Reading this ledger" textbox (`p1_readledger`) | last paragraph | …the national series cannot see a district-level closure. … | …the national series cannot see a district-level suspension. … |
| 02 Exposure Map | bar chart (`p2_income`) | title | Household income exposed  \|  DOSM median income x worker-month exposure | Household income exposed, upper bound  \|  DOSM median income x worker-month exposure |
| 05 Risk, Cost and Return | header textbox (`header4`) | subtitle | What is at stake in ringgit, and at what assumption level does the programme pay for itself? | What is at stake in ringgit, and at what earnings-share assumption does modelled benefit equal programme cost? |
| 05 | card (`p5_hie`) | title and field name | Household income exposed | Household income exposed, upper bound |
| 05 | bar chart (`p5_hie_chart`) | title | Household income exposed by district  \|  DOSM median income × exposure | Household income exposed by district, upper bound  \|  DOSM median income × exposure |
| 05 | bar chart (`p5_breakeven`) | title | Break-even earnings share by district  \|  above this line it returns its cost | Break-even earnings share by district  \|  where modelled benefit equals programme cost |
| 07 Evidence and Model Card | card (`p6_p`), value p = 0.0025 | title and field name | Fisheries test · exact p | 2023 per-state Mann-Whitney test · exact p |
| 07 | "The negative result" textbox (`p6_neg`) | first sentence | The intuitive answer to a monsoon tourism closure is that boat crews go fishing. | The intuitive answer when monsoon boat services stop is that boat crews go fishing. |

Layout checks:
- The new card titles fit their cards. "Household income exposed, upper bound" was cut off on the narrow P00 card, which is why that card uses the shorter title.
- The P00 "four claims" textbox already overflowed its box by a few pixels with the Linux fallback font, before any change (228 of 212 px). The new claim-4 sentence is shorter than the old one, so the overflow is no worse. Check it on the presentation laptop with Segoe UI.

## 4. Task 4: embedding cross-check NOT run (inputs missing)

The brief said to stop if the 13 MASCO task documents behind the TF-IDF matrix were not all in the repo. They are not, so I stopped: nothing was downloaded, `analysis/embedding_check/` was not created, and pitch.html has no embedding line.

- **Present.** The 8 destination pathways' task lists are in dashboard.html (SkillEvidence table, with MASCO PDF page references). That is 5 short task phrases each, 40 in total.
- **Missing.** The task documents for the **5 current jobs**: Boat Operator, Dive Instructor, Homestay Operator, Snorkel Guide and Tourism Vendor. A few of their phrases can be inferred from rows marked "Carries over", but not the documents.
- **Possibly incomplete.** The dashboard's P07 says there are 78 task records in total, and only 40 are in the repo. So even the 8 destination documents cannot be confirmed as the exact TF-IDF input.
- **Also missing.** The TF-IDF/SVD code and its settings, so 417 terms and 70.5% variance cannot be reproduced from the repo.
- **Not found in history either.** Nothing in git history or in the zip uploaded on 13 Oct (`MonsunBridge_site.zip`, which holds only index.html and images) contains these files.

To run the cross-check later, add the 13 documents exactly as they went into the TF-IDF matrix (one file per occupation), and ideally the vectoriser script.

## 5. Problems found but not changed (team decision needed)

These conflict between web.html and dashboard.html, or concern data, so the hard rules kept me from editing them. Judges can open either file.

1. **MASCO "verbatim" or not?**
   - web.html says "Task text quoted verbatim" (03 data table) and grades MASCO text Observed (04).
   - dashboard P07 limitation 1 says "The 78 task records are the authors' condensed descriptions written from cited MASCO 2020 pages, graded CURATED TEXT, not verbatim MASCO extracts."
   - Pick one answer before Q&A (QA card 9).
2. **"118 official records".** The dataset table in web.html 03 lists 8 + 3 + 1,116 + 480 + 1,368 + 78 + 4 records. The repo does not say how 118 is counted. Be ready to explain it.
3. **District priority index.**
   - web.html 07 shows Besut 87.5, Rompin 70.0, Marang 57.6, Kuala Nerus 35.7.
   - The dashboard's P02 "Transition priority / 100" card and its data show Besut 91.7, Rompin 88.2, Marang 76.9, Kuala Nerus 54.1.
   - pitch.html shows no priority numbers.
4. **The "Johor included" test row.**
   - The dashboard's inference table (P00 and P06) shows "Same panel, Johor included, n = 55, −40.3% retention, p = 0.00041".
   - web.html 06b says Johor included gives −34.7%, and that the −40.3% estimate came from dropping Johor's west coast and was withdrawn.
   - That row is data, so it was not edited.
5. **Nowcast "MASE".**
   - The dashboard's P06 card "Nowcast MASE vs naive" shows 0.731, and the P06 text says "MASE 0.731 … MASE 1.050".
   - web.html 08 says 0.731 is the relative MAE and the MASE is 0.745 (pre-season 1.050 relative MAE, 1.070 MASE). The dashboard's own P06 forecast note also says "relative MAE 0.731".
   - pitch.html says "0.731 relative MAE". Consider renaming the P06 card "Nowcast relative MAE vs naive" (a label-only edit I did not make, because it was not in the brief).
6. **Access setting +25%.** web.html 08 says it changes 1 of 20 top ranks; the dashboard's WeightSensitivity table shows 0. pitch.html quotes neither.
7. **Months behind 0.639.** dashboard P03 says "across 600 state-months"; the dashboard's Transition grade says "DERIVED from 720 monthly landings".
8. **Old wording still in web.html**, which was not edited under R2:
   - "the Northeast Monsoon closes the islands" (hero), "A plan for the months the islands close", "Islands and jetties closed", "Five islands close each season", "Island that closes".
   - The dashboard page guide says "pays for itself".
   - Pilot Stage 1 is dated 2026/27 and the reach section says "season 2026/27".
   - If a judge opens web.html, those conflict with the pitch.

## 6. Checks run

- **Rendering.** All 9 steps at 1920×1080 and 1280×720 in Chromium. No content runs outside its slide and there is no horizontal scroll. At 1280×720, body text is at least 13.3 px and the smallest labels and axis ticks are 12.7 px.
- **Interaction.** Space, PageDown and ← stepping; Home reset; N notes; T timer, amber at 8:01 and red at 10:01 with a simulated clock; ? help; the dashboard page buttons over file://; keyboard hand-off between the dashboard and the deck. No page errors.
- **Scripts.** `check_dashboard_labels.py` and `check_pitch_figures.py` both print PASS.
