# 🔋 Real-Time Monitoring Platform for Hydrogen Systems

A dynamic and scalable solution for monitoring and analyzing **hydrogen storage and distribution costs** in enterprise environments.  
🎓 Developed as part of my Bachelor's Thesis at the **Universidad Politécnica de Madrid**.

🔗 **Live Dashboard**: https://short.upm.es/ndgmd

---

## 📌 Project Overview

This project focuses on **real-time cost tracking** and **data visualization** related to hydrogen fuel usage in major Spanish cities. 

---

## 🧰 Tech Stack

| Tool                     | Role                                                              |
|--------------------------|-------------------------------------------------------------------|
| **Microsoft Azure**      | Cloud platform for ETL, storage and task automation               |
| **Azure Data Factory**   | Building ETL pipelines to ingest and transform fuel data          |
| **Azure Table Storage**  | NoSQL storage for structured hydrogen data                        |
| **REST APIs**            | Extraction of fuel prices and market rates                        |
| **Power BI**             | Data modeling and interactive dashboards                          |
| **Python**               | Scripted data ingestion with Azure SDKs                           |
| **Power Query**, **DAX** | In-tool transformation and advanced KPI calculations              |

---

## 📁 Project Structure

```
├── src/ # Python scripts for Azure pipeline automation
├── data/ # Example datasets and synthetic test data
├── docs/ # Official thesis document and architectural diagrams
├── dashboard.pbit # Power BI dashboard file
├── requirements.txt # Python dependencies
```

---
## 🧪 Features

### ✅ Real-Time Data Monitoring
- Tracks hydrogen production and fuel prices across key cities in Spain.
- Integrates REST APIs with Azure triggers for automated daily refreshes.

### 📊 Data Visualization
- Power BI dashboards with custom visuals and KPI tracking.
- Filtering by city, fuel type, and date range.

### ⚙️ Cloud Automation
- ETL pipelines managed via Azure Data Factory.
- Data stored and accessed efficiently through Azure Table Storage.

---

## 🔐 Limitations & Status

- **Azure Access**: The data pipeline currently does not run live due to the expiration of the educational license used during development.
- **Deployment**: To activate live updates, a valid Azure subscription and new credentials are required.

---

## 💾 How to Run Locally

### Prerequisites
- Python 3.x installed on your local machine
- Power BI Desktop for data visualization
- An active Microsoft Azure account  
  *(Note: Educational license used during development is now expired)*

### Steps

All setup and configuration steps are explained in the thesis document located in the `docs/` folder.

---

## 🧪 Usage

- **Automated Updates**: The system was designed to extract and update data daily using Azure triggers.
- **Interactive Dashboards**: Use Power BI Desktop to explore trends in fuel prices and hydrogen distribution across Spanish cities.

---

## Future Improvements

- **Geographic Expansion**: Incorporate more regions and international data sources as available.
- **Predictive Modeling**: Add forecasting capabilities for fuel and hydrogen prices.
- **Live Hydrogen Feeds**: Automate hydrogen-related datasets when available through external APIs.

---

## 📄 License

This project was developed as part of a Bachelor's Thesis at the Universidad Politécnica de Madrid (UPM).  
It is publicly available for educational purposes only.  

All intellectual property rights are retained by the UPM and the author, as per institutional agreements.  
Any reuse or redistribution of this project must acknowledge the UPM and the author.  
Please contact them for permission regarding commercial use or adaptations.

---

## ✍️ Author

**Arabela Cárceles Carrillo**
  
---

## 🙏 Acknowledgments

- **Supervisors**: Jorge Pablo Díaz Velilla, Sergio José Ríos Aguilar  
- **Institution**: Universidad Politécnica de Madrid

