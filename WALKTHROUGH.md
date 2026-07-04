# DyslexiEase Standalone Desktop App - Walkthrough & Features

Welcome to **DyslexiEase**, an accessible learning assistant designed specifically to help dyslexic students study, read, and understand academic topics without losing exam-grade detail.

---

## 🚀 How to Run the Application

From VS Code:
1. Open a **New Terminal** (`Ctrl + \``).
2. Paste this command and press **Enter**:
   ```powershell
   .\venv\Scripts\python main.py
   ```
*The app window will immediately launch on your desktop. No browser tabs or network ports are opened!*

---

## 📷 Multimodal Scanners (OCR Worksheet Scan)
Located in the **1. Enter Lesson** tab:
1. **Upload Photo**: Click this to select any image of a textbook page or school worksheet. Gemini Vision OCR will extract the text.
2. **Live Webcam Scan**: Click this to activate your computer's webcam inside the app. Hold your printed sheet steady up to the lens, click **Capture & Scan Text**, and Gemini will instantly transcribe it.

---

## 📖 Accessibility Reading Controls
Located in the **2. Reader view** tab:
- **Bionic Reading Toggle**: Bolds the first half of words to serve as visual eye anchors.
- **Reading Ruler Toggle**: Adds a yellow horizontal tracking line that follows your mouse to prevent line-skipping.
- **Color Overlays (Irlen Filters)**: Low-contrast backgrounds (Cream, Soft Yellow, Pastels) to eliminate page vibrating/visual stress.
- **Synchronized Text-to-Speech (TTS)**: Reads text aloud and highlights the spoken word dynamically.
- **💡 AI Simplify Layout**: Spaces out paragraphs into short sentences, sections, and clear bullet points without stripping out key facts, resolving visual crowding for easier reading.

---

## 🛡️ Academic Terminology Retention (Self-Detecting Intelligence)
We have enforced strict guardrails to prevent AI over-simplification. The system **automatically detects the intellectual level** of the input lesson text (from elementary school to advanced university research) and matches that exact level of detail, equations, and vocab.
- **Interactive Keywords**: Academic terms are highlighted with a dotted line in the Reader View. Hover over them to view a kid-friendly explanation in a glassmorphic tooltip box.

---

## 🎨 Picture Generator (Visual Diagrams & Storyboards)
Located in the **3. Picture Generator** tab (formerly Comic Strip):
- **Choose Visual Format:**
  - **📊 Labeled Diagram:** Generates 1 detailed, clean, text-free background illustration. The app then places **crisp HTML labels** at coordinate offsets on top of the image!
    - Tapping an overlay label reads the term and its description aloud (vocal reinforcement).
    - Prevents blurry, scrambled AI image-rendering text.
  - **📷 Visual Storyboard:** Generates 3 to 6 step-by-step sequential illustrations explaining chronological processes (e.g. Water Cycle steps, Photosynthesis inputs/outputs).
- Press **Change Format** at any time to switch visual rendering styles!

---

## 🎙️ Auditory Study Buddy (Siri-Style Voice Orb)
Located in the **5. Study Buddy** tab:
- **Glowing Blue Voice Orb:** Replaces the standard typing chat boxes with a futuristic, animated holographic orb!
- **Voice Assistant Workflow:** Tap directly on the orb, speak your question, and Pip will automatically process your voice, transcribe it, and **speak the answer back to you**!
- **Transcript Logs:**
  - Realtime subtitles display underneath the orb so you can read along.
  - **✏️ Wobble Checks (Inline Spelling):** Any typos or phrasing errors you speak or type get highlighted in the subtitles with a non-invasive orange wavy line. Hover over it to see the correction, or click to expand explanations on what it should have been.
  - **Full Logs:** Toggle the collapsible details box at the bottom to view the entire chat logs history.

---

## 🎮 Practice Game (Diagram Dash)
Located in the **6. Practice Game** tab:
- **No Hardcoded Levels:** Removed all static plant cell/water cycle SVG levels. The game is now 100% dynamic!
- **Choose Your Mode:**
  - **Custom Diagram Dash:** Automatically loads your active lesson's generated diagram! It blanks out the labels, turning them into dotted targets. Drag the cards from the tray and drop them onto the physical coordinates of the diagram!
  - **Vocabulary Matcher:** Drag lesson vocabulary cards onto their correct definition blocks. Shuffled and generated on-the-fly. Always active as a high-value default fallback!
- **Pace Levels:** Chill (no timer), Steady, or Fast (with decoy tokens).
- **Study Hints:** Making mistakes twice triggers Pip to speak a voice tip explaining the target part's role!
- Respects active sidebar overlays and fonts automatically.
- **XP / Level Up:** Earning correct matches yields XP which updates your Level badge globally in the header. Saved to browser memory.
