# 🚀 Binance Futures Trading Bot (Testnet)

A **Python-based trading bot** that places real orders on the **Binance USDT-M Futures Testnet** using the official Binance API.
This project demonstrates **real-world API integration, secure credential handling, CLI interaction, logging, and error handling**.

---

## 📌 Features

* ✅ Binance **USDT-M Futures Testnet** integration
* ✅ Market orders (Buy / Sell)
* ✅ Command-line interface (CLI)
* ✅ Secure API key management using environment variables
* ✅ Robust error handling
* ✅ Detailed logging of API requests & responses
* ✅ Clean, reusable, object-oriented code structure

---

## 🛠 Tech Stack

* **Language:** Python 3.10+
* **API:** Binance Futures REST API
* **Library:** `python-binance`
* **Environment Management:** `python-dotenv`
* **Logging:** Python `logging` module

---

## 📂 Project Structure

```
trading-bot/
├── bot.py              # Core trading logic
├── main.py             # CLI interface
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Security & hygiene
├── bot.log             # Runtime logs (auto-generated)
└── README.md
```

---

## 🔐 Security Best Practices

* API credentials are stored in a `.env` file
* `.env` is excluded via `.gitignore`
* Withdraw permissions are **disabled** on API keys

> **Note:** Never commit real API keys to GitHub.

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

Rename `.env.example` → `.env` and add your credentials:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

---

## 🧪 Running the Bot

```bash
python main.py
```

### CLI Input Example

```
Symbol (BTCUSDT): BTCUSDT
BUY or SELL: BUY
Quantity: 0.001
```

### Output Example

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

### On Binance UI

* Login: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
* Navigate to:

  * **Order History** → for all orders
  * **Trade History** → for executed trades
  * **Positions** → for open positions

> Market orders fill instantly and may not appear in “Open Orders”.

---

## 🪵 Logging

All API interactions and errors are logged automatically:

```
bot.log
```

Includes:

* Order requests
* API responses
* Exceptions & failures

---

## ⚠️ Known Behavior

* Binance Futures API responses vary by order type
* Some fields like `orderId` may not always be present
* Code safely handles optional fields using `.get()`

---

## 🧠 What This Project Demonstrates

* Real exchange integration (not mocked)
* Practical understanding of Futures trading
* Secure handling of sensitive data
* Production-safe Python coding practices
* Debugging and API response handling

---

## 🚀 Future Improvements

* Limit & Stop-Limit orders
* Stop-Loss & Take-Profit automation
* WebSocket price streaming
* Strategy logic (Grid / TWAP)
* PnL & position monitoring
* Lightweight UI dashboard

---

## 📧 Submission Details

**Built by:** Piulee Mukharjee
**Exchange:** Binance Futures Testnet
**Language:** Python

---

✅ This project uses **real Binance APIs on Testnet** and demonstrates industry-standard trading bot architecture.
