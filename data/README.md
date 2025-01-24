# Data Folder

This folder contains datasets used in the project for monitoring and analyzing fuel prices and hydrogen production costs. 
The data is divided into two categories: **static data** and **dynamic data**.

## Data Structure
```
data/
├── static/          # Static datasets related to hydrogen production and costs.
│   ├── DatosHidrógeno.xlsx
│   └── README.md    # Description of datasets.
```

## Static Data (`static/`)
### Files:
- **`DatosHidrógeno.xlsx`**: Contains detailed data about hydrogen production, demand, and costs. The file includes the following sheets:
  - `Annual consumption aggregated`: Annual hydrogen consumption data (English).
  - `Consumo Anual 2022`: Annual hydrogen consumption data (Spanish).
  - `Scenarios for future H2 demand`: Future scenarios for hydrogen demand (English).
  - `Demanda futura`: Future scenarios for hydrogen demand (Spanish).
  - `HydrogenProductionCosts`: Hydrogen production costs (English).
  - `Costes Producción Hidrógeno2022`: Hydrogen production costs for 2022 (Spanish).
  - `AggregatedataHydrogenProuctio`: Aggregated hydrogen production data (English).
  - `Demanda Hidrogeno 2022`: Hydrogen demand for 2022 (Spanish).

### Columns (examples):
- `Country`: Country name (e.g., Spain).
- `Production capacity T/year`: Production capacity in tons per year.
- `Output T/year`: Hydrogen output in tons per year.
- `End-use`: Sector of hydrogen consumption.
- `Cost`: Production cost (€/kg).

## Dynamic Data
- Dynamic data was collected in real-time from the API `https://api.precioil.es` for monitoring fuel prices in major Spanish cities.
  - **Columns**:
    - `Date`: Date of data collection (YYYY-MM-DD).
    - `City`: Name of the city.
    - `Fuel Type`: Type of fuel (e.g., Diesel, Gasoline95).
    - `Price`: Price per liter (EUR).
- The API allowed daily updates for fuel prices, which were processed and visualized using Azure and Power BI.

### Note:
The dynamic data collection service is currently **interrupted** due to the expiration of the Azure license. To use this feature, a valid Azure subscription is required.

## Additional Notes
- Processed data is included in Power BI for visualization and analysis.
- For access to raw or larger datasets, please contact the project author.
