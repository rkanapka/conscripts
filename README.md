# Lithuanian Conscripts Data Analysis

![image](https://github.com/rkanapka/conscripts/assets/40775067/6836839b-1a3c-452e-ab61-a6c297ef7c14)

## Overview
This Python project aims to analyze data related to Lithuanian conscripts, extracting information from the official Lithuanian conscripts' site https://sauktiniai.karys.lt. The project utilizes the Pandas library to process the data and generates a comprehensive analysis presented in an Excel spreadsheet.

## Features
* Data Extraction: Fetches data from the official Lithuanian conscripts website.
* Data Processing: Utilizes Pandas for efficient data manipulation and analysis.
* Excel Output: Generates an Excel spreadsheet containing detailed tables of analysed data.

<!-- GETTING STARTED -->
## Getting Started

To get started with the Lithuanian Conscripts data analysis application, follow these steps:

### Prerequisites

* Python3.12

### Installation

Project setup:

1. Clone the repo:
   ```bash
   git clone https://github.com/devKanapka/conscripts.git
   ```
2. Create virtual environment & source it:
   ```bash
    python -m venv .venv
    # On Windows:
    venv\Scripts\activate
    # On macOS and Linux:
    source venv/bin/activate
   ```
3. Install requirements:
   ```bash
    pip install -r requirements-dev.txt
   ```
4. Install pre-commit:
   ```bash
    pre-commit install
   ```
5. Run application:
   ```bash
    python -m conscripts.main
   ```
6. Analyse results in the generated Excel spreadsheet - "conscripts.xlsx":

## Screenshoots
### 1st sheet of spreadsheet
![image](https://github.com/rkanapka/conscripts/assets/40775067/ea17d049-1a3e-4a6c-8a9e-4ba1d906aafa)
![image](https://github.com/rkanapka/conscripts/assets/40775067/88f0ffd3-4796-48e8-a445-b357057d4038)

### 2nd sheet of spreadsheet
![image](https://github.com/rkanapka/conscripts/assets/40775067/79da6fa4-ce3b-41a6-8539-729ac998dc6c)

## Contributions
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

## Contact

[![Facebook][facebook-shield]][facebook-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Instagram][instagram-shield]][instagram-url]

Rimvydas Kanapka - [kanapka.rimvydas@gmail.com](MAILTO:kanapka.rimvydas@gmail.com)

<!-- Social media -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-007AB5.svg?style=for-the-badge&logo=linkedin
[linkedin-url]: https://www.linkedin.com/in/rimvydas-kanapka
[facebook-shield]: https://img.shields.io/badge/-facebook-0866FF.svg?style=for-the-badge&logo=facebook
[facebook-url]: https://www.facebook.com/kanapka.rimvydas
[instagram-shield]: https://img.shields.io/badge/-instagram-C5346E.svg?style=for-the-badge&logo=instagram&logoColor=white
[instagram-url]: https://www.instagram.com/rimvydaskanapka
