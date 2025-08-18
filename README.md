# Spam Email Detector 🛡️

A machine learning-powered web application that detects spam emails with 98% accuracy using Random Forest classification.

![App Screenshot 1](/static/images/1.png)
![App Screenshot 2](/static/images/2.png)

## 🔍 Overview

This project combines:
- **Backend**: FastAPI with a trained Random Forest model (0.98 accuracy, 0.97 F1-score)
- **Frontend**: HTML/CSS with JavaScript for dynamic interactions
- **ML Pipeline**: TF-IDF vectorization and feature engineering

## ✨ Features

- Real-time spam detection
- Detailed analysis of email content
- Example emails for quick testing
- Dark mode UI with responsive design
- Confidence percentage visualization

## 🛠️ Technical Details

### Model Performance
| Metric       | Score  |
|--------------|--------|
| Accuracy     | 0.98   |
| F1-Score     | 0.97   |
| Precision    | 0.98   |
| Recall       | 0.97   |

### Tech Stack
**Backend**:
- Python 3.11
- FastAPI
- Scikit-learn
- Joblib (model persistence)

**Frontend**:
- HTML5/CSS3
- JavaScript (ES6)
- Font Awesome icons

**Machine Learning**:
- Random Forest Classifier
- TF-IDF Vectorization (5000 features)
- Custom text preprocessing

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spam-detector.git
   cd spam-detector
