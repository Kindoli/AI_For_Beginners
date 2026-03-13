# SMS Spam Classification using Deep Learning

This project uses a **Deep Neural Network** built with **TensorFlow/Keras** to classify SMS messages as either **Spam** or **Ham** (not spam).

## 🚀 Overview
The goal of this project is to build a binary classifier that can process raw text data and predict whether a message is unwanted spam or a legitimate communication with high accuracy.

## 📊 Dataset
The dataset used is the [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset). 
- **v1 (Label):** `ham` or `spam`
- **v2 (Text):** The content of the SMS message

*Note: The dataset was loaded using `latin-1` encoding to handle special characters.*

## AI Pipeline

Text Data
   ↓
Data Exploration (pandas)
   ↓
Text Vectorization (TF-IDF)
   ↓
Train/Test Split
   ↓
Neural Network Model
   ↓
Prediction

## 🛠️ Tech Stack
- **Language:** Python
- **Environment:** Jupyter Notebook / VS Code
- **Libraries:** - `Pandas` for data manipulation
  - `Scikit-learn` for data splitting
  - `TensorFlow/Keras` for building the neural network

## 🧠 Model Architecture
The model is a **Sequential Neural Network** consisting of:
1. **Input Layer:** Dense layer (16 neurons, ReLU activation)
2. **Hidden Layer:** Dense layer (8 neurons, ReLU activation)
3. **Output Layer:** Dense layer (1 neuron, Sigmoid activation)

The model was compiled using the `Adam` optimizer and `binary_crossentropy` loss function.

## 📈 Performance
- **Epochs:** 10
- **Batch Size:** 32
- **Accuracy:** [98.03%]


## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/Kindoli/AI_For_Beginners.git)](https://github.com/Kindoli/AI_For_Beginners.git)

## Contacts

**LinkedIn:** https://www.linkedin.com/in/kindoli-edward-5058544a/
