![yume-logo](https://github.com/user-attachments/assets/8b3802fa-e89b-4e44-8a0d-be5b318240a1)

# 🌙 Yume - Terminal Manga Downloader

**Yume** (夢) is a command-line tool born from insomnia and obsession — a script that scrapes the web to download and bundle manga chapters into PDFs. Feed it a URL pattern, tell it where to save, and it will walk the lonely digital alleys for you, gathering pages one by one... quietly.

## ✨ Features

- 🧾 Download manga by specifying a URL pattern with `{ch}` as the chapter placeholder.  
- 🎯 Custom CSS selector to target images.  
- 📚 Automatically compiles each chapter into a PDF.  
- 🧠 Simple terminal-based prompts.  
- 🌌 Works across a range of chapters (start ➝ end).  

## 🛠️ Installation

Clone this repo, install dependencies, and run away from your responsibilities.

```
git clone https://github.com/LxrdShadow/yume.git
cd yume
pip install -r requirements.txt
```

## 🧪 Usage

Run the app with:

```
python -m app.main
```

You'll be asked to provide:

- 🗂 **Destination Directory**: Where the PDFs should be saved.  
- 🏷 **Prefix**: A prefix for each output file (e.g. "Naruto_").  
- 🔗 **Chapter URL**: Use `{ch}` where the chapter number goes (e.g. `https://mangasite.com/naruto/chapter-{ch}`).  
- 🖼 **Image Selector**: CSS selector used to extract image URLs.  
- 🔢 **Start Chapter**: The first chapter to download.  
- 🔢 **End Chapter**: The last chapter to download.  

### Example

```
destination: ./downloads
prefix: Naruto_
url: https://example.com/manga/naruto-{ch}
selector: .manga-page img
from chapter: 1
to chapter: 3
```

This will create:

downloads/  
├── Naruto_1.pdf  
├── Naruto_2.pdf  
└── Naruto_3.pdf  

## ⚠️ Disclaimer

- This tool scrapes websites. Make sure you have permission to download the content.  
- I am not responsible for your sudden addiction to reading entire manga series offline.  
- Use ethically. Yume is just a dreamer, not a pirate. 🏴‍☠️  

## 💔 Why?

Because sometimes we can't sleep.  
Because the internet is noisy.  
Because manga saved us once, and we want to hold on to those pages.  

## 🧘 License

MIT. Do what you want, just don’t blame me if it becomes sentient.

---

> _"A dream that lingers too long becomes a memory. A memory that fades becomes code."_ – Yume
