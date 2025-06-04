<h1 align="center">☁️ CloudBYP - Cloudflare Bypass Tool ☁️</h1>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.1-blue" />
  <img src="https://img.shields.io/badge/author-G4UR4V007-green" />
  <img src="https://img.shields.io/badge/status-active-brightgreen" />
</p>

<p align="center">
  <b>Find the real IP behind Cloudflare protection using Censys!</b>
</p>

---

## 🚀 Features

- 🔍 Discover origin IP of Cloudflare-protected domains.
- ⚙️ Integrates with <a href="https://censys.io">Censys API</a>.
- 🧠 Intelligent parsing with BeautifulSoup.
- 🧪 Easy-to-use CLI interface.

---

## 🛠️ Requirements

- Python 3.x
- Modules:
  - `requests`
  - `beautifulsoup4`

Install using:

```bash
pip3 install -r requirements.txt
```

Or manually:

```bash
pip3 install requests beautifulsoup4
```

---

## ⚙️ Configuration

Save your Censys API credentials in `config.json` like so:

```json
{
  "api_id": "YOUR_CENSYS_API_ID",
  "api_secret": "YOUR_CENSYS_API_SECRET"
}
```

---

## 📦 Usage

```bash
python3 CloudBYP.py --domain example.com
```

**Arguments:**

- `--domain` : Target domain name (protected by Cloudflare).

🔗 Example:

```bash
python3 CloudBYP.py --domain targetsite.com
```

---

## 📄 License

Licensed under the MIT License. See [LICENSE](LICENSE) for more info.

---

## 👤 Author

- **Name:** G4UR4V007  
- **GitHub:** [@0xgh057r3c0n](https://github.com/0xgh057r3c0n)

---

## ⚠️ Disclaimer

> This tool is for **educational and authorized testing only**. Unauthorized use is strictly prohibited.
