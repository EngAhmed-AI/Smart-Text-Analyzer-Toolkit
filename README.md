# 📝 Smart Text Analyzer & NLP Toolkit

A modular Python-based text processing and analytics toolkit. This tool provides interactive text analysis including keyword extraction, sentiment analysis, text similarity evaluation, and an in-memory Undo/Redo history tracking system using custom Stack data structures.

---

## 📌 Project Features

* **Flexible Text Input:** Supports direct text entry via CLI or importing text files (`.txt`) with robust file validation.
* **Text Normalization & Processing:** Strips punctuation, handles casing, and cleans text efficiently.
* **Data Structures (Undo/Redo):** Built a custom `Stack` class to handle text modification history (`Undo` & `Redo`).
* **Keyword Extraction:** Identifies top frequent words while filtering out custom English stop-words.
* **Text Similarity Detector:** Computes similarity percentage between two texts using Set operations.
* **Rule-Based Sentiment Analysis:** Calculates sentiment polarity (Positive, Negative, Neutral) and confidence scores.
* **Interactive CLI Dashboard:** Command-line dashboard allowing seamless execution of all operations.

---

## 🛠️ Project Structure

```text
smart_text_analyzer/
├── text_analyzer/
│   ├── utils.py          # Text cleaning & normalization
│   ├── analytics.py      # Word & character metrics
│   ├── keywords.py       # Stop-word filtering & keyword extraction
│   ├── similarity.py     # Text similarity computation
│   ├── sentiment.py      # Lexicon-based sentiment analysis
│   └── stack.py          # Custom Stack Data Structure
└── project.py            # CLI Application entry point




🚀 How to Run
Clone the repository:

Bash
git clone [https://github.com/EngAhmed-AI/Smart-Text-Analyzer-Toolkit.git](https://github.com/EngAhmed-AI/Smart-Text-Analyzer-Toolkit.git)
cd Smart-Text-Analyzer-Toolkit
Run the CLI Application:

Bash
python project.py

3. اضغط على `File` ⬅️ `Save As`.
4. اختر نوع الملف `All Files (*.*)` وضع الاسم: **`README.md`** واضغط حفظ.

---

الآن اصبحت الملفات جاهزة بالكامل على جهازك لسحبها ورفعها على GitHub! 🚀
