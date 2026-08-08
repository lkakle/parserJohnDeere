### John Deere Catalog E-commerce Scraper & Automation

A production-ready Python web scraper designed to extract dynamic catalog data from the official John Deere platform and automatically structure it for bulk CMS import (Tilda, Deal.by). 

### 🚀 Live Demo & Results

* **Processed & Populated Live Catalog:** [WestAgro - John Deere Catalog](/url?sa=i&source=web&rct=j&url=https://westagro.ru/catalog/forage-harvesters/johndeere&ved=2ahUKEwjEr_2Go5GWAxWTQvEDHfO2HZcQg5wRegYIAAgZEAo&opi=89978449&cd&psig=AOvVaw1zkSKO3OZ2U79407n0XWuY&ust=1786286809004000)
* **Developer LinkedIn Profile:** [Matvei Kirilchik](/url?sa=i&source=web&rct=j&url=https://www.linkedin.com/in/matvei-kirilchik/&ved=2ahUKEwjEr_2Go5GWAxWTQvEDHfO2HZcQg5wRegYIAAgZEA8&opi=89978449&cd&psig=AOvVaw1zkSKO3OZ2U79407n0XWuY&ust=1786286809004000)

### 🎯 Project Overview

* **Task:** Automate the extraction of a large-scale agricultural spare parts catalog (including titles, exact SKUs, technical specs, and high-res images) and import the structured data into the client's Tilda CMS layout.
* **Solution:** Developed a custom Python script to safely extract product details from the supplier's website, clean the raw data, and format it into e-commerce-ready Excel/CSV templates.
* **Outcome:** Automated a tedious, multi-week manual copy-paste task into an efficient workflow completed in just a few days. The live store features structured navigation, filterable attributes, and clean code fully ready for Google indexing.

### 🛠️ Tech Stack & Advanced Features

* **Language:** Python 3.x
* **Libraries:** BeautifulSoup4, Requests, Selenium (for dynamic JS rendering and infinite scrolls)
* **Data Automation:** Pandas / OpenPyXL (for advanced data cleaning and structured Excel formatting)
* **CMS Integration:** Automated batch upload mapping for Tilda CMS (including customized SEO HTML descriptions, embedded focus keywords, and product filtering groups).

### ⚙️ Key Technical Challenges Solved

1. **Dynamic Content Handling:** Successfully extracted data from pages utilizing Javascript-heavy rendering and infinite scrolling via Selenium.
2. **Anti-Bot Protection:** Managed proxy rotation and request headers configuration to bypass platform security measures safely.
3. **SEO Integration:** Programmatically injected target keywords, structured heading hierarchies (H1-H3), and clean nested HTML code straight into the product description fields during the transformation phase.
