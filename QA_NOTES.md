# Q&A answer cards: DOSM Datathon 2026 final, 19 Oct

Short answers for the 5-minute Q&A. Every figure is quoted from web.html (W), dashboard.html (D) or a committed script; the source is in brackets. **TO CONFIRM WITH TEAM** marks anything the repo does not state; confirm it, or don't say it. Press 1 to 9 on pitch.html to jump to the matching slide.

---

### 1. Why does a marine job rank first for a boat operator? (slide 5)
- **Score.** Marine Operations Assistant scores 0.77 for a Besut boat operator, against 0.34 for the next option. [W 05b]
- **Biggest driver.** Task similarity contributes the most: 0.40 × 0.963 = +0.385. [W 05c]
- **Be upfront about seasonal fit 0.80.**
  - It is **one uniform analyst setting** applied to all non-fishing pathways, because no official monthly series exists for them. The dashboard grades it "ANALYST SETTING (no landings observation)". [D Transition table]
  - Only the three fishing pathways have a derived value: 0.639, "DERIVED from 720 monthly landings". [D Transition table]
  - It is exactly what our own sensitivity test exposes: lower the seasonal-fit setting by 25% and **4 of 20** top ranks move [W 08; D page 06 "that is where the uncertainty actually lives"].
- **Why marine work is still plausible off-season.** Its MASCO tasks (MASCO PDF p. 133) include "repair and service marine engines", "manage boat registration documents", "locate engine defects with instruments" and "monitor temperature fuel and oil readings" [D SkillEvidence]. That is maintenance and paperwork, not open-sea work.
- **Guardrail.** Rankings are not job offers. Employers confirm vacancies before anyone enrols [W 05b], and the pilot measures placements and months worked, which then replace the setting.

### 2. Where does "At least 43 of 100 placed" come from? (slide 9)
- **Wording.** Say the sentence exactly: "At least 43 of 100 placed, under the pre-specified pilot rule." [W 11] Add: "The threshold depends on the stated wage, work-duration and cost assumptions." [W 11]
- **Possible explanation, TO CONFIRM WITH TEAM before using it.** 43 is the smallest count out of 100 whose one-sided 95% Wilson lower bound exceeds the 34.6% services-and-sales break-even rate. `analysis/qa/gate_wilson_check.py` checks the arithmetic:
  - 43 placed gives a lower bound of 35.15% (above 34.6%); 42 placed gives 34.20% (below).
  - The same rule would give 38 for clerical support (30.3%) and 44 for craft and trades (35.4%). If this is the reason, be ready to explain why services and sales is the reference group.
- **Simple framing for judges.** "43 is chosen so that, even allowing for sampling error in a 100-person pilot, we can say the placement rate is above break-even before we expand."

### 3. Where do the planning share and the dependency weight come from? (slide 2)
- **Formula.** WME = observed district employment × tourism planning share × dependency weight × exposure months. [W 04; D page 02]
- **Worked example.** Besut: 61,800 × 8% × 1.00 × 4.37 = 21,603 worker-months from 4,944 modelled workers. [D page 02 "The exposure arithmetic"]
- **Planning shares used.** Besut 8%, Marang 7%, Rompin 6%, Kuala Nerus 5%. [D page 02 "Exposure build" table]
- **What the repo says about the source.**
  - "District tourism share is MODELLED from state-level published shares; it is the largest modelled step." [D page 07, limitation 3]
  - Both factors are "declared planning assumptions", which is why the cohort is graded Modelled. [D page 02; W 04]
- **TO CONFIRM WITH TEAM.**
  - The repo does not name the state-level publication behind the shares.
  - It shows only Besut's dependency weight (1.00); the other three districts' weights and their basis are not stated. Do not back-calculate them on stage.
- **Sensitivity.** [D page 05 sensitivity chart]
  - Dependency weight ±15% moves cost per worker-month between RM 771.59 and RM 1,043.92.
  - Planning share ±25% cancels out (RM 887.33), because it scales the cohort and the cost together.
- **Link to our ask.** This is why our first ask of DOSM is a district-level tourism-employment table.

