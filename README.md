# 📦 Inventory Forecasting & Optimization App

A user-friendly Streamlit web application that helps businesses **forecast product demand** and **optimize inventory levels** using advanced machine learning and time series techniques.

---

## 🚀 Live App

👉 [Click here to launch the app](https://inventory-forecasting-app-bu2annkoqfpx5jjgs5jayp.streamlit.app/)

---

## 📝 Features

✅ Upload your sales data in CSV or Excel format  
✅ Forecast future demand using Prophet  
✅ Automatically compute optimized inventory levels  
✅ Visualize trends and seasonality  
✅ Export the forecast and inventory plan

---

## 📄 Sample Input Format

Upload a file with the following columns:

| date       | product_id | units_sold |
|------------|------------|------------|
| 2024-01-01 | P001       | 45         |
| 2024-01-02 | P001       | 48         |
| 2024-01-03 | P001       | 50         |

- **`date`** must be in `YYYY-MM-DD` format  
- **`units_sold`** is required for forecasting  
- Multiple products supported

---

## 🖥️ Run Locally (for developers)

```bash
git clone https://github.com/your-username/inventory-forecasting-app.git
cd inventory-forecasting-app
pip install -r requirements.txt
streamlit run app.py
