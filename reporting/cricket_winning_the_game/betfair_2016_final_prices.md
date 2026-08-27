# Betfair Exchange prices — 2016 World T20 final

## Reporting purpose

Use the in-play Match Odds market, if recovered, as an external contemporaneous measure of how much each final-over delivery changed the match state.

Desired checkpoints:

- West Indies need 19 from 6
- after 19.1: 13 from 5
- after 19.2: 7 from 4
- after 19.3: 1 from 3
- match won after 19.4

For each checkpoint, recover the West Indies and England Exchange prices immediately before/after the delivery, plus matched volume where available. Convert decimal odds to raw implied probability only as a descriptive aid (`1 / decimal odds`), with a note that Exchange prices are not vig-free model probabilities and can move during suspension/reopening.

## Source identified

Betfair Historical Data provides timestamped Betfair Exchange market, price and settlement data from April 2015 onward. The 3 April 2016 final is therefore within coverage.

Betfair's Developer Program states that all historical data from May 2015 through April 2016 is available at a purchase price of £0, including ADVANCED and PRO packages. The user still has to complete Betfair's purchase process while logged in before the files become downloadable.

Official source trail:

- Betfair Historical Data service: https://historicdata.betfair.com/
- Service description: https://support.developer.betfair.com/hc/en-us/articles/360002407732-What-data-is-provided-by-the-Historical-Data-service
- Historical Data API access: https://support.developer.betfair.com/hc/en-us/articles/12859956891932-How-Can-I-Make-HTTP-Requests-to-the-Historical-Data-API
- £0 May 2015-April 2016 pricing notice: https://forum.developer.betfair.com/forum/developer-program/historical-data/38607-historical-data-pricing-update-may-2015-to-april-2016-data-now-free-to-purchase

## Access status

**Source found; raw market file not yet acquired.**

The historical portal requires a registered Betfair.com account login. The raw file is not exposed publicly through the web and no reliable public mirror of this specific match market was found during reporting searches.

Do not invent or estimate the market prices from the score state. If the file is acquired, use the actual Exchange stream.

## Target download

Sport: Cricket

Date: 3 April 2016 (or April 2016 package)

Event: England v West Indies, ICC World Twenty20 final, Eden Gardens, Kolkata

Market: Match Odds

Preferred package: PRO if practical; ADVANCED is also sufficient for ball-level reconstruction.

## Alignment source

Use the contemporary ball-by-ball timestamps/sequence to align the Exchange stream with the four deliveries. Guardian live coverage timestamps the final over at approximately 13:00-13:05 EDT; ESPN/official scorecards establish the exact ball sequence.

Do not assume the first price tick after a six is the clean post-ball price: cricket markets are normally suspended around material events and then reopened. For article use, define a consistent rule such as the first stable traded price after reopening, and document it.
