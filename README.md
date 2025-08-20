#  Image Resizer Tool

##  Project Overview
This project is a simple **Image Resizer Tool** built with **Python** and the **Pillow** library.  
The main purpose of this tool is to **automate image resizing and format conversion** for all images in a given folder.  

By running this script, you can quickly resize images to a standard dimension (e.g., 800x800) and save them in a new output folder without having to do it manually.

---

##  Objective
- Resize and convert images in **batch** (multiple images at once).
- Automate repetitive image processing tasks.
- Learn how to work with **PIL (Python Imaging Library)** for real-world applications.

---

##  Tools & Libraries Used
- **Python** – Programming language.
- **os** – To handle folder and file paths.
- **Pillow (PIL)** – For image resizing and saving.

---

##  How It Works
1. The script reads all files from an **input folder**.
2. It checks if each file is an image.
3. Each image is resized to the specified size (e.g., `800x800`).
4. The resized images are saved into a separate **output folder**.
5. The script supports format conversion as well (e.g., `.jpg → .png`).

---

##  How to Use
1. Install dependencies:
   ```bash
   pip install pillow
