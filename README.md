# Nurture Notes

## Description

An Organized Journaling Interface for Caretakers with Extended Functionality. 

This application essentially allows a user to write and flip through the pages of his or her journals with ease, creating a more comforting feel to the editor. It implements straightforward organization over years, and allows caretakers of all kinds to track progress through goals, write reflective narratives through the use of interactive (generated but customizable) prompts, and a simple way to collect memories, whether into the photo gallery, saved journals, or saved pages. 

## Installation

Open Terminal and Clone Repository:

```bash
git clone https://github.com/AmerikanischerAdler/nurture_notes
```

If python3 is not installed on your machine, run:

**MacOS:**

```bash
brew update 
brew install python3
``` 

**TIP**: For MacOS, be sure that homebrew is installed on your machine. If not, visit https://brew.sh to install.

**Ubuntu:**

```bash
sudo apt update 
sudo apt install python3
```

## Usage

1) Open Terminal

2) Navigate to nurture_notes Directory:

```bash
cd nurture_notes
```

3) Start Flask App:

*This will spin up a local backend server*

```bash
python3 app.py
```

If this doesn't work, try:

```bash
python3.11 app.py
```

**TIP**: You may need to install python3.11

4) Open Web Browser to New Tab or Window

5) Enter Server Address in Search Bar:

You may be able to simply click this link: http://127.0.0.1:5000/home

**TIP**: Make sure to have "/home" at the end of your server address

## Inspiration

My mother is a caretaker for special needs. Watching after her brother Jonathan throughout his entire life, she explained to me once an issue she'd been having with organizing her various documents. Over the years, her online documents of journal entries (when she would reflect at the end of the day on what Jonathan had learned, what had made him happy or upset, and whatever activities they'd done together that day) would grow so long, that they would become quite challenging to navigate through, especially in search of specific dates and memories. And that's when I resolved to design an application, which could organize journal entries, in a format most similar to a book, with some extended features such as checklists for goals, search bar functionality, and an image gallery for capturing every golden moment. 

