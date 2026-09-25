<div align="center">

# ✦ UNIVERSAL FILE ORGANIZER

### **Automate. Organize. Simplify.**

A modern, open-source **Python file organization and automation platform** that transforms digital clutter into a clean, structured workspace — locally or through a beautiful web interface.

<br>

<img src="https://img.shields.io/badge/Python-3.8%2B-111827?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/FastAPI-0.110.0-0f766e?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Tailwind_CSS-UI-0f172a?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS">
<img src="https://img.shields.io/badge/License-MIT-c9a227?style=for-the-badge" alt="MIT License">

<br><br>

**Clean files. Clean workflow. Clean mind.**

<br>

<a href="https://github.com/webX22/python-universal-file-organizer">
  <img src="https://img.shields.io/badge/View%20on-GitHub-111827?style=for-the-badge&logo=github" alt="View on GitHub">
</a>

</div>

---

<div align="center">

## ✦ Overview

</div>

**Universal Python File Organizer** is an open-source full-stack automation application built to eliminate digital clutter.

Instead of manually sorting hundreds of files, the application automatically analyzes files and places them into professional categories such as:

`Documents` · `Images` · `Videos` · `Audio` · `Archives` · `Code` · `Spreadsheets` · `Presentations` · `Others`

The project combines a **Python automation engine**, a **FastAPI backend**, and a modern **web interface**.

It can operate directly on folders located on your computer or process files uploaded through the web interface.

---

<div align="center">

## ✦ Why Universal File Organizer?

</div>

| Problem                                           | Solution                       |
| ------------------------------------------------- | ------------------------------ |
| Downloads folder becomes cluttered                | Automatically categorize files |
| Hundreds of files need manual sorting             | Process them in bulk           |
| Different file extensions are difficult to manage | Extension-based classification |
| Users want a simple interface                     | Modern web dashboard           |
| Repetitive file management wastes time            | Python automation              |
| Files need to remain local                        | Local-first processing         |

---

<div align="center">

## ✦ Core Features

</div>

<table>
<tr>
<td width="50%">

### ⚡ Automatic Organization

Automatically detects file types and moves them into structured categories.

</td>
<td width="50%">

### 🗂️ Multi-Format Support

Designed to handle documents, images, archives, code, spreadsheets and more.

</td>
</tr>

<tr>
<td>

### 🖥️ Local Folder Mode

Point the application to a folder such as your Downloads directory and organize it automatically.

</td>
<td>

### 🌐 Web Upload Mode

Drag and drop files directly into the web interface and process them instantly.

</td>
</tr>

<tr>
<td>

### 🚀 FastAPI Backend

Uses FastAPI for a lightweight and high-performance Python API.

</td>
<td>

### ✦ Modern Interface

Clean frontend experience powered by Tailwind CSS.

</td>
</tr>

<tr>
<td>

### 🔒 Local Processing

Designed around local file automation so your files can remain on your own machine.

</td>
<td>

### 🧩 Open Source

MIT licensed and available for modification, improvement and redistribution.

</td>
</tr>
</table>

---

<div align="center">

## ✦ How It Works

</div>

```text
                    ┌──────────────────────┐
                    │     Your Files       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   File Detection     │
                    │   & Classification   │
                    └──────────┬───────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │       Organization Engine       │
              └───────────────┬─────────────────┘
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
         Documents         Images           Archives
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                    ┌──────────────────────┐
                    │  Organized Folders   │
                    └──────────────────────┘
```

---

<div align="center">

## ✦ Supported Categories

</div>

| Category         | Examples                            |
| ---------------- | ----------------------------------- |
| 📄 Documents     | PDF, DOC, DOCX, TXT, RTF            |
| 🖼️ Images       | JPG, JPEG, PNG, GIF, WEBP, SVG      |
| 🎬 Videos        | MP4, MKV, AVI, MOV, WEBM            |
| 🎵 Audio         | MP3, WAV, FLAC, AAC, OGG            |
| 📦 Archives      | ZIP, RAR, 7Z, TAR, GZ               |
| 💻 Code          | PY, JS, TS, HTML, CSS, PHP, JSON    |
| 📊 Spreadsheets  | XLS, XLSX, CSV, ODS                 |
| 📑 Presentations | PPT, PPTX, ODP                      |
| 📁 Others        | Unrecognized or unsupported formats |

