# 🚀 Binance Futures Trading Bot (Testnet)

✨ **A real-world Python trading bot built on the Binance USDT-M Futures Testnet** ✨
This project demonstrates **hands-on experience with real exchange APIs**, secure credential management, CLI-based trading, logging, and production-style error handling.

> ⚡ Built to showcase practical skills for **Junior Python Developer / Crypto Trading Bot** roles.

---

## 🌟 Key Highlights

💹 Real Binance **USDT-M Futures Testnet** integration
🧠 Clean, reusable, object-oriented Python design
🖥️ Interactive **Command-Line Interface (CLI)**
🔐 Secure API key handling using environment variables
🪵 Detailed logging of API requests, responses & errors
🛡️ Safe handling of varying Binance API responses

---

## 🛠️ Tech Stack

* 🐍 **Language:** Python 3.10+
* 🌐 **API:** Binance Futures REST API
* 📦 **Library:** `python-binance`
* 🔑 **Secrets Management:** `python-dotenv`
* 📊 **Logging:** Python `logging` module

---

## 📂 Project Structure

```text
trading-bot/
├── bot.py              # Core trading logic (Binance Futures)
├── main.py             # CLI interface for placing orders
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Security & repository hygiene
├── bot.log             # Runtime logs (auto-generated)
└── README.md
```

---

## 🔐 Security Best Practices

🔒 API credentials are stored in a `.env` file
🚫 `.env` is excluded from version control using `.gitignore`
❌ Withdraw permissions are **disabled** on API keys

> ⚠️ **Never commit real API keys to GitHub.** This project follows industry-standard security practices.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/trading-bot.git
cd trading-bot
```

---

### 2️⃣ Create & Activate Virtual Environment (Recommended)

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Rename `.env.example` → `.env` and add your **Binance Futures Testnet** credentials:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

---

## ▶️ Running the Bot

```bash
python main.py
```

### 💬 CLI Input Example

```
Symbol (BTCUSDT): BTCUSDT
BUY or SELL: BUY
Quantity: 0.001
```

### ✅ Output Example

```
Order Placed Successfully
Order ID: N/A
Client Order ID: x-R4BD3S82...
Status: FILLED
Executed Qty: 0.001
Average Price: 96855.4
```

---

## 📊 Order Verification

🔎 **Via Binance UI (Demo Trading Mode):**

* Login: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
* Navigate to:

  * 📜 **Order History** → all orders
  * 📈 **Trade History** → executed trades
  * 💼 **Positions** → open positions

> ℹ️ Market orders execute instantly and may not appear in **Open Orders**.

---

## 🪵 Logging

All activity is logged automatically for debugging and audits:

```text
bot.log
```

Includes:

* 📤 API requests
* 📥 API responses
* ❗ Errors & exceptions

---

## ⚠️ Known Behavior

* Binance Futures API responses vary by order type
* Certain fields (e.g., `orderId`) may not always be present
* Code safely handles optional fields using `.get()` to avoid crashes

---

## 🧠 What This Project Demonstrates

✅ Real exchange API usage (not mocked)
✅ Understanding of Futures trading workflows
✅ Secure handling of sensitive data
✅ Production-ready Python practices
✅ Debugging and API response handling

---

## 🚀 Future Enhancements

✨ Limit & Stop-Limit orders
🛑 Stop-Loss & Take-Profit automation
📡 WebSocket live price streaming
📊 Strategy logic (Grid / TWAP)
📉 PnL & position monitoring
🖥️ Lightweight UI dashboard

---

## 👤 About the Developer

👩‍💻 **Piulee Mukharjee**
🎓 Computer Science Engineering Student
💡 Interested in Python, Crypto Trading Systems, AI & Backend Development

🔗 **LinkedIn:**
👉 [https://www.linkedin.com/in/piulee-mukharjee-14a54b266/](https://www.linkedin.com/in/piulee-mukharjee-14a54b266/)

---

## 📬 Submission Context

📌 **Role:** Junior Python Developer – Crypto Trading Bot
🏦 **Exchange:** Binance Futures Testnet
🐍 **Language:** Python

---

🔥 This project uses **real Binance APIs on Testnet** and reflects **industry-level trading bot architecture**.
Feel free to ⭐ the repository or connect with me on LinkedIn!
