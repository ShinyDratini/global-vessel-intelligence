# \# Global Vessel Intelligence System (GVIS)

# 

# !\[Python](https://img.shields.io/badge/Python-3.11-blue)

# !\[MySQL](https://img.shields.io/badge/Database-MySQL-orange)

# !\[Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)

# !\[Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-green)

# !\[Status](https://img.shields.io/badge/Status-In%20Development-yellow)

# !\[License](https://img.shields.io/badge/License-MIT-lightgrey)

# 

# \## Project Overview

# 

# The Global Vessel Intelligence System (GVIS) is an end-to-end maritime intelligence platform designed to transform vessel movement data into actionable insights for shipping, logistics, supply chain management and commodity trading.

# 

# The project combines Automatic Identification System (AIS) data, geospatial analytics, machine learning, database management and automated reporting to support data-driven maritime decision-making.

# 

# \## Business Objectives

# 

# \- Monitor vessel movements and maritime traffic.

# \- Identify port congestion and operational bottlenecks.

# \- Predict vessel arrival times and potential delays.

# \- Analyse global maritime trade and commodity flow patterns.

# \- Detect abnormal vessel behaviour and potential supply chain disruptions.

# \- Automate maritime intelligence reporting and risk monitoring.

# 

# \## Core Modules

# 

# | Module | Description |

# |---|---|

# | Vessel Tracking | Live AIS data ingestion and historical vessel movement analysis |

# | Port Congestion | Geofencing, anchorage waiting times and port turnaround analysis |

# | ETA Prediction | Machine learning-based vessel arrival time estimation |

# | Commodity Intelligence | Crude oil tanker and LNG carrier movement analysis |

# | Maritime Risk | Anomaly detection, route deviations and disruption monitoring |

# | Intelligence Dashboard | Interactive maps, operational KPIs and automated reporting |

# 

# \## System Architecture

# 

# ```mermaid

# flowchart TD

# &#x20;   A\[AIS Data Stream] --> D\[Python Data Ingestion]

# &#x20;   B\[Marine Weather API] --> D

# &#x20;   C\[Port Reference Data] --> D

# &#x20;   D --> E\[Data Validation and Processing]

# &#x20;   E --> F\[MySQL Database]

# &#x20;   F --> G\[Geospatial Analytics]

# &#x20;   F --> H\[Machine Learning Models]

# &#x20;   F --> I\[Commodity Flow Analytics]

# &#x20;   G --> J\[Streamlit Dashboard]

# &#x20;   H --> J

# &#x20;   I --> J

# &#x20;   J --> K\[Automated Reports and Alerts]

# ```

# 

# \## Technology Stack

# 

# | Category | Technologies |

# |---|---|

# | Programming | Python 3.11 |

# | Database | MySQL, SQLAlchemy |

# | Data Engineering | Pandas, NumPy, WebSockets, REST APIs |

# | Geospatial Analytics | GeoPandas, Shapely, Geopy |

# | Machine Learning | Scikit-learn, XGBoost |

# | Visualisation | Plotly, Matplotlib, Seaborn |

# | Interactive Mapping | Folium, PyDeck |

# | Web Application | Streamlit |

# | Testing | Pytest |

# | Version Control | Git, GitHub |

# | Automation | Windows Task Scheduler |

# 

# \## Planned Data Sources

# 

# | Data Source | Application |

# |---|---|

# | AISStream | Live AIS vessel position data |

# | MarineCadastre | Historical AIS datasets |

# | IMF PortWatch | Port activity and maritime trade indicators |

# | Open-Meteo | Marine weather conditions |

# | World Port Index | Global port reference information |

# | EIA | Energy market data |

# | UN Comtrade | International commodity trade statistics |

# 

# Data availability, geographic coverage and licensing restrictions will be evaluated during development.

# 

# \## Repository Structure

# 

# ```text

# global-vessel-intelligence/

# ├── config/

# ├── data/

# │   ├── raw/

# │   ├── processed/

# │   └── reference/

# ├── notebooks/

# ├── src/

# │   ├── ingestion/

# │   ├── preprocessing/

# │   ├── analytics/

# │   ├── models/

# │   └── reporting/

# ├── sql/

# ├── dashboard/

# │   └── pages/

# ├── tests/

# ├── models/

# ├── reports/

# ├── logs/

# ├── .env.example

# ├── .gitignore

# ├── requirements.txt

# ├── LICENSE

# └── README.md

# ```

# 

# \## Development Roadmap

# 

# \- \[ ] Phase 1 — Project Initialisation and AIS Data Collection

# \- \[ ] Phase 2 — Database Design and ETL Pipeline

# \- \[ ] Phase 3 — Interactive Vessel Tracking

# \- \[ ] Phase 4 — Port Congestion Analytics

# \- \[ ] Phase 5 — Machine Learning ETA Prediction

# \- \[ ] Phase 6 — Commodity Flow Intelligence

# \- \[ ] Phase 7 — Maritime Risk and Anomaly Detection

# \- \[ ] Phase 8 — Streamlit Intelligence Dashboard

# \- \[ ] Phase 9 — Automated Reporting and Monitoring

# \- \[ ] Phase 10 — Deployment and Documentation

# 

# \## Installation

# 

# Clone the repository:

# 

# ```bash

# git clone https://github.com/ShinyDratini/global-vessel-intelligence.git

# cd global-vessel-intelligence

# ```

# 

# Create a dedicated Python environment:

# 

# ```bash

# conda create -n gvis python=3.11 -y

# conda activate gvis

# ```

# 

# Install dependencies:

# 

# ```bash

# pip install -r requirements.txt

# ```

# 

# Create a local environment configuration file using `.env.example` and configure the required API and database credentials.

# 

# \## Industry Applications

# 

# \- Maritime operations and vessel monitoring

# \- Port and terminal operations

# \- Freight forwarding and logistics

# \- Supply chain risk management

# \- Commodity trading and market intelligence

# \- Energy transportation analytics

# \- Maritime data engineering

# 

# \## Future Enhancements

# 

# \- Deep learning-based vessel trajectory prediction

# \- Global maritime trade network analysis

# \- Commodity price and vessel flow correlation modelling

# \- Vessel routing and voyage cost optimisation

# \- AI-generated maritime intelligence briefings

# \- Cloud-based real-time streaming architecture

# 

# \## Author

# 

# Developed as an independent portfolio project combining professional logistics and supply chain experience with postgraduate training in data analytics.

# 

# \## Disclaimer

# 

# This project is intended for educational, research and portfolio purposes. It is not intended for navigational, commercial trading or safety-critical operational decisions. AIS data may contain inaccuracies, missing observations and reporting delays. Vessel movements alone do not establish actual cargo quantities or ownership.

# 

# \## License

# 

# This project is licensed under the MIT License.

