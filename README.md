# 🌸 Menstrual Health Chatbot

A specialized chatbot for menstrual health education and information, built using fine-tuned T5 transformer model.

## 📋 Project Overview

This chatbot provides accurate, helpful information about menstrual health topics including:
- Menstrual cycles and periods
- Common menstrual disorders (PMS, PCOS, endometriosis)
- Menstrual hygiene and products
- Menstrual pain management
- Reproductive health education

## 🛠️ Technical Implementation

### Model Architecture
- **Base Model**: T5-small (60M parameters)
- **Fine-tuning**: Question-answering task with "question: " prefix
- **Training Data**: 531 Q&A pairs covering diverse menstrual health topics
- **Performance**: BLEU score of 0.45-0.51 on test set

### Key Features
- Generative question-answering using fine-tuned T5
- Professional web interface built with Gradio
- Domain-specific responses for menstrual health queries
- Example questions for user guidance

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Installation Steps

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd MenstrualHealth_Chatbot-main
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the chatbot**:
   ```bash
   python chatbot_ui.py
   ```

4. **Access the interface**:
   - Open your browser to `http://localhost:7860`
   - Or follow the link provided in the terminal

## 📊 Dataset

The chatbot was trained on a comprehensive dataset of menstrual health Q&A pairs covering:
- Basic menstrual cycle information
- Common symptoms and disorders
- Hygiene and product recommendations
- Pain management strategies
- Reproductive health education

### Data Processing
- **Preprocessing**: Text cleaning, lowercasing, missing value removal
- **Tokenization**: T5 tokenizer with max length 64
- **Splitting**: 90/10 train/validation split

## 🎯 Usage Examples

### Sample Conversations

**Q: What is a normal menstrual cycle length?**  
**A:** A normal menstrual cycle typically ranges from 21 to 35 days, with the average cycle lasting around 28 days.

**Q: How can I alleviate menstrual cramps?**  
**A:** Menstrual cramps can be alleviated through various methods including over-the-counter pain relievers, applying heat to the abdomen, gentle exercise, relaxation techniques, and dietary changes.

**Q: What are the signs of a heavy menstrual flow?**  
**A:** Signs of a heavy menstrual flow include soaking through one or more pads or tampons every hour for several consecutive hours, passing large blood clots, and experiencing symptoms like fatigue and shortness of breath.

## 🔧 Model Training Details

### Hyperparameters
- **Learning Rate**: 5e-5
- **Batch Size**: 8
- **Epochs**: 2
- **Max Length**: 64 tokens

### Experiment Results

| Experiment | Model | Learning Rate | Batch Size | Epochs | BLEU Score | Notes |
|------------|-------|---------------|------------|--------|------------|-------|
| 1 | T5-small | 5e-05 | 8 | 2 | 0.45 | Baseline; outputs short answers, some echoing |
| 2 | T5-small | 5e-05 | 8 | 4 | 0.51 | Longer training, more accurate, less echo |

## 📈 Performance Metrics

- **BLEU Score**: 0.45-0.51 (sentence-level BLEU on test set)
- **Qualitative Evaluation**: Provides relevant, domain-specific answers
- **Response Quality**: Short, informative answers suitable for chatbot interaction

## 🏗️ Project Structure

```
MenstrualHealth_Chatbot-main/
├── Notebok.ipynb              # Main training notebook
├── fix_notebook.py            # Notebook metadata cleaner
├── chatbot_ui.py              # Gradio web interface
├── requirements.txt           # Python dependencies
├── README.md                  # This documentation
├── best_model/                # Fine-tuned model files
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── ...
└── data/                      # Training data and results
    ├── Training Data.csv
    ├── test_cleaned.csv
    ├── train_tokenized.csv
    ├── experiment_table.csv
    └── ...
```

## 🎨 Interface Features

- **Clean Design**: Professional, user-friendly interface
- **Example Questions**: Pre-loaded examples for easy testing
- **Real-time Responses**: Instant answers from the fine-tuned model
- **Error Handling**: Graceful handling of edge cases
- **Mobile-Friendly**: Responsive design for various devices

## 🔒 Privacy & Safety

- **Local Processing**: All responses generated locally
- **No Data Storage**: User queries are not stored or logged
- **Domain-Specific**: Only responds to menstrual health related questions
- **Medical Disclaimer**: Information provided is educational, not medical advice

## 🤝 Contributing

This project demonstrates fine-tuning transformer models for domain-specific chatbots. For educational purposes only.

