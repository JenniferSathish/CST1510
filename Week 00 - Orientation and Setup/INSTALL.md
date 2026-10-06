# Setting up for CST1510

Seven steps, once, before Week 1.
Prefer a visual version? See the
[Setup Guide](https://anna29.github.io/CST1510/setup-guide.html).

**Windows or Mac?** Everything is the same, except Windows uses `python` and
macOS uses `python3`.

---

## 1. Install three things

- **Python** from [python.org/downloads](https://www.python.org/downloads/).
  Windows: on the first screen, tick **"Add python.exe to PATH"**.
- **VS Code** from [code.visualstudio.com](https://code.visualstudio.com/).
  Then open Extensions (`Ctrl/Cmd + Shift + X`) and install **Python** and
  **Jupyter**, both by Microsoft.
- **Git** from [git-scm.com/downloads](https://git-scm.com/downloads),
  accepting the defaults.

## 2. Create your GitHub repository

Create a free account at [github.com](https://github.com/). Then click
**+** (top right) → **New repository**, name it `CST1510`, tick
**Add a README file**, and click **Create repository**.

## 3. Clone it into Documents

Open a terminal (Windows: **PowerShell**, Mac: **Terminal**) and run:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
cd Documents
git clone https://github.com/YOUR-USERNAME/CST1510.git
```

Use your own name, the email from your GitHub account, and your GitHub
username. This creates the folder `Documents/CST1510`.

To check your Git settings at any time:

```
git config --list
```

Look for `user.name` and `user.email` in the list. Press `q` to exit if the
list fills the screen.

## 4. Open the folder in VS Code

**File → Open Folder** → `CST1510`, then **Terminal → New Terminal**.
Use this terminal from now on.

Check which branch you're on and that it's linked to GitHub:

```
git branch -vv
```

You should see `* main` followed by `[origin/main]`. That means you're on the
`main` branch and it's linked to your repository on GitHub.

Every week's folder from Moodle goes inside `CST1510`, starting with this
Week 00 folder.

## 5. Add a `.gitignore` file

This tells Git which files never to upload. In VS Code, create a new file in
the `CST1510` folder, name it `.gitignore` (starting with a dot), paste this
in and save:

```
.venv/
__pycache__/
.ipynb_checkpoints/
.DS_Store
.env
```

## 6. Make a test file

Create `hello.py` in the `CST1510` folder:

```python
print("Hello from CST1510!")
```

Run it:

```
python hello.py       # Windows
python3 hello.py      # macOS
```

## 7. Push it to GitHub

```
git add .
git commit -m "Week 0 setup"
git push
```

The first time, VS Code asks you to sign in to GitHub: click **Allow** and
follow the browser window. Then open your repository on GitHub and check
`hello.py` and `.gitignore` are there.

**Done.** Every week from now on, finish the lab with the same three commands.

---

## If something goes wrong

| Problem | Fix |
|---|---|
| `python` not found (Windows) | Reinstall Python and tick "Add python.exe to PATH" |
| `python3` opens the Microsoft Store (Windows) | Use `python` on Windows |
| `fatal: not a git repository` | Open the `CST1510` folder in VS Code and use its terminal |
| A notebook won't run | Click **Select Kernel** (top right) and click **Install** if asked about ipykernel |

---

# Week 7: virtual environment and packages

You don't need this until Week 7.

**1. Create the environment and install the packages** in the VS Code
terminal:

```
python -m venv .venv                     # Windows
.venv\Scripts\activate

python3 -m venv .venv                    # macOS
source .venv/bin/activate

python -m pip install -r "Week 00 - Orientation and Setup/requirements.txt"
```

**2. Tell VS Code to use it:** `Ctrl/Cmd + Shift + P` →
**Python: Select Interpreter** → pick `.venv`. In notebooks, **Select Kernel**
→ `.venv`.

**3. Check it:**

```
python "Week 00 - Orientation and Setup/verify_setup.py"
```

Every line should say `OK`. Then push as usual.

If Windows says `running scripts is disabled`, run
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, answer `Y`, and try
again.
