# 🚀 Binance Futures Testnet Trading Bot

A simplified Python-based trading bot that places **MARKET** and **LIMIT** orders on the Binance Futures Testnet (USDT-M).
Built with clean architecture, CLI interface, logging, and proper error handling.

---

## 📌 Features

* ✅ Place **MARKET** and **LIMIT** orders
* ✅ Supports both **BUY** and **SELL**
* ✅ Command Line Interface (CLI) using `argparse`
* ✅ Input validation and error handling
* ✅ Structured project architecture
* ✅ Logging of API requests, responses, and errors
* ✅ Uses Binance Futures **Testnet**

---

## 🧠 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API client
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│   └── cli.py             # CLI entry point
│
├── logs/
│   └── trading.log        # Generated logs
│
├── .env                   # API credentials
├── README.md
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone <your-repo-link>
cd trading_bot
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Create Binance Testnet Account

* Visit: https://testnet.binancefuture.com
* Generate API Key and Secret

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

---

## ▶️ How to Run

⚠️ Important: Always run using module mode

---

### 🟢 MARKET Order

```
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

---

### 🔵 LIMIT Order

```
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 60000
```

---

## 📊 Sample Output

```
✅ Order Placed Successfully!
Order ID: 13004176925
Status: NEW
Executed Qty: 0.000
Avg Price: 0.0
```

---

## ⚠️ Important Notes

* Binance Futures requires **minimum notional value ≥ 100 USDT**
* On Testnet:

  * Orders may remain in `NEW` status
  * `Executed Qty` may be `0.0` due to low liquidity
* This is expected behavior and not a bug

---

## 📝 Logging

All logs are stored in:

```
logs/trading.log
```

Includes:

* API requests
* Responses
* Errors

---

## 🛡️ Error Handling

The application handles:

* Invalid user inputs
* API errors (Binance exceptions)
* Network failures
* Missing credentials

---

## 🧪 Assumptions

* User provides valid trading symbol (e.g., BTCUSDT)
* API keys are correctly configured in `.env`
* Orders are tested only on Binance Futures Testnet

---

## ⭐ Bonus Improvements (Optional)

* Add Stop-Limit or OCO order support
* Improve CLI UX using `Typer` or `Click`
* Add AI-based natural language command parsing (LangChain)

---

## 👨‍💻 Author

Santosh Gudikandula



