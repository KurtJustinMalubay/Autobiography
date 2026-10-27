# Kurt Justin J. Malubay — Autobiography & Portfolio

CSIT 349 · Applied AI · Section F1 · Instructor: Jun Albert S. Pardillo

A single-page Streamlit portfolio: autobiography, skills chart, projects, and a
feedback form. Genshin Impact–inspired UI with light/dark mode toggle.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Assets you need

Place these files in the `assets/` folder:

| File | Purpose | Required? |
|------|---------|-----------|
| `profile.jpg` | Your photo for the Home page hero section | Yes |
| `infinitus.jpg` | Key art or screenshot of the Infinitus project | Yes |
| `tlgms.png` | Screenshot of the TLGMS prototype | Yes |
| `cv.pdf` | Your résumé PDF for download button | Optional |

## Structure

```
kurt_portfolio/
├── app.py              ← main app (single file)
├── requirements.txt    ← dependencies
├── README.md           ← this file
└── assets/
    ├── profile.jpg     ← YOUR PHOTO
    ├── infinitus.jpg   ← INFINITUS KEY ART
    ├── tlgms.png       ← TLGMS SCREENSHOT
    └── cv.pdf          ← YOUR RESUME (optional)
```
