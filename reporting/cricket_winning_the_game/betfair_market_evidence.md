# Betfair Exchange Market Evidence

## Purpose

The article argues that the same score event can have very different value depending on the match state. Historical exchange prices provide a useful external check on that argument: they show how people trading the match in real time repriced the possible results as deliveries, time and wickets disappeared.

These prices are **evidence of contemporaneous market expectations, not objective win probabilities**. Decimal exchange odds can be converted to a rough implied probability with `1 / odds`. Where several outcomes existed, the percentages below are normalised across the available runners to reduce small inconsistencies between last-traded prices sampled at slightly different moments.

Do not present these figures as a model proving the correct probability of an outcome. Their journalistic value is that they show the direction and scale of the repricing while the match was happening.

## Source and extraction

Source: Betfair Historical Data, downloaded 28 September 2026 from https://historicdata.betfair.com/

The raw Betfair historical archives are not committed to this repository. The market IDs, archive tier and representative observations are recorded here so the extraction is reproducible from the source archive.

### Kolkata 2016

- Event: England v West Indies, 3 April 2016
- Betfair event ID: `27744338`
- Market: Match Odds
- Market ID: `1.123968779`
- Archive tier: **Pro**
- Sampling: tick-level / sub-second historical stream

Guardian live coverage provides the public chronology: 19 required from six at 12:59 EDT; Stokes begins the final over at 13:00; the first two sixes are reported at 13:02; the third at 13:04. Live-blog timestamps are publication times, not guaranteed ball-release timestamps, so the Betfair figures below are representative prices from the stable intervals around the corresponding market step-changes rather than claims about one exact millisecond.

| Match state | Representative UTC timestamp | England price | West Indies price | Approx. West Indies implied chance |
|---|---|---:|---:|---:|
| 19 from 6 | 17:00:09 | 1.16 | 7.20 | 13.9% |
| 13 from 5 | 17:01:55 | 1.42 | 3.35 | 29.8% |
| 7 from 4 | 17:02:47 | 3.20 | 1.43 | 69.1% |
| 1 from 3 | 17:03:09 | 100.0 | 1.01 | 99.0% |

Analytical use: three deliveries moved West Indies from a large outsider to an almost certain winner in the exchange market. That is a direct contemporary illustration of the article's claim that each delivery creates a new match state rather than merely adding runs.

Public chronology:
- Guardian live: https://www.theguardian.com/sport/live/2016/apr/03/england-v-west-indies-world-twenty20-final-live

### Sydney 2021

- Event: Australia v India, 7–11 January 2021
- Betfair event ID: `30208329`
- Market: Match Odds
- Market ID: `1.177412195`
- Archive tier: **Basic**
- Sampling: approximately one-minute snapshots

Because the Basic archive is sampled at roughly one-minute intervals, use it only for broad match-state changes, not to attribute an exact probability change to one delivery.

| Phase | Representative UTC timestamp | Australia | India | Draw | Normalised implied split |
|---|---|---:|---:|---:|---|
| Start of final day | 10 Jan 22:30 | 1.19 | 40.0 | 7.60 | AUS 84.3% / IND 2.5% / Draw 13.2% |
| Pant–Pujara partnership; India's shortest final-day price | 11 Jan 02:48 | 1.67 | 3.60 | 8.00 | AUS 59.8% / IND 27.7% / Draw 12.5% |
| Around tea, 280/5 | 11 Jan 04:35 | 1.48 | 26.0 | 3.45 | AUS 67.3% / IND 3.8% / Draw 28.9% |
| Around 30 overs remaining | 11 Jan 05:03 | 2.04 | 65.0 | 2.00 | AUS 48.7% / IND 1.5% / Draw 49.7% |
| Later in final session | 11 Jan 06:00 | 6.20 | 1000 | 1.20 | AUS 16.2% / IND 0.1% / Draw 83.7% |
| Near the finish | 11 Jan 06:59 | 470 | 1000 | 1.01 | AUS ~0.2% / IND ~0.1% / Draw ~99.7% |

Analytical use: the market first recognised a meaningful India-win path during the Pant–Pujara partnership, then effectively removed that outcome as wickets and injuries changed the feasible objective. The live contest in the market became Australia versus the draw — exactly the strategic shift the article is describing.

Public chronology:
- Guardian day-five live: https://www.theguardian.com/sport/live/2021/jan/11/australia-v-india-third-test-day-five-live

### Headingley 2019

- Event: England v Australia, 22–25 August 2019
- Betfair event ID: `29424953`
- Market: Match Odds
- Market ID: `1.161492920`
- Archive tier: **Basic**
- Sampling: approximately one-minute snapshots

Guardian live coverage records Stuart Broad's dismissal at 286/9 at about 14:16 UTC. In the following minutes, as Jack Leach arrived and the market settled around the new state, England traded as high as 30.0 while Australia traded around 1.04.

| Match state | Representative UTC timestamp | England | Australia | Draw | Normalised implied split |
|---|---|---:|---:|---:|---|
| 286/9; Leach arrives; 73 required | 14:18 | 30.0 | 1.04 | 960 | ENG 3.35% / AUS 96.55% / Draw 0.10% |

Analytical use: one remaining wicket made 73 runs an extreme task in the market's view. This supports the section's opening state without requiring ball-by-ball market narration.

Public chronology:
- Guardian day-four live: https://www.theguardian.com/sport/live/2019/aug/25/ashes-2019-england-v-australia-third-test-day-four-live

## Publication rule

Use the market evidence asymmetrically:

- **Kolkata:** several prices are useful because the match state flips ball by ball.
- **Sydney:** a few broad snapshots reveal the objective shifting from a possible chase to Australia-versus-draw.
- **Headingley:** one opening price is enough to establish how severe the final-wicket problem was.

The prices should support the cricket argument, not turn the article into a betting-market recap.
