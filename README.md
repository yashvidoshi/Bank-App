# 🏦 Bank-App

A simple yet functional **bank account creation web application** built using **Flask** and **Python**.  
Users can open a **Savings** or **Current** account, and all submitted data is validated, interest is calculated, and records are stored in a `.csv` file.

---

## 📌 Features

- Clean, responsive HTML form
- Gender dropdown (Male/Female/Other)
- Account type selection (Saving / Current)
- Interest calculation for Saving accounts
- Minimum balance validation
- Form submissions stored in `accounts_log.csv`
- Built using Flask backend + CSV data logging

---

## 💻 Technologies Used

- **Python 3**
- **Flask**
- **HTML5 / CSS3**
- **CSV (for data storage)**

---

## 🛠 How to Run Locally

1. Clone the repo or download the folder:
   ```bash
   git clone https://github.com/yashvidoshi/Bank-App.git
   cd Bank-App

2. Install Flask
   ```bash
    pip install flask
   ```
   Optional if you are using a virtual environment
    ```
    python3 -m venv venv
    source venv/bin/activate    # For macOS/Linux
    # OR
    venv\Scripts\activate       # For Windows
     ```
3. Run the Flask app:
   ```
   python backend.py
   ```
4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```


  