### 4. Press reports say only about 3,000 to 5,000 island tourism players. Why 13,703? (slide 2)
- **Scope difference.** 13,703 is a **modelled planning envelope of tourism-linked workers in four districts**, including mainland tourism-linked work, not only island operators.
  - It is built from all of each district's observed employment, times a tourism planning share. [D page 02]
  - The occupations modelled are boat operators, dive and snorkel crew, and homestay and island-vendor staff. [W "about"; D Occupation table]
  - It is "a planning envelope and is never called a register". [D page 02]
- **Not a contradiction.** A count of island players answers a narrower question. The 3,000 to 5,000 range comes from the team brief, not our data: **have the press source ready if you cite it.**
- **What a smaller cohort would change.** The budget, not the unit cost: planning share ±25% leaves cost per worker-month at RM 887.33 [D page 05 sensitivity chart]. The district verification step is where the real count gets fixed.

### 5. Why lead with p = 0.0083 and not the smaller p = 0.00062? (slide 6)
- Only three states are on the treated east coast. With so few clusters, cluster-robust standard errors are anti-conservative, so the panel's smaller p is the weaker evidence.
- The exact permutation test makes no such assumption: our labelling is the most extreme of all 120 possible ways to label 3 of 10 states as east coast. [W 06b]
- All tests are two-sided. The coast-pair test (n = 5) is not significant because 0.0625 is its smallest possible two-sided p. [W 06b; D page 00]

### 6. What is the p = 0.0025 tile on the dashboard? (live demo)
- It is the **2023 per-state Mann-Whitney test**: Terengganu and Pahang, every non-monsoon month of 2023 out-landed every monsoon month, U = 0. [D pages 00 and 07]
- The tile has been renamed to say so. Our headline remains p = 0.0083 from the permutation test.

### 7. Is the 0.639 vs 0.977 gap causal? Is it observed? (slides 1 and 6)
- **Grade.** It is **Derived**: a ratio computed from observed DOF monthly landings, averaged over five seasons. [W 06b]
- **Precision.** The gap is −35.4%, with a 95% CI of −46.8% to −21.7%. [W 06b]
- **Not causal.** "Coast is not randomly assigned, so this is an association under exchangeability. No causal effect is claimed." [D page 00]
- **Watch out.** The dashboard text says "600 state-months" (page 03), but its data grade says "720 monthly landings". TO CONFIRM which count is right.

### 7b. Is −35.4% simply 0.639 vs 0.977? (slides 1, 3, 6)
- No. A judge who divides 0.639 by 0.977 gets a slightly smaller gap.
- **−35.4% is the state × season panel estimate**: a difference-in-differences with season fixed effects over 50 state-seasons, 95% CI −46.8% to −21.7%. [W 06b]
- 0.639 and 0.977 are the five-season average ratios for each coast. [W 06b]
- The slides now label it "panel estimate" for exactly this reason. Do not call it the ratio of the two dots.

### 7c. Which test is the headline? (slides 4, 6)
- **The exact permutation test, p = 0.0083.**
- The panel test (p = 0.00062) agrees, but with three treated states its clustered errors are anti-conservative. [W 06b]
- The dashboard's two explanatory notes (pages 00 and 06) were relabelled to say the same, so the demo and the slides now agree.

### 7d. Why are only 3 of the 7 datasets checksum-verified? (slide 3)
- Those three were downloaded programmatically from data.gov.my (labour force, household income, fish landings), so their bytes can be hashed. [W 03]
- The other four were transcribed from published releases or reviews: the DOSM tourism survey, the METMalaysia review, MASCO and the Tourism Satellite Account. Each is cited to its publisher. [W 03]

### 8. Your forecast fails before the season. Why keep it? (slide 8)
- **What was tested.** Models were chosen on 2018–2022 with rolling-origin cross-validation; held-out 2023 was scored once. [W 08]
- **One month ahead.** Relative MAE 0.731, i.e. 27% lower error than seasonal naive. The pooled test gives p = 0.004, but clustered by state (3 clusters) it is not significant. [W 08]
- **Pre-season.** 1.050, worse than naive, so **not claimed**. [W 08]
- **Proposed use.** An in-season severity monitor, not a pre-season forecast. It is on the roadmap and not built.
- **Watch out.** The dashboard's page 06 card says "Nowcast MASE vs naive 0.731". web.html says 0.731 is the relative MAE and the MASE is 0.745. If asked, the 0.731 is the relative MAE.

