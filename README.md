# Indeed review scraper

This code takes in review pages from the website Indeed. It then parses those and creates a spreadsheet with the reviews. This code is part of a course in AI, so see this as a quick sketch rather than a fully worked out piece of software.

N.B.: because of anti-scraping measures by Indeed, I downloaded the pages quickly by hand instead of fetching them programmatically. This saved me some time. If you want to make a more serious version of this I recommend fetching the reviews in an automated way.

## Prerequisites

The code is written in python, and does not use any external libraries except for beautifulsoup to parse html.
