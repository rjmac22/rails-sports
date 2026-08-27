# Article Structure — Cricket from First Principles: Winning the Game

This is an editorial map, not draft prose.

Its job is to turn the Study 21 reasoning and the reporting into a readable article without reproducing the notebook question-by-question.

## Working editorial idea

Cricket counts runs, but runs are accumulated while other resources disappear. Which resource matters most — wickets, deliveries, playing time, or access to a particular batter — depends on the match state.

The article should let the reader discover this through real matches rather than announce it as a theorem.

## Proposed shape

### 1. Open in Kolkata: 19 runs, six balls

**Scene:** 2016 World T20 final. West Indies need 19 from the last over.

**Why open here:**

- the problem is immediately legible even to a reader who knows little cricket;
- there are exactly six legal deliveries left;
- the disappearing resource is visible;
- the arithmetic changes violently after each six;
- it gives the article motion before any rules explanation.

**Key states:**

- 19 from 6
- 13 from 5
- 7 from 4
- 1 from 3
- victory with two deliveries unused

**Reader discovery:** a six is not merely six added runs. Scoring heavily early changes the value of every delivery that remains.

**Do not do yet:** explain every format, define all resources, or announce the complete thesis.

**Reporting source:** `world_t20_2016_final.md`

---

### 2. Pull back: what exactly was running out?

Use the minimum formal rules needed to explain the scene.

**Establish briefly:**

- cricket records score in runs;
- a legal over contains six valid balls;
- T20 gives each side a fixed 20-over innings;
- wickets can also end the innings.

Then widen the lens:

| Format | Wickets | Deliveries | Playing time |
|---|---|---|---|
| Test | limited | not fixed in the same way | fixed by the match schedule / playing conditions |
| ODI | limited | fixed | bounded by the one-day contest |
| T20 | limited | fixed | bounded by the short contest |

**Section job:** move the reader from "score runs" to "score runs before something runs out".

This should be short. The rules are scaffolding, not the story.

**Reporting source:** `rules_spine.md`

---

### 3. Sydney: sometimes not scoring is progress

**Scene:** final day of Australia v India, Sydney 2021.

Start with the apparent contradiction:

India are chasing 407, yet by the final session a ball on which they score zero can be a good outcome.

**Sequence to show:**

- India start day five with several outcomes still technically alive;
- Pant's 97 temporarily makes the chase more plausible;
- Pant and Pujara are dismissed;
- Vihari's hamstring injury removes scoring/running options and cannot simply be solved with a replacement batter;
- at tea India are 280/5, 127 short, with 36 overs left;
- Vihari and Ashwin's relevant achievement becomes surviving 259 deliveries without another wicket.

**Reader discovery:** once the attainable objective becomes a draw, India can make progress while the scoreboard barely moves. Each harmless delivery consumes part of Australia's remaining opportunity to win.

**Important qualification:** there is no fake single moment where India "switch to draw". The objective narrows as the state changes.

**Time explanation:** Test time is not merely waiting for a wall clock. India must survive the cricket that can lawfully be played before the match ends.

**Reporting source:** `sydney_2021.md`

---

### 4. Synthesis so far: the same delivery can have opposite value

Keep this very short.

- Kolkata: West Indies need to extract value from each remaining delivery before the stock disappears.
- Sydney: India benefit when deliveries disappear without a wicket.

This is the first place we can state clearly that **the value of a delivery is conditional on the match state and objective**.

Then complicate it once more: even within one match, not all remaining deliveries are equivalent.

That leads naturally to Headingley.

---

### 5. Headingley: who gets the delivery?

**Scene:** England 286/9 chasing 359 in 2019. Stokes 61*, Leach arrives at No. 11. England need 73; Australia need one wicket.

**Start with the apparent simplicity:**

England need runs. Australia need a wicket.

Then show why the next delivery matters differently depending on who faces it.

**Evidence to use:**

- Stokes declining early singles;
- taking twos that reduce the target while retaining strike;
- taking late singles to control who faces the next over;
- Leach's explicit description of the plan;
- Australia's problem of preventing Stokes's boundaries while still trying to gain access to Leach.

**Reader discovery:** a single run does not have a fixed tactical value. One run early in an over may expose Leach; one run late may preserve Stokes's access to future deliveries.

This is the most conceptually sophisticated example, which is why it comes after Kolkata and Sydney rather than before them.

**Reporting source:** `headingley_2019.md`

---

### 6. Brief fielding-side bridge: control is probabilistic

Use Headingley to make two short points, without turning this into the field-placement article.

**Point 1 — competing objectives**

Australia have to trade off:

- preventing Stokes scoring quickly;
- creating wicket opportunities;
- creating deliveries at Leach.

Paine's later reflection about sometimes accepting boundary risk to get more balls at Leach is the useful practitioner evidence.

**Point 2 — tactics do not determine the result**

Australia still create a dropped catch, a run-out chance and the unreviewed lbw opportunity. The choices alter probabilities; execution and chance still matter.

**Stop here on field placement.** The spatial allocation question belongs to the later fielding studies.

---

### 7. Bring the three matches together

This should be the conceptual payoff, not a new example.

The clean three-way distinction:

- **Kolkata:** extracting enough value from a delivery before the delivery resource runs out.
- **Sydney:** surviving the delivery so the opponent's opportunity runs out.
- **Headingley:** controlling who receives the delivery because the delivery's value depends on the batter facing it.

The same basic scoring system produces radically different rational behaviour because the match state changes what is scarce.

This is where the article can finally make the broader statement:

**Cricket is not simply a contest to score runs. It is a contest to score, prevent, preserve and trade resources before the relevant constraint runs out.**

Do not make this sound like a newly discovered law of cricket. The purpose is explanatory: make familiar cricket logic visible to a reader analytically.

---

### 8. Ending / handoff

End by returning to the fielding side.

Once we understand that wickets, runs, deliveries and time have changing values, the next question becomes:

**How does the fielding side allocate its limited players to influence those probabilities?**

That is the natural bridge into the spatial fielding studies rather than another conclusion paragraph repeating the thesis.

## What the article should NOT become

- a history of famous cricket finishes;
- a rules explainer;
- a detailed critique of Tim Paine's Headingley captaincy;
- an optimisation model for batting or field placement;
- a notebook rewritten into prose question-by-question;
- a claim that these ideas are new to cricket practitioners.

## Evidence budget

We have enough.

- Kolkata: one compact opening scene plus Brathwaite's decision logic.
- Sydney: one substantial middle example showing the objective changing with time and injuries.
- Headingley: one substantial example showing delivery identity / strike control and the wicket-versus-runs trade-off.
- Rules: only enough to make those examples intelligible.

Do not add another match unless drafting exposes a specific evidential hole.

## Drafting order

Do not necessarily write from paragraph one onward.

Recommended drafting order for the writer:

1. Kolkata scene.
2. Sydney scene and explanation.
3. Headingley scene and explanation.
4. Three-match synthesis.
5. Rules bridge.
6. Opening transition and ending bridge.

Writing the evidence-heavy sections first reduces the temptation to force examples into a thesis written too early.

## Editorial test for every paragraph

Ask:

**What does the reader understand after this paragraph that they could not understand before it?**

If the answer is only "another cricket fact", cut or relocate it.
