# rails-sports

Sports analysis, modelling and insight built around questions that supporters, players, coaches and managers actually care about.

## Project approach

1. Start with a genuine sporting debate.
2. Build a rigorous model.
3. Test competing ideas.
4. Show the evidence.
5. Explain what it means in plain English.

See [Project principles](docs/PROJECT_PRINCIPLES.md) for the full editorial and analytical standard.

## Research index

The notebooks are a reusable research archive, not a fixed article sequence. Stories can draw from several studies, and new studies can be added whenever an argument needs more evidence.

| Study | Topic | Core question | Potential use | Status |
|---|---|---|---|---|
| 01 | Penalty shootout sudden-death reach | How likely is a penalty shootout to reach sudden death? | Penalty shootout story | Complete |
| 02 | Penalty shootout sudden-death length | If sudden death starts, how long should we expect it to last? | Penalty shootout story | Complete |
| 03 | Snooker match length | How much does a longer best-of-N format increase the stronger player's chance of winning? | Match-format story | Complete |
| 04 | Snooker frame dependence | What changes if frame results are not independent and one frame affects the next? | Match modelling / dependence | Complete |
| 05 | Snooker parameter uncertainty | What happens when we do not know a player's true frame-win probability exactly? | Model uncertainty / ability-change background | Complete |
| 06 | Snooker parameter variation | What happens if frame-win probability varies over time even when its average stays the same? | Model variation / ability-change background | Complete |
| 07 | Snooker stale history | If a player genuinely improves, how badly can a career-wide average lag behind current ability? | Changing ability | Complete |
| 08 | Snooker rolling window | Can recent frames estimate current ability better than an all-career average? | Changing ability | Complete |
| 09 | Snooker window size | How does rolling-window size trade responsiveness against noise? | Changing ability | Complete |
| 10 | Snooker exponential weighting | Can a smooth weighting method forget old results without a hard cutoff? | Changing ability | Complete |
| 11 | Snooker gradual ability change | How do rolling and exponentially weighted estimates behave when ability changes gradually? | Changing ability | Complete |
| 12 | Snooker temporary form | What happens when a player improves temporarily and then returns to the old level? | Form versus lasting change | Complete |
| 13 | Snooker change detection | How reliably can a genuine change be distinguished from ordinary random variation? | Detecting real change | Complete |
| 14 | Snooker searching for form | What happens when we scan an entire career for apparently exceptional stretches? | Multiple testing / false discoveries | Complete |
| 15 | Snooker finding real change | If a genuine permanent improvement is hidden in a career, can we locate it? | Detecting real change | Complete |
| 16 | Snooker change size | How does the size of an underlying ability change affect how easily it can be detected? | Detecting real change | Complete |
| 17 | Snooker change window size | How does the amount of evidence around a candidate change affect detection and localisation? | Detecting real change | Complete |

## Potential story threads

These are editorial possibilities rather than fixed notebook groupings.

- **Penalty shootouts and sudden death** — Studies 01–02.
- **How match structure changes the stronger player's chances** — Studies 03–04, with Studies 05–06 available if the story needs a broader modelling discussion.
- **Measuring a player's current ability** — Studies 05–12.
- **Form versus genuine ability change** — Studies 07–17.
- **Detecting where a player's underlying ability changed** — especially Studies 13–17, drawing on earlier studies where useful.

A study can support more than one story. The aim of this index is simply to make it easy to find previous work and reuse or extend it later.
