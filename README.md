<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=150&section=header&text=cURL%20to%20Fetch&fontColor=ffffff&fontSize=38" alt="Animated cURL to Fetch header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=900&center=true&vCenter=true&width=620&lines=cURL%20to%20Fetch;Convert%20requests%20to%20fetch()" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/curl-to-fetch?label=MIT)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/curl-to-fetch)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/curl-to-fetch?style=social)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/curl-to-fetch)

<img src="./assets/mark.svg" width="150" alt="Project illustration"/>

**Convert common cURL requests into readable JavaScript fetch() code. Input is parsed as text and never executed.**

</div>

## ✨ Overview

A small local converter for translating everyday cURL requests into JavaScript fetch snippets. It favors explicit supported options over silent guesses.

## 🚀 Features

- 🧾 Parses URLs, methods, headers, and common body flags.
- 🔒 Never executes shell commands or contacts the target URL.
- 🧩 Produces safely quoted JavaScript strings.
- ⚠️ Rejects unsupported flags with a clear error.

## 🧪 Demo

```text
$ python main.py 'curl -X POST -d "hello" https://example.test/api'
const response = await fetch("https://example.test/api", {
  method: "POST",
  body: "hello",
});
```

## ⚡ Quick Start

```bash
git clone https://github.com/CyberLoop-dev/curl-to-fetch.git
cd curl-to-fetch
python main.py 'curl -H "Accept: application/json" https://example.test/items'
```

## 🧰 Tech Stack

Python 3.10+ · Standard library only.

## 🗂️ Folder Structure

```text
curl-to-fetch/
├── main.py
├── tests/test_main.py
├── requirements.txt
├── .github/workflows/tests.yml
└── assets/mark.svg
```

## 🗺️ Roadmap

- [x] Common request methods, headers, and body flags
- [x] Unit tests and CI
- [ ] Additional cURL option coverage
- [ ] Optional TypeScript output

## 🤝 Contributing

Open an issue for a reproducible conversion case. Add tests for new flags and document unsupported behavior.

## 📄 License

MIT — see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated footer wave"/></div>