> The classification system can be extended with additional file extensions and custom categories.

---

<div align="center">

# ✦ Installation

</div>

## 01 — Install Python

> **Already have Python 3.8+ installed?**
> Skip to the next step.

Check your current installation:

```bash
python --version
```

If Python is not installed, download it from:

**https://www.python.org/downloads/**

### Windows

During installation, make sure you enable:

```text
☑ Add python.exe to PATH
```

Then continue with the standard installation.

### macOS

Using Homebrew:

```bash
brew install python
```

Or download Python directly from:

**https://www.python.org/downloads/**

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## 02 — Verify Python & Pip

Open **Command Prompt**, **PowerShell**, **Terminal**, or your preferred shell.

Run:

```bash
python --version
pip --version
```

Example:

```text
Python 3.12.x
pip 24.x
```

### Windows Alternative

If `python` is not recognized, try:

```bash
py --version
```

and:

```bash
py -m pip --version
```

---

<div align="center">

# ✦ Get the Project

</div>

## 03 — Clone the Repository

Clone the project:

```bash
git clone https://github.com/webX22/python-universal-file-organizer.git
```

Enter the project directory:

```bash
cd python-universal-file-organizer
```

### Download Without Git

You can also download the repository directly from GitHub:

```text
GitHub
  ↓
Code
  ↓
Download ZIP
  ↓
Extract
  ↓
Open the project folder
```

---

<div align="center">

# ✦ Dependencies

</div>

## 04 — Install Required Packages

Install everything listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

The project uses packages including:

```text
FastAPI
Uvicorn
python-multipart
```

If your system uses `python3`:

```bash
pip3 install -r requirements.txt
```

---

<div align="center">

# ✦ Launch

</div>

## 05 — Start the Application

Run:

```bash
python main.py
```

On macOS/Linux:

```bash
python3 main.py
```

The server should start locally.

Then open your browser and visit:

```text
http://127.0.0.1:8000
```

You can use:

* Google Chrome
* Microsoft Edge
* Mozilla Firefox
* Safari

---

<div align="center">

# ✦ Using the Application

</div>

## Local Machine Mode

Use the local folder organizer when you want to organize an existing directory on your computer.

### Example

Suppose your Downloads folder contains:

```text
Downloads/
├── invoice.pdf
├── vacation.jpg
├── project.py
├── music.mp3
├── archive.zip
├── report.xlsx
└── presentation.pptx
```

Enter the folder path into the application:

```text
C:\Users\YourName\Downloads
```

Then click:

```text
RUN PYTHON SCAN
```

The application analyzes the files and organizes them into categories.

Example result:

```text
Downloads/
├── Documents/
│   └── invoice.pdf
│
├── Images/
│   └── vacation.jpg
│
├── Code/
│   └── project.py
│
├── Audio/
│   └── music.mp3
│
├── Archives/
│   └── archive.zip
│
├── Spreadsheets/
│   └── report.xlsx
│
└── Presentations/
    └── presentation.pptx
```

---

## Web Upload Mode

The web interface provides another way to organize files.

### Workflow

```text
Drag & Drop Files
        ↓
File Upload
        ↓
File Analysis
        ↓
Category Detection
        ↓
Automatic Sorting
        ↓
Organized Result
```

Simply drag files into the upload area and select:

```text
PROCESS & SORT
```

The backend processes the uploaded files and organizes them according to their detected type.

---

<div align="center">

# ✦ Project Architecture

</div>

```text
python-universal-file-organizer/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
└── uploads/
```

> Your actual directory structure may differ depending on the current implementation.

---

<div align="center">

# ✦ Technology Stack

</div>

<table>
<tr>
<td align="center" width="25%">

### 🐍

**Python**

Core automation engine

</td>
<td align="center" width="25%">

### ⚡

**FastAPI**

Backend API

</td>
<td align="center" width="25%">

### 🎨

**Tailwind CSS**

Frontend styling

</td>
<td align="center" width="25%">

### 📁

**OS / Shutil**

File operations

</td>
</tr>
</table>

### Backend

* Python 3.8+
* FastAPI
* Uvicorn
* python-multipart
* `os`
* `shutil`

### Frontend

* HTML
* Tailwind CSS
* JavaScript

---

<div align="center">

# ✦ API Documentation

</div>

