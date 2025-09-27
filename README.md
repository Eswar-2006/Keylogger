# Educational Keylogger — Internship Project

> ⚠️ **Strict Disclaimer:** This repository contains an *educational* keylogger implemented solely for learning and defensive cybersecurity purposes. **Do not** run this code on systems you do not own or have explicit written permission to test. Unauthorized use is illegal and unethical.

---

## Project Overview

A simple, minimal keylogger prototype built as part of a cybersecurity training / internship task. The goal is to demonstrate how keyboard-event capture and local logging work so learners can understand attack techniques and build detection/mitigation strategies.

This project is intended to be used **only** in isolated lab environments (virtual machines or disposable test systems) and never on production or third-party machines.

---

## Features

* **Keystroke Count per Word:** Tracks how many times each distinct word was typed during a logging session and stores counts in a structured summary file.
* **Instant Letter Capture:** Records the exact letters pressed at any given instant (timestamped), allowing inspection of input at precise moments.
* **Paragraph Reconstruction:** Reassembles logged keystrokes into paragraph-style content so you can view the typed text in a human-readable format (with timestamps and simple formatting).
* **Configurable Output:** Choose separate outputs for counts, instant letter logs, and reconstructed paragraphs (e.g., `keyfreq.txt`, `keylog.txt`, `keyparagraph.txt`).
* **Filtering & Privacy:** Options to exclude certain keys (e.g., passwords or sensitive inputs) and keep all logs local for privacy and safety.

---

## Requirements

* Python 3.8+ (or whichever runtime your implementation uses)
* Platform-specific packages listed in `requirements.txt`

---

## Installation

```bash
# clone the repo
git clone https://github.com/Eswar-2006/keylogger.git
cd <repo-name>

# create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\\Scripts\\activate  # Windows

# install dependencies in vscode and run the keylogger.py file
pip install pynput
```

---

## Usage

> Only run in a controlled test environment (VM or isolated machine).

```bash
# Basic run (example)
python keylogger.py --output logs.txt

# Stop the logger (esc) and inspect logs.txt
```

Replace `keylogger.py` and flags with your actual filenames and arguments.

---

## Safe Usage & Legal Notice

* **Authorized use only:** Run this code only on machines you own or where you have explicit written permission.
* **Test environments:** Use virtual machines or disposable test systems to avoid accidental harm.
* **Do not share:** Do not distribute logs containing real user keystrokes or sensitive data.
* **Local analysis only:** Logs remain local — do not send or upload them to public servers unless anonymized and permitted.

If you are unsure about the legality or ethics of running this project in your jurisdiction or environment, seek guidance from a supervisor or legal counsel.

---

## Detection & Prevention (Learning Focus)

This repository is intended to teach both offensive technique and defensive detection. Consider adding or studying the following detection/prevention ideas:

* Monitor for unexpected processes or programs that hook keyboard events.
* Use endpoint detection tools that flag applications registering global hooks.
* Restrict execution policies and use application allowlists.
* Regularly scan for unknown autorun entries or suspicious services.
* Educate users about phishing and the risks of running unknown binaries.

---

## Project Structure (example)

```
README.md
requirements.txt
keylogger.py
detector.py         # optional: simple detection heuristics
utils/
  └─ config.py
logs/
  └─ example_log.txt
```

---

## Contributing

Contributions are welcome but must follow the project’s educational intent. Suggested improvements:

* Add detection modules and heuristics.
* Provide safe, reproducible lab playbooks and VM snapshots.
* Add unit tests for non-malicious components.

Before submitting a pull request, ensure your changes do not make the project easier to abuse and include clear documentation.

---

## Attribution

Developed as part of an internship / cybersecurity training exercise.

---

## License

Choose an appropriate license. Example: `MIT License — educational use only` (note: license does not override laws or permissions).

---

*If you want, I can tailor this README to explicitly mention your SkillCraft internship, include exact filenames used in your project, or generate a `requirements.txt` and example `keylogger.py` stub.*
