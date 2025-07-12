# 📨 Mirsal

**Mirsal** (مرسال) is a lightweight CLI tool to view any log file live in your browser — from anywhere.

It starts a clean, scrollable log viewer server and exposes it via [Ngrok](https://ngrok.com/) with just one command.

> مرسال: Arabic for "messenger" — your log updates, delivered.

---

## 🚀 Features

- 🌐 Access your logs from anywhere via Ngrok
- 📄 View live logs in a styled browser interface
- 🔄 Auto-scrolls to the latest log lines
- 🪶 Lightweight & fast (Flask + Ngrok under the hood)
- ✅ No config needed — just run and go!

---

## 📦 Installation

```bash
pip install mirsal
````

---

## 🧪 Usage

```bash
mirsal <your_log_file>
```

Example:

```bash
mirsal slurm-12345.out
```

You’ll see:

```
🚀 Log viewer is live at: https://abc123.ngrok.io
```

Open that URL from your browser or mobile and watch logs live with automatic scrolling.

---


## 📜 License

MIT License

---

## 👨‍💻 Author

**Bashar Talafha**
Built with love for developers who love clean logs.