Because the application uses FastAPI, interactive API documentation is available when the server is running.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

These interfaces are useful when developing, testing, or extending the API.

---

<div align="center">

# ✦ Customization

</div>

The organizer is designed to be extensible.

You can customize:

* File categories
* File extensions
* Destination folders
* Organization rules
* Upload behavior
* API endpoints
* Frontend design
* Folder naming
* Automation logic

For example:

```python
"Design": [".psd", ".ai", ".fig", ".sketch"]
```

Or extend an existing category:

```python
"Images": [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".svg",
    ".avif"
]
```

---

<div align="center">

# ✦ Development

</div>

### Create a virtual environment

Recommended for development:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

<div align="center">

# ✦ Production Considerations

</div>

This project is primarily designed for local use and development.

Before exposing it publicly or deploying it to a server, consider implementing:

* Authentication
* Authorization
* File-size limits
* Upload validation
* File-name sanitization
* Rate limiting
* Secure temporary storage
* Path traversal protection
* Logging
* Error handling
* HTTPS
* Environment variables
* Production ASGI configuration

**Never expose arbitrary filesystem access to untrusted users without appropriate security controls.**

---

<div align="center">

# ✦ Security

</div>

Because this application works with files and filesystem paths, security should be considered carefully when modifying or deploying it.

### Important principles

```text
Validate paths
      ↓
Validate uploads
      ↓
Restrict accessible directories
      ↓
Sanitize filenames
      ↓
Limit upload sizes
      ↓
Handle errors safely
```

For local personal use, the application can operate directly on your machine.

For public deployment, additional security controls are strongly recommended.

---

<div align="center">

# ✦ Roadmap

</div>

### Current

* [x] Python automation engine
* [x] FastAPI backend
* [x] Web interface
* [x] Local folder organization
* [x] File upload processing
* [x] Automatic categorization

### Planned

* [ ] Custom category editor
* [ ] File preview
* [ ] Organization history
* [ ] Undo organization
* [ ] Advanced organization rules
* [ ] Duplicate detection
* [ ] File statistics dashboard
* [ ] Custom folder templates
* [ ] Scheduled organization
* [ ] Dark / light themes
* [ ] Improved error reporting
* [ ] Docker support
* [ ] Automated testing
* [ ] Desktop application

---

<div align="center">

# ✦ Contributing

</div>

Contributions are welcome.

### 1. Fork the repository

```bash
git clone https://github.com/webX22/python-universal-file-organizer.git
```

### 2. Create a branch

```bash
git checkout -b feature/my-new-feature
```

### 3. Make your changes

Improve the application, fix bugs, or add new functionality.

### 4. Commit

```bash
git add .
git commit -m "Add new file organization feature"
```

### 5. Push

```bash
git push origin feature/my-new-feature
```

### 6. Open a Pull Request

Explain what you changed and why.

---

<div align="center">

# ✦ License

</div>

This project is released under the **MIT License**.

See the [`LICENSE`](LICENSE) file for the complete license text.

---

<div align="center">

# ✦ Support the Project

If Universal File Organizer helped improve your workflow, consider supporting the project:

<br>

⭐ **Star the repository**

🍴 **Fork the project**

🐛 **Report bugs**

💡 **Suggest improvements**

🔧 **Submit pull requests**

<br>

Every contribution helps the project grow.

---

### Built with Python · FastAPI · Tailwind CSS

**Universal File Organizer**

*Organize less. Automate more.*

<br>

<a href="https://github.com/webX22/python-universal-file-organizer/stargazers">
<img src="https://img.shields.io/github/stars/webX22/python-universal-file-organizer?style=for-the-badge&logo=github&label=STARS" alt="GitHub Stars">
</a>

<a href="https://github.com/webX22/python-universal-file-organizer/network/members">
<img src="https://img.shields.io/github/forks/webX22/python-universal-file-organizer?style=for-the-badge&logo=github&label=FORKS" alt="GitHub Forks">
</a>

<a href="https://github.com/webX22/python-universal-file-organizer/issues">
<img src="https://img.shields.io/github/issues/webX22/python-universal-file-organizer?style=for-the-badge&logo=github&label=ISSUES" alt="GitHub Issues">
</a>

<br><br>

<a href="https://github.com/webX22">
  <strong>GitHub · webX22</strong>
</a>

</div>
