# ps158-reproduce2

**Inequality and Income.** An interactive scatter plot of the Gini index against GDP per capita for 165 countries. It tests Kuznets' inverted-U hypothesis, the idea that inequality rises and then falls as countries get richer.

Live page: https://jvelaise.github.io/ps158-reproduce2/

## Files

- `index.html`: the page. It is self-contained, with the data embedded.
- `data/gini_gdp_by_country.json`: the joined dataset, with one entry per country listing `[year, gini, gdp_per_capita]` for each survey year.
- `data/process.py`: the script that builds the dataset from the World Bank API downloads.

## Data

World Bank, World Development Indicators (data updated 8 Oct 2026):

- `SI.POV.GINI`: Gini index
- `NY.GDP.PCAP.PP.KD`: GDP per capita, PPP (constant 2021 international $)

To rebuild the dataset, download the raw files and run the script:

```bash
mkdir -p raw
curl -s "https://api.worldbank.org/v2/country/all/indicator/SI.POV.GINI?format=json&per_page=20000&date=2000:2025" -o raw/gini.json
curl -s "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.PP.KD?format=json&per_page=20000&date=2000:2025" -o raw/gdp.json
curl -s "https://api.worldbank.org/v2/country?format=json&per_page=400" -o raw/countries.json
python3 data/process.py raw data/gini_gdp_by_country.json
```

## Main findings (surveys from 2015 or later)

- The correlation between Gini and log GDP per capita is about −0.27, which is weak.
- A quadratic fit peaks near $4,300 per person, so it is only a faint inverted U.
- All 15 countries with a Gini above 45 are in Sub-Saharan Africa or Latin America.
- Many countries measure consumption rather than income, which makes them look more equal. Gini values from the two methods are not fully comparable.
