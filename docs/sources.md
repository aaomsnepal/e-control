# NEPSE Data Sources (Old → Live)

## 1. Historical / Old Data Repositories

| Repository | What it contains | Link |
|------------|------------------|------|
| **Aabishkar2/nepse-data** | Company-wise OHLC (long history, ~1995+) | https://github.com/Aabishkar2/nepse-data |
| **Nepse-All-Scraper** | Daily OHLC, dividends, rights, floorsheet (auto updated) | https://github.com/SamirWagle/Nepse-All-Scraper |
| **nepse-open-data** | Floorsheet + Adjusted/Unadjusted OHLC + Index | https://github.com/socrateai-official/nepse-open-data |
| **NepseDataHome** | Claims 20+ years data | https://github.com/sakshyambanjade/NepseDataHome |
| **ShareSansarScraper** | Daily price tables archive | https://github.com/OmitNomis/ShareSansarScraper |
| **YONEPSE** | Live + historical JSON shards | https://github.com/Shubhamnpk/yonepse |

### Direct CDN Links (Nepse-All-Scraper)

- Company List:  
  https://cdn.jsdelivr.net/gh/SamirWagle/Nepse-All-Scraper@main/data/company_list.json

- Example OHLC:  
  `https://cdn.jsdelivr.net/gh/SamirWagle/Nepse-All-Scraper@main/data/company-wise/{SYMBOL}/prices.csv`

- Floorsheet pattern:  
  `https://cdn.jsdelivr.net/gh/SamirWagle/Nepse-All-Scraper@main/data/floorsheet/floorsheet_YYYY-MM-DD.csv`

---

## 2. Live / Near Real-time Sources

### Python Libraries

| Library | Link | Notes |
|---------|------|-------|
| nepse_data_api | https://github.com/ra8in/nepse_data_api | Good coverage + caching |
| NepseUnofficialApi | https://github.com/basic-bgnr/NepseUnofficialApi | Classic, floorsheet support |
| api-nepse | https://pypi.org/project/api-nepse/ | Runs local API server |

### Other Languages

| Library | Language | Link |
|---------|----------|------|
| go-nepse | Go | https://github.com/VoidArchive/go-nepse |
| nepse-api-unofficial | TypeScript | https://github.com/surajrimal07/nepse-api-unofficial |
| @rumess/nepse-api | Node.js | https://www.npmjs.com/package/@rumess/nepse-api |

### Hosted / Free APIs (Rate Limited)

- https://nepseapi.surajrimal.dev
- YONEPSE: https://shubhamnpk.github.io/yonepse/

---

## 3. Official / Licensed (for Production)

- NEPSE Official API (application required)
- npstocks (Licensed vendor): https://npstocks.com/
- MDP / SmartWealthPro: https://data.smartwealthpro.com/

---

## 4. Useful Websites

- NEPSE Official: https://www.nepalstock.com.np
- Merolagani: https://merolagani.com
- ShareSansar: https://www.sharesansar.com
- ChartNepali: https://www.chartnepali.com
- NepseAlpha: https://nepsealpha.com

---

**Last updated:** September 2026
