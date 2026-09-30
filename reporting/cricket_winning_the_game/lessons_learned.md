# Lessons learned — “What does it mean to win a game of cricket?”

This file records process mistakes and useful discoveries from producing the cricket article so they are not repeated on later Rails Sports pieces.

## 1. A fact-check is not finished just because the research is sound

The underlying reporting can be correct while the final prose still overstates or alters what the source says.

Examples from this article:

- “thumb strapped up” sounded plausible but was not supported. The source said Jadeja was **padded up** to bat despite the fractured thumb.
- “Pujara told him to hang on until tea” compressed two separate things into one. Pujara told Vihari to stay around and assess the hamstring; Vihari then decided to try to make it to tea.
- Headingley Betfair data was sampled at roughly one-minute intervals, so “as Leach arrived” was too precise. “Around the time Leach arrived” matched the evidence.

### Rule

After the substantive fact-check, run a separate **prose–evidence alignment pass**:

> Does every exact number, quote, physical detail, visual detail, timing claim and attribution in the final prose say only what the source can support?

Do not treat plausible detail as sourced detail.

---

## 2. Physical and visual details need sourcing too

Numbers and quotations naturally attract scrutiny. Narrative details can slip through because they sound harmless.

Check details such as:

- clothing, bandages, equipment and injuries;
- where someone was standing or what they were doing;
- who said or decided something;
- whether something happened before, during or after another event;
- how a player appeared or reacted.

If the source does not establish it, remove it or rewrite it more generally.

---

## 3. Editing can create new factual errors

A line may have been accurate before an edit and become inaccurate after a seemingly harmless rewrite.

Therefore:

1. research;
2. draft;
3. line edit;
4. **fact-check the edited prose again**.

The final fact-check must use the final wording, not an earlier draft.

---

## 4. Lock settled editorial decisions

Repeatedly reopening wording that has already been discussed wastes time and makes the article less stable.

Once a line or passage has been explicitly agreed, treat it as **locked**.

Reopen it only when there is a real reason:

- new evidence contradicts it;
- a later section creates a structural problem;
- repetition becomes visible at article level;
- the wording creates a factual or logical error;
- publication formatting exposes a genuine problem.

Do not “review” settled prose simply because another editing pass has begun.

---

## 5. Separate editorial passes by purpose

Several kinds of work were getting mixed together.

They should be distinct:

### Story/editing pass
Does the article explain the idea clearly and tell the story well?

### Fact-check pass
Is every factual claim supported?

### Prose–evidence alignment pass
Does the wording contain more precision or colour than the evidence warrants?

### Proof pass
Spelling, punctuation, duplicated words, broken links, Markdown hierarchy and formatting only.

### Presentation pass
Headline, standfirst, images, captions, charts, pull quotes, layout, source note, SEO and social presentation.

A later pass should not casually reopen the work of an earlier one.

---

## 6. Do not turn analysis into commentary

A reconstruction should be included because it explains something the reader otherwise would not see.

The rejected Headingley material about the dropped catch, run-out chance and lbw appeal was accurate enough, but it began to read like ball-by-ball commentary rather than analysis.

### Test

> What does this detail reveal that the reader would otherwise miss?

If the answer is merely “this happened next”, cut it.

---

## 7. Ask “Where’s the consequence?”

A true and interesting fact is not automatically worth publishing.

Every technical, tactical or historical detail should earn its place by changing or explaining something:

- a decision;
- a probability;
- a constraint;
- a tactic;
- a player’s options;
- the meaning of the score;
- the broader argument.

If there is no consequence, it is probably a “so what”.

---

## 8. Specificity is valuable only when it is both useful and supportable

Small specific details can give authority and texture — for example, Jack Leach being a specialist left-arm spinner rather than merely “a bowler”.

Keep specificity when it:

1. helps the reader understand the situation;
2. adds useful colour;
3. is supported by evidence.

Do not strip useful detail merely to make prose shorter, but do not invent precision for atmosphere.

---

## 9. Market data needs precision labels

Betfair data can be powerful because it shows how expectations changed, but the sampling level matters.

For each market claim record:

- market ID;
- data product / sampling level;
- timestamp precision;
- match-state alignment method;
- whether the number is exact to a delivery or only approximate around that period.

Use wording such as “around the time” when the data cannot support ball-exact timing.

---

## 10. Keep the source ledger synchronized with the article

When wording changes because of a source issue, update the source ledger at the same time.

The ledger should establish:

- what the source supports;
- whether it is primary, contemporary or retrospective;
- what exact article claim depends on it;
- any limitation on precision.

This prevents the same uncertainty being rediscovered later.

---

## 11. Source transparency does not require citation clutter

Inline links throughout the body made the article feel more like Wikipedia than a finished feature.

For Rails Sports, the preferred approach is book-like:

- keep the article body clean;
- include a short **Notes and sources** section at the end;
- point readers to the research notebook and reporting files;
- keep the detailed audit trail there.

Readers who want the evidence can inspect it without interrupting everyone else’s reading experience.

---

## 12. Presentation is a separate skill

A finished draft is not yet a finished publication.

The presentation/editorial layer includes:

- headline;
- standfirst/deck;
- hero image;
- captions and credits;
- charts and diagrams;
- subheads;
- pull quotes;
- page rhythm;
- source note;
- byline/date;
- SEO title/description;
- social presentation.

Learn this layer while packaging real articles rather than adding another long preparatory course before publishing.

---

## 13. Proofing should be narrow

The final proof caught a real Markdown hierarchy problem: “Notes and sources” had accidentally become a subsection of “What’s the score?”.

That is exactly what a proof pass is for.

At proof stage, check:

- spelling;
- punctuation;
- repeated/missing words;
- heading hierarchy;
- Markdown rendering;
- links;
- obvious typographic inconsistencies.

Do **not** use proofing as an excuse to restart line editing.

---

## 14. Finish and ship

This article took time because the process itself was being learned.

That is useful once. It should make later articles faster.

The purpose of this file is to convert the effort into a reusable method, not to raise the bar so high that nothing gets published.

When the required passes are complete and no material problem remains, move to publication.
