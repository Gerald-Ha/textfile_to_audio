# 🎤 Bark AI Text-to-Speech (TTS) Project

🚀 **Bark AI** is a powerful AI text-to-speech program. This program, `bark_textfile.py`, converts the text content from the `text.txt` file into speech and saves it as `output.wav`.

## 📌 Features
👉 **Automatic text processing** – Reads the content of `text.txt` and converts it into speech.  
👉 **Supports long texts** – The script automatically splits long texts into meaningful paragraphs.  
👉 **Single audio file** – All sections are merged into one file.  
👉 **Automatic playback** – The audio file is played automatically after processing.  

---

## 🔧 Installation
### 1️⃣ Requirements
- **Python 3.8 or newer**
- **pip** (Python package manager)
- **Windows, Linux, or macOS**
- **Powerful hardware recommended**
  - The processing time can be significant. In a test using an **Nvidia RTX 4070** and **96GB RAM**, the conversion of a text file containing:
    - **811 words**
    - **4,897 characters (without spaces)**
    - **5,690 characters (with spaces)**
    - **27 sentences**
    - **30.0 words per sentence on average**
    - **Estimated reading time: 6.2 minutes**
  
    still took **over an hour** to complete. We strongly recommend using a high-performance GPU and ample RAM.

### 2️⃣ Clone the repository
If you have Git installed:
```sh
git clone https://github.com/your-github-username/bark-ai-tts.git
cd bark-ai-tts
```
Alternatively, you can download the ZIP file from GitHub and extract it.

### 3️⃣ Create and activate a virtual environment
```sh
python -m venv venv
```
- **Windows (CMD/PowerShell):**  
  ```sh
  venv\Scripts\activate
  ```
- **Linux/macOS:**  
  ```sh
  source venv/bin/activate
  ```

### 4️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

---

## 🎤 Usage
1. Write the desired text in **`text.txt`**.
2. Run the script:
   ```sh
   python bark_textfile.py
   ```
3. The script processes the text and saves the speech output as **`output.wav`**.
4. The file is played automatically.

### 🔍 How does `bark_textfile.py` work?
- The script reads the content from the `text.txt` file.
- If the text is too long, it is automatically split into smaller chunks.
- Each section is converted into speech using Bark AI.
- All generated audio data is merged into a single file: `output.wav`.
- After processing, `output.wav` is played automatically.

---

## 🛠 Troubleshooting
If the script is not working:
- Make sure you are using the **correct Python version (3.8 or newer)**.
- If **Bark AI has trouble loading the models**, check the file:
  ```
  venv\Lib\site-packages\bark\generation.py
  ```
  and replace the following line (around line 212):
  ```python
  checkpoint = torch.load(ckpt_path, map_location=device)
  ```
  with:
  ```python
  checkpoint = torch.load(ckpt_path, map_location=device, weights_only=False)
  ```
- If the file **does not play**, open it manually (`output.wav`).

---

## 🌟 License
This project is licensed under the **MIT License**.  
More information can be found in the [`LICENSE`](LICENSE) file.

---

## 💡 Credits
- **Bark AI** – Open-source text-to-speech model  
- **PyTorch** – Deep learning framework  

---

