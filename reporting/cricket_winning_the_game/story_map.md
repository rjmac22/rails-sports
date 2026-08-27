# Cricket from First Principles — Journalism Story Map

Source study: `notebooks/21_cricket_from_first_principles.ipynb`

Map Study 21 questions to real cricket evidence so the article demonstrates the analysis rather than listing conclusions.

This file is generated from `story_map.json`. Edit the JSON, then run:

```bash
python reporting/cricket_winning_the_game/build_story_map.py
```

## Question-to-evidence map

| Study question | Analytical point | Evidence | Article role | Decision | Reporting |
|---|---|---|---|---|---|
| What does it mean to win? | A result depends on the format and the match state, not on runs alone. | MCC/ICC result rules | setup | keep | to report |
| What is the basic score? | Runs are the basic scoring unit, but a score has meaning only inside the state of the match. | MCC scoring rules | setup | keep short | to report |
| What limits the accumulation of runs? | Runs are accumulated while wickets, deliveries and/or playing time are being consumed. | Test / ODI / T20 format constraints | core concept | keep | to report |
| Why do wickets matter beyond changing the score? | A wicket can become the scarce resource that ends a chase even when many runs remain. | Headingley 2019 — Stokes and Leach | scene and explanation | keep | reported |
| Are the remaining deliveries equivalent? | No. Their value can depend on who faces them and what state follows. | Headingley 2019 — Stokes and Leach | scene and explanation | keep | reported |
| How does a fixed number of deliveries change the problem? | In limited-overs cricket, each legal delivery consumes a finite resource. | 2016 World T20 final | contrast | likely | to report |
| How can time itself change what a side is trying to do? | In a Test, consuming time can become more valuable than scoring runs when a draw is the attainable result. | Sydney 2021 — Australia v India | major example | keep | to report |
| Does the value of runs, wickets, deliveries and time stay fixed? | No. Their value changes with match state. | Headingley 2019 — Stokes and Leach<br>Sydney 2021 — Australia v India<br>2016 World T20 final | synthesis | keep | partial |
| Do tactics determine outcomes? | Tactics change probabilities; execution and chance still determine what actually happens. | Headingley 2019 — Stokes and Leach | qualification | keep short | reported |
| What is the fielding side trading off? | Run prevention and wicket-taking can pull in different directions. | Headingley 2019 — Stokes and Leach | bridge | keep short | reported |
| What does a field setting represent? | A field setting allocates limited fielding resources across space. | Headingley 2019 — Stokes and Leach | bridge to later studies | bridge only | enough for bridge |

## Evidence jobs

### MCC/ICC result rules

- Type: rules
- Reporting file: `sources.md`
- Status: to report
- Job: Establish formal result conditions without turning the article into a rules explainer.

### MCC scoring rules

- Type: rules
- Reporting file: `sources.md`
- Status: to report
- Job: Establish runs as the basic score.

### Test / ODI / T20 format constraints

- Type: rules and examples
- Reporting file: `sources.md`
- Status: to report
- Job: Show that different formats constrain scoring with different combinations of wickets, deliveries and time.

### Headingley 2019 — Stokes and Leach

- Type: match
- Reporting file: `headingley_2019.md`
- Status: reported enough
- Job: Show that remaining deliveries are not equivalent because both sides care who faces them; also show state-dependent run value and the wicket/run-prevention trade-off.

### Sydney 2021 — Australia v India

- Type: match
- Reporting file: `sydney_2021.md`
- Status: to report
- Job: Show time becoming the scarce resource and the batting objective shifting from chasing runs to surviving.

### 2016 World T20 final

- Type: match
- Reporting file: `world_t20_2016_final.md`
- Status: to report
- Job: Show a fixed number of deliveries as an explicit disappearing resource.

## Guardrails

- Do not turn Headingley into a detailed captaincy or optimal-field analysis.
- Use real examples to answer Study 21 questions; do not write question -> answer -> proved.
- The glossary handles vocabulary; the article must still explain ideas that matter to the argument.
- Not every Study 21 question needs a full scene. Some should be established briefly.
- Field placement is a bridge to the later spatial studies, not the destination of this article.
