# Real-Time Monitoring and Control Platform for Hydrogen Systems

This repository contains the source code and documentation for my Bachelor's Thesis project, titled **"Development of a Real-Time Monitoring and Control Platform for Hydrogen Storage and Distribution Systems in Enterprises."** 
The project was developed at the Universidad Politécnica de Madrid and aims to provide a dynamic and scalable tool to monitor and analyze costs related to the use of hydrogen in business contexts.

## Features
- **Dynamic Data Monitoring**: Real-time tracking of fuel prices and hydrogen production costs in major Spanish cities.
- **Scalability**: Designed to adapt to future expansions as the hydrogen market matures.
- **Data Visualization**: Integration with Power BI for clear and interactive visual dashboards.
- **Automated Updates**: Daily data extraction and report updates using Azure services.

## Technologies Used
- **Microsoft Azure**: Cloud-based data storage and processing using services such as:
  - Azure Data Factory for ETL pipelines.
  - Azure Table Storage for efficient and scalable NoSQL data storage.
  - REST API services for data extraction.
- **Power BI**: For data modeling, analysis, and visualization.
- **Python**: Development of custom scripts for data extraction and processing using libraries from the Azure SDK.
- **Power Query and DAX**: Used within Power BI for advanced data transformation and calculations.

## Repository Structure
- `src/`: Contains Python scripts for setting up Azure services and pipelines.
- `data/`: Datasets used in the project.
- `docs/`: Project documentation.

## Installation and Setup
### Prerequisites
- An active Microsoft Azure account (see note below regarding license).
- Python 3.x installed on your local machine.
- Power BI Desktop installed for data visualization.

### Steps
All steps for configuring and running the project are detailed in the Bachelor's Thesis document located in the `docs/` folder.

## Important Note
- The development and documentation of this project were carried out in Spanish.
The data collection service is currently **interrupted** due to the expiration of the Azure educational license used during development.
  To enable the full functionality of the project, you will need a valid Microsoft Azure subscription to manage and automate the data workflows.

## Usage
- **Data Update**: Data is automatically extracted and updated daily using Azure triggers (requires an active Azure subscription).
- **Interactive Dashboards**: Navigate through the Power BI interface to explore fuel and hydrogen cost trends.

## Future Improvements
- **Data Coverage Expansion**: Add support for more cities and regions as new data sources become available.
- **Enhanced Analysis**: Integrate predictive analytics to anticipate fuel price trends.
- **Dynamic Hydrogen Data**: Automate hydrogen-related data collection as market maturity progresses.

## Authors
- **Arabela Cárceles Carrillo**  
  Bachelor in Computer Science, Universidad Politécnica de Madrid  
  [LinkedIn Profile](https://www.linkedin.com/in/arabela-carceles-carrillo/)

## Acknowledgments
- Supervisors: Jorge Pablo Díaz Velilla, Sergio José Ríos Aguilar
- Universidad Politécnica de Madrid

## License
This project was developed as part of a Bachelor's Thesis at the Universidad Politécnica de Madrid (UPM). 
  While the content of this repository is publicly available for educational purposes, ownership of the project and its associated intellectual property is retained by the UPM as per institutional agreements signed by the author.

### Usage
- Any reuse or redistribution of this project must acknowledge the UPM and the author.
- Please contact the UPM or the author for permissions regarding commercial use or adaptations.

## Links
- [Project Repository](https://github.com/arabelacarceles/TFGInformatica)
- [Platform Access](https://short.upm.es/ndgmd)