### 9. Is the MASCO text verbatim? (slides 3 and 8)
- **The repo contradicts itself. Decide before Q&A.**
  - web.html section 03 says "Task text quoted verbatim".
  - dashboard page 07, limitation 1, says: "The 78 task records are the authors' condensed descriptions written from cited MASCO 2020 pages, graded CURATED TEXT, not verbatim MASCO extracts."
- **Safest true answer.** "Task descriptions written from the cited MASCO 2020 pages, each with its PDF page reference; similarity measures overlap in that wording." The page references are in D SkillEvidence.

### 10. Why TF-IDF and not modern embeddings or an LLM? (slide 8)
- **Explainable by construction.** The score is a linear form with known weights, so the contribution chart is exact. There is no pre-trained model and no network call at run time. [D page 03, page 07 third-party components]
- **On the roadmap.** Mapping free-text job descriptions to MASCO codes with embeddings or an LLM, plus human review during district verification. **Proposed, not built.**
- **If asked whether we cross-checked with embeddings.** No. The five current-job MASCO documents used in the TF-IDF matrix are not in the published repo, so the cross-check could not be run. Don't imply it was.

### 11. What does RM 887 buy, and who pays? (slide 7)
- **Build-up.** One training month at RM 1,100, plus two support months at 60% of that rate, plus 10% administration, gives RM 2,662 per participant. Over three months that is RM 887 per worker-month. [W 07]
- **Grade.** Scenario. "Unit cost is not drawn from any published schedule." [D page 04]
- **Default scenario.** At 20% participation: 2,741 participants, RM 7.30M, 8,223 worker-months covered (about 16% of 52,655). [W 07]
- **Break-even placement rate (participant earnings = programme cost).** About one-third: 30.3% to 35.4%, depending on the destination wage. It is arithmetic, not a measured return, and participant earnings are not a return to government budgets. [W 07]

### 12. Is RM 315.5M the income loss? (slide 7)
- No. It is household income exposure: DOSM district median household income × worker-month exposure. [D pages 02, 05]
- It is an **upper bound**, because it assumes one tourism-linked worker per household. [W 07; D page 05]
- Expected loss depends on a tourism earnings share that the reader sets on page 05. It is never estimated from data. [D page 05]

### 13. Why only a dry-run this season? (slide 9)
- The season opens around 9 November.
- District verification needs 8–10 weeks before the season [W 02b], and that window has passed.
- So 2026/27 is a desk dry-run with district officers, with no participants. The live Besut pilot is 2027/28 (100 participants, RM 266,200 indicative), four districts follow in 2028/29, and wider adoption after that.
- Every stage is proposed, subject to partner agreement.

### 14. What exactly do you want from DOSM? (slide 9)
1. A district-level tourism-employment table for Besut, Marang, Kuala Nerus and Rompin, which replaces our largest modelled step.
2. A quarterly slot for the worker-month exposure indicator. web.html 02b already proposes DOSM "update a reusable exposure indicator, every quarter".
3. A seat at the 2026/27 desk dry-run.

### 15. Why do you say operators "suspend" and not that the islands "close"?
- Terengganu issues no official closure order (team brief). **Have the source ready.**
- What happens is that island operators suspend and boat services stop. The 133-day window itself is METMalaysia's dated monsoon window. [W 04]

### 16. Can it scale? Is 13,703 a national estimate?
- No. It is 0.392% of Malaysia's 3.5 million tourism jobs, and "a four-district pilot scope, not a national estimate … No national extrapolation is performed." [D page 07]
- Each expansion has a gate: validate locally before expanding. [W 11]

---

## Inconsistencies a judge might spot (fix or prepare an answer)
Details are in CHANGES_PITCH.md section 5.
- "118 official records" vs the record counts in web.html 03's dataset table. **TO CONFIRM** how 118 is counted.
- District priority index: web.html 07 shows Besut 87.5; dashboard page 02 shows 91.7 (and the other districts differ too). pitch.html shows neither.
- Dashboard inference table row "Same panel, Johor included … −40.3%". web.html says Johor-included is −34.7% and the −40.3% estimate was withdrawn.
- Access setting +25%: web.html 08 says it moves 1 of 20 top ranks; the dashboard's sensitivity table shows 0.
- web.html still uses "islands close", "pays for itself" and a 2026/27 pilot date. It was left unedited by rule. Present from pitch.html and the dashboard.
