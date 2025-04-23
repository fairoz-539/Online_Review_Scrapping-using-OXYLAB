
# Online Review Scrapping using OXYLAB

Scrapping Reviews from [AmbitionBox](https://www.ambitionbox.com/reviews/coca-cola-company-reviews) website.

---

## 📝 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 About the Project

This project demonstrates how to scrape employee reviews of companies from the [AmbitionBox](https://www.ambitionbox.com/reviews) website using the OXYLAB API. The collected data can be used for analysis to better understand employee sentiments, company reviews, and various metrics provided on the platform.

### Purpose
- Extract and store reviews programmatically using web scraping techniques.
- Analyze the collected data for actionable insights.

---

## ✨ Features

- Scrape company reviews efficiently using OXYLAB's web scraping API.
- Handle dynamic content and captcha challenges seamlessly.
- Output the scrapped data in a structured format (e.g., JSON or CSV).
- Modular Python scripts for easy customization and extension.

---

## ⚙️ How It Works

1. **OXYLAB API**: Utilized to bypass website restrictions and scrape data without direct interaction.
2. **Target Pages**: The script scrapes reviews from the [Coca-Cola Company review page](https://www.ambitionbox.com/reviews/coca-cola-company-reviews).
3. **Steps**:
   - Set up OXYLAB API credentials.
   - Send requests to the AmbitionBox review pages.
   - Parse the HTML content to extract relevant data like review titles, ratings, and review descriptions.
   - Save the extracted data to a file for further analysis.

---

## 🛠️ Technologies Used

- **Python**: Core programming language used to implement the scraper.
- **OXYLAB API**: For bypassing restrictions and scraping dynamic data.
- **BeautifulSoup**: For parsing HTML content.
- **Requests**: For handling HTTP requests.

---

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- An OXYLAB account with API access
- Git

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fairoz-539/Online_Review_Scrapping-using-OXYLAB.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Online_Review_Scrapping-using-OXYLAB
   ```
3. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate         # On Linux/Mac
   venv\Scripts\activate            # On Windows
   ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

1. **Configure OXYLAB API Credentials**:
   - Add your OXYLAB API key and other required details.

2. **Run the Scraper**:
   ```bash
   python scraper.py
   ```

3. **Output**:
   - Extracted data will be saved to a file (e.g., `output.json` or `output.csv`) in the project directory.

---

## 📂 Folder Structure

```
Online_Review_Scrapping-using-OXYLAB/
├── scraper.py          # Main script to run the scraper
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── output/             # Folder where scraped data will be saved
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "What you did"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---
