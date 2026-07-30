# Tomato Leaf Disease Classifier (CV7)

Binary image classification distinguishing **Tomato Bacterial Spot** vs **Tomato Target Spot**, built for GET 324 (AI, Machine Learning and Convergent Technologies) — Laboratory Exercise 10 Mini-Project, Group CV7, Civil Engineering.

## Dataset
- Source: [PlantVillage Dataset — Kaggle (emmarex/plantdisease)](https://www.kaggle.com/datasets/emmarex/plantdisease)
- Classes used: `Tomato_Bacterial_spot`, `Tomato_Target_Spot`
- Split: 80% train / 10% validation / 10% test

## Models Trained
| Model | Test Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Custom CNN | **99.72%** | 100.00% | 99.29% | 99.64% |
| MobileNetV3Small (Transfer Learning) | 98.87% | 97.90% | 99.29% | 98.59% |

**Best model:** Custom CNN — saved as `models/model.keras` and used in the deployed app.

## How to Use the App
1. Open the deployed Streamlit link (see repo description / About section).
2. Upload a tomato leaf image (jpg/jpeg/png).
3. The app displays the predicted class (Bacterial Spot or Target Spot) with confidence percentages for both classes.

## Project Structure
├── app.py
├── requirements.txt
└── models/
└── model.keras

## Deployment
Built with TensorFlow/Keras, deployed as a Streamlit Community Cloud app. Model trained in Google Colab.

## Group Members
| Name | Registration Number | GitHub Username |
|---|---|---|
| Mandu, Harrison Udoh | 22/EG/CV/1453 | Harrison11-civil |
| Effiong, Victor Kufre | 22/EG/CV/1493 | Effiong-Victor |
| Utip, Joseph Kufre | 22/EG/CV/1433 | josephkufre093-Civil |
| Tom, Godwin Godwin | 22/EG/CV/1443 | Tom-Godwin |
| Etim, Godwin Okon | 22/EG/CV/1463 | Godwin-Etim |
| Mfonabasi Anwanga Obot | 22/EG/CV/1413 | Mfonabasi-Obot |
| Udom, Erikan Idongesit | 22/EG/CV/1483 | erikan1d |
| Etukudoh, Isreal Effiong | 22/EG/CV/1513 | Etukudoh-Isreal |
| Idimudo, Favour Ime | 22/EG/CV/1423 | Favour-Idimudo |
