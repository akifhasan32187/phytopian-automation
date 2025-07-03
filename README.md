# 🔐 Phytopian Login Automation

This repository contains two login automation scripts for [Phytopian](https://app.phytopian.com/login):

- `login.py`: Python + Selenium + PyAutoGUI
- `login.js`: JavaScript + Playwright

Each script automates:
- Login process
- Handling the "OK" popup using screen coordinates
- Clicking the avatar
- Logging out
- Closing the browser window

---

## ⚙️ Environment Setup

Below are the setup instructions for both Python and JavaScript environments.

---

### 🐍 Python + Selenium (`login.py`)

#### ✅ Requirements

- Python 3.7 or higher  
- Google Chrome browser  
- ChromeDriver (matching your Chrome version)  
- pip (Python package manager)

#### 🛠️ Setup Instructions

1. **Create and activate a virtual environment** (optional but recommended):

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 🔐 Login Automation with Playwright (JavaScript)

Automated login testing using [Playwright](https://playwright.dev/) with JavaScript. This project demonstrates how to automate web login flows using Chromium and Playwright, including interactions with UI popups.

## ✅ Requirements

- **Node.js** v16 or higher  
- **npm** (comes with Node.js)  
- **Chromium browser** (automatically installed via Playwright)

## 🛠️ Setup Instructions

```bash
# 1. Initialize a new Node.js project (if not already)
npm init -y

# 2. Install Playwright
npm install playwright

# 3. Install Playwright browsers (Chromium, Firefox, WebKit)
npx playwright install

# 4. Create your script file (if not already created)
touch login.js
```

## ▶️ Run the Script

```bash
node login.js
```





