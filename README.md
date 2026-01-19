# Guilt-3P
Guilt 3P (is read as Guilt Trip)

The 3Ps stands for **Petty Productivity Patrol** or an old tamil meme **Parama-Poi-Padi da** Guilt-3P is a simple CLI system - By dev for devs - which roasts you when you get distracted. This makes you guilt trip instead of blocking webpages (no blocking only roasting)

---

## 🤡 Stop Being a Failure: A Detailed Guide

Do you have the attention span of a goldfish on espresso? Do you find yourself doom-scrolling on Youtube or Insta when you should be debugging that memory leak? 

Welcome to **Guilt-3P**, the only productivity tool that doesn't "block" sites—because blocking is for cowards. I believe in **Psychological Warfare**. 

### 🛠️ Features (or "Ways I hurt you")

*   **The Roaster-Speaker™**: My system uses Text-to-Speech to literally yell at you. It won't stop until your self-esteem hits rock bottom. Imagine being roasted by a machine (that too in the default google voice). That should make you feel more than shameful 😂.
*   **The Hall of Shame**: Every time you visit a "forbidden" site, we log it in a file called `HALL_OF_SHAME.txt` right on your desktop. Perfect for when your parents, partner, or boss walk by.
*   **Aggressive Context Switching**: Watching YouTube? *BAM.* Guilt-3P will forcefully teleport your VS Code or Terminal to the front. You can run, but you can't hide from your unfinished PRs.
*   **The Nag Engine**: Constant notifications that remind you how disappointed your ancestors are in your lack of focus.

### 🍱 The "Secret Sauce" (Data)
We have curated lists of:
*   `forbidden.py`: Sites that trigger the roast (your digital sins).
*   `roasts.py`: High-quality, artisanal insults crafted for maximum emotional damage.
*   `nagging.py`: Small pokes to keep you awake.
*   `praises.py`: Rare occurrences when you actually do work (don't get used to it, you're still a slacker).

### 🚀 How to start your misery (For local running)
1. **Clone** : `git clone https://github.com/Astrasv/Guilt-3P` and `cd Guilt-3P`
2.  **Setup**: Install dependencies using `uv sync`.
3.  **Ignition**: Run the main script: `python tracker.py`.
4.  **The Test**: Open a browser and add the `src/guilt-3p/asset/extensions` folder as a extention.
5.  **The Result**: Cry as your computer tells you how useless you are while forcing you back to your terminal.

### ⚠️ Disclaimer
This tool is not responsible for:
*   Broken monitors.
*   Loss of friends (because you're always "working" but actually being roasted).
*   The fact that you still haven't finished that side project from 2022.


## Installation (as python package)

```bash
pip install -e .
```

## Setup

1.  **Initialize Config**: Create a customization file for your own roasts/forbidden sites.
    ```bash
    guilt-3p init-config
    ```
    This creates a `config.json` (location shown in output) where you can add:
    - `custom_roasts`: List of strings.
    - `custom_forbidden`: List of domain keywords (e.g., "twitter").
    - `custom_browsers`: List of browser process names.

2.  **Install Extension**: The browser extension is required to track URLs.
    ```bash
    guilt-3p setup-extension
    ```
    Follow the on-screen instructions to load the unpacked extension in Chrome/Edge/Brave.

## Usage

### Standard CLI Mode
Runs the tracker with console output.
```bash
guilt-3p run
```
Commands while running:
- `break 5`: Take a 5-minute break.
- `quit`: Exit.


## Customization (IN BETA MIGHT BREAK)

You can edit `config.json` to personalize your experience.

Example `config.json`:
```json
{
  "general": {
    "extend_defaults": true
  },
  "custom_roasts": [
    "Why are you watching cat videos?",
    "Your code is crying."
  ],
  "custom_forbidden": [
    "reddit",
    "youtube"
  ]
}
```

**Git😉 back to work.** Adios!!!

