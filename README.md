# Virtual Worlds, Real Concern
## An Interdisciplinary Analysis of the Influence of Immersive Gaming Environments on Environmental Perceptions 

This project investigates whether playing environmentally themed video games—specifically Animal Crossing—is linked to greater climate awareness and concern. By combining player behavior data with global climate opinion data, the study uses interactive visualizations to explore correlations between in-game actions and real-world environmental perception. The findings offer new insights into the potential of virtual worlds as tools for climate engagement and education. 

---

## Table of Contents

- [Overview](#overview)
- [Authors and Contribution Statement](#authors-and-contribution-statement)
- [SDG Contribution](#sdg-contribution)
- [Visualizations Included](#visualizations-included)
- [Tools & Libraries](#tools--libraries)
- [Intellectual and Professional Growth](#intellectual-and-professional-growth)
- [Navigation Instructions](#navigation-instructions)
- [Project Information](#project-information)
- [Embedded Media](#embedded-media)
- [References](#references)

---

## Overview

This research project examines how immersive environmental video games can influence players' climate awareness and concern. By exploring the link between virtual experiences and real-world attitudes, it highlights the potential of games as powerful tools for climate communication and education.

As a case study, we chose to examine Animal Crossing: New Horizons, a popular game that emphasizes interactions with the in-game environment. Players are incentivized to gather resources for use in crafting items or building amenities (like a general store) for the island. They are also prompted to collect bugs, fish, and fossils to donate to the museum, sell, or display. This environmental interaction is the focus of this study.

This project was developed using the Streamlit Python library. To run it, the files can either be downloaded and run locally on your device, or the app can be accessed online at Streamlit Cloud.

---

## Authors and Contribution Statement

**Gbemisayo Motunrayo Aderonke Adelaja** – Literature review, data cleaning, background research, identifying the project’s scholarly contribution and future directions.

**Hailee Cunnigham** – Visualization design and implementation, including dataset merging, format selection, Streamlit development for accessibility, and use of colorblind-safe palettes.

Both Gbemisayo and Hailee collaborated on the poster design and README documentation.

---

## SDG Contribution

This project supports:  
**SDG 13: Climate Action** – By analyzing how gameplay in Animal Crossing: New Horizons relates to environmental attitudes, the project promotes awareness and informal education around climate issues, contributing to global efforts on climate change knowledge and engagement.

**SDG 17: Partnerships for the Goals** – The project bridges disciplines including game design, environmental science, and psychology. By combining gameplay data with public opinion datasets, it demonstrates how cross-sector collaboration can support innovative climate solutions.

---

## Visualizations Included

1. **Scatterplot** – Shows the correlation between playtime and environmental agreement. Includes trendline, R² value, and region-based coloring with interactive filters.

2. **Boxplot** – Compares environmental opinions by favorite in-game activity. Highlights medians, spread, and outliers for each player group.

3. **Grouped Bar Chart** – Contrasts climate concern levels between general populations and players across countries. Uses color and alignment for clear comparison. 

**Ethics & Accessibility:**  
- **FAIR Principles** – Ensures reusability and clarity (Wilkinson et al., 2016)  
- **CARE Principles** – Consideration of Indigenous and cultural context  

---

## Tools & Libraries

- `pandas` – Data cleaning and organization  
- `matplotlib` – Static visualizations  
- `streamlit` – Interactive web app for real-time data exploration  
- `seaborn` – Colorblind-safe palettes for inclusive design  
- `Coblis` – Color Blindness Simulator to test accessibility  
- `Google Colab` – Cloud-based development environment for collaboration and execution  

---

## Intellectual and Professional Growth

**Hailee Cunningham**  
Through self-study and collaboration, I strengthened my design and coding skills, applying both prior programming knowledge and new tools like Streamlit to enhance interactivity. Feedback from peers and instructors guided my revisions and helped me make the project more accessible and engaging.

**Gbemisayo Adelaja**  
Hands-on activities and feedback from the symposium sharpened my ability to design for clarity and audience needs. The museum field trip challenged my perspective on accessibility, inspiring better data presentation in our final project. Using simulated data also deepened my understanding of data transparency and usability.

---

## Navigation Instructions

- **`Final report.pdf`** – Full project process and result summaries   
- **`app.py`** – Python code for visualizations  
- **`gameData.csv`** – Data file for animal crossing players perception on climate issues 
- **`globalData.csv`** – Data file for general public perception on climate issues 
- **`Final poster.pdf`** – Summary poster suitable for presentation with all visualizations included  
Download all packages from the requirements.txt. Make sure the two .csv data files are uploaded in the same file directory (this is mock data randomly generated by Mockaroo). Run the file and view the prototype visualization.

Download app.py and all .csv files, making sure they are in the same file. In your terminal, navigate to the folder with the files and run the command streamlit run app.py.

Alternatively, access the visualization here: https://finalproject-t4xubdn2cznyernjn2l4sj.streamlit.app/.

---

## Project Information

- **Authors**: Gbemisayo Motunrayo Aderonke Adelaja and Hailee Cunningham  
- **Instructor**: Professor Luyao Zhang  
- **Course**: INFOSCI 301- Data visualization and Information Aesthetics  
- **Institution**: Duke Kunshan University

**Acknowledgement**:  
We would like to acknowledge Prof. Luyao Zhang, who gave us feedback on the initial steps of the project that led to this final submission. Nemuleen Togtbaatar and Yiqing Wang for peer reviewing our paper. The students from INFOSCI 301 course who gave insightful feedback for our project. We also want to acknowledge the use of Github, Streamlit, Canva, Google collab as tools we use to achieve this project and report. 

**Disclaimer**:  
This final project is for INFOSCI 301 Data Visualization and Information Aesthetics, instructed by Prof. Luyao Zhang at Duke Kunshan University in Spring 2025.

**Data**:  
We implemented data from Vuong et al.'s multinational dataset of game players’ behaviors in a virtual world and environmental perceptions (https://www.scidb.cn/en/detail?dataSetId=cb5d36cce29f4e5695a586c9b85d04b6&dataSetType=journal) and the Peoples' Climate Vote (https://peoplesclimate.vote/data-center).

---

## References

- Anscombe, F. J. (1973). Graphs in Statistical Analysis. The American Statistician.  
- Bekoum Essokolo, V.-L., & Robinot, E. (2022). Let’s Go Deep into the Game to Save Our Planet! Sustainability.  
- Carman, J., et al. (2024). Geeks versus Climate Change. Climatic Change.  
- Ferguson, C. J., & Jackson, S. (2022). The Influence of Video Games on Environmental Attitudes. Frontiers in Psychology.  
- Flanagan, M., & Nissenbaum, H. (2014). Values at Play in Digital Games. MIT Press.  
- Ouariachi, T., et al. (2019). A Framework for Climate Change Engagement through Video Games. Environmental Education Research.  
- Statista (2025). Animal Crossing: New Horizons Sales.  
- Talbot, J., et al. (2014). Perception of Bar Charts. IEEE TVCG.  
- Tufte, E. R. (1983). The Visual Display of Quantitative Information. Graphics Press.  
- UNDP (2021). People’s Climate Vote.  
- UNDP & University of Oxford (2021). People’s Climate Vote.  
- Vuong, Q.-H., et al. (2021). Animal Crossing Survey Dataset. Sciengine.  
- Wilkinson, L. (2005). The Grammar of Graphics. Springer.

## Project Poster
You can view or download the project poster here:  
![Project Poster](./project_poster.jpg)
