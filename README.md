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
```

2. **Install required Python packages**:

```bash
pip install -r requirements.txt
```

3. **Download and install ChromeDriver**:

- Go to the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/downloads).
- Download the version that matches your Chrome browser.
- Extract the downloaded file and note the path to `chromedriver`.

4. **Update `login.py` with the ChromeDriver path**:

- Open `login.py` in a code editor.
- Find the line `driver_path = "path/to/chromedriver"`.
- Replace it with the actual path to your `chromedriver`.

5. **Run the script**:

```bash
python login.py
```

---

### 🔑 Environment Variables

Create a `.env` file in the project root with the following content:

```
USER_NAME=your_email@example.com
PASS_WORD=your_password
```

- Replace `your_email@example.com` and `your_password` with your actual credentials.
- The `.env` file must be in the same directory as `login.js`.

---

### JavaScript + Playwright (`login.js`)

#### ✅ Requirements

- **Node.js** v16 or higher  
- **npm** (comes with Node.js)  
- **Chromium browser** (automatically installed via Playwright)

#### 🛠️ Setup Instructions

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

### 🔑 Environment Variables

Create a `.env` file in the project root with the following content:

```
USERNAME=your_email@example.com
PASSWORD=your_password
```

- Replace `your_email@example.com` and `your_password` with your actual credentials.
- The `.env` file must be in the same directory as `login.js`.

## ▶️ Run the Script

```bash
node login.js
```





