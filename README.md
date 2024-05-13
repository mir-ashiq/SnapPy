# SnapPy: Automate Sending Snaps on Snapchat (Python)**

**Tired of manually sending Snaps? SnapPy automates the process using Selenium and Python, freeing up your time for more important things.**

**Features:**

* Effortlessly login using saved cookies (no more re-entering credentials)
* Send Snaps to multiple users in a single go, saving time and effort
* Lightweight and easy-to-use script, perfect for beginners

**Disclaimer:**

This script is for educational purposes only. Please use it responsibly and adhere to Snapchat's terms of service.

**Installation:**

1. **Prerequisites:** Ensure you have Python (version 3 recommended) and pip (Python's package manager) installed on your system. You can verify this by running `python --version` or `python3 --version` and `pip --version` in your terminal. If not installed, download them from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. **Install Dependencies:** Open your terminal or command prompt and navigate to the directory where you cloned or downloaded the SnapPy repository. Then, run the following command:

   ```bash
   pip install selenium webdriver-manager pickle
   ```

**Usage:**

1. **Download ChromeDriver:** Head over to [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) to download the appropriate ChromeDriver version for your Chrome browser. Extract the downloaded file to a location accessible by your system (e.g., your system PATH).
2. **Prepare Cookies (Optional):** If you want to avoid manual login, you can save your Snapchat login cookies. Log in to Snapchat on your browser, then navigate to `chrome://settings/cookies` and search for Snapchat cookies. You can then export them and place the file (e.g., `cookies.pkl`) in the same directory as your SnapPy script.
3. **Run the Script:** Open your terminal/command prompt and navigate to the SnapPy directory. Then, run the script using:

   ```bash
   python snappy.py
   ```

**Configuration (Optional):**

- **`cookies.pkl`:** If you have a saved cookies file, the script will automatically attempt to use it for login. Otherwise, you'll be prompted to enter your username and password.
- **`usernames.txt` (Optional):** Create a text file named `usernames.txt` in the same directory as the script and list the usernames of the recipients you want to send Snaps to, each on a separate line. The script will automatically iterate through this list.

**Example `usernames.txt`:**

```
user1
user2
user3
```

**Limitations:**

- Sending Snaps with text or attachments is not currently supported.
- This script relies on browser automation and may require adjustments if Snapchat's login process or website structure changes significantly.

**Contributing:**

We welcome contributions to improve SnapPy. Feel free to fork the repository, make changes, and submit pull requests.

**License:**

SnapPy is licensed under the MIT License. See the `LICENSE` file for details.
