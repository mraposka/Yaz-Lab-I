import csv
import re
import os
import numpy as np
import torch
from torch import nn
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Süre değerlerini saklamak için bir liste
time_data = []
labels = []
count = 0

# Geçerli çalışma dizinindeki tüm CSV dosyalarını al
current_directory = os.getcwd()  # Geçerli çalışma dizini
csv_files = [f for f in os.listdir(current_directory) if f.endswith('.csv')]

# Informer Modelini tanımlama (simplified version)
class InformerModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(InformerModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        lstm_out, (hn, cn) = self.lstm(x)
        output = self.fc(lstm_out[:, -1, :])  # Take the last time step
        return output


# Eğitim döngüsünü ve görselleştirmeleri güncellenmiş haliyle ekleme
def informerPrediction(time_data, label='Unknown'):
    # 1. Veriyi saniyeye dönüştürme
    def time_to_seconds(time_str):
        if ':' in time_str:
            minutes, seconds = time_str.split(':')
            return int(minutes) * 60 + float(seconds)
        else:
            return float(time_str)

    if not time_data:
        print(f"No time data found for {label}")
        return

    # Convert the time data to seconds
    time_series = np.array([time_to_seconds(t) for t in time_data])
    
    # 2. Veriyi ölçekleme
    scaler = MinMaxScaler()
    time_series_scaled = scaler.fit_transform(time_series.reshape(-1, 1))
    
    # 3. Giriş dizilerini oluşturma
    input_sequence_length = 2
    X = []
    y = []
    
    for i in range(len(time_series) - input_sequence_length):
        X.append(time_series_scaled[i:i + input_sequence_length])
        y.append(time_series_scaled[i + input_sequence_length])
    
    if len(X) == 0:
        print(f"Insufficient data for {label} to create sequences")
        return

    X = np.array(X)
    y = np.array(y)
    
    # PyTorch tensörlerine dönüştürme
    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.float32)
    
    if len(X_tensor.shape) == 2:
        X_tensor = X_tensor.unsqueeze(-1)
    
    # Modeli tanımlama
    input_size = 1
    hidden_size = 64
    output_size = 1
    model = InformerModel(input_size, hidden_size, output_size)
    
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    # Eğitim döngüsü
    epochs = 100
    losses = []
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        
        output = model(X_tensor)
        loss = loss_fn(output, y_tensor)
        loss.backward()
        optimizer.step()
        
        losses.append(loss.item())
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item()}")

    # Tahminleri al
    model.eval()
    with torch.no_grad():
        predictions = model(X_tensor).numpy()
    
    # Veriyi ters ölçekleme
    predictions_rescaled = scaler.inverse_transform(predictions)
    y_rescaled = scaler.inverse_transform(y_tensor.numpy().reshape(-1, 1))
    
    # Hata metriklerini hesaplama
    mse = np.mean((predictions_rescaled - y_rescaled) ** 2)
    mae = np.mean(np.abs(predictions_rescaled - y_rescaled))
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((y_rescaled - predictions_rescaled) / y_rescaled)) * 100
    r_squared = 1 - (np.sum((y_rescaled - predictions_rescaled) ** 2) / np.sum((y_rescaled - np.mean(y_rescaled)) ** 2))
    
    # Sonuçları yazdırma
    print(f"MSE: {mse}")
    print(f"MAE: {mae}")
    print(f"RMSE: {rmse}")
    print(f"MAPE: {mape}")
    print(f"R-Squared: {r_squared}")
    
    # Tahmin ve gerçek verileri görselleştirme
    plt.figure(figsize=(14, 6))
    plt.plot(time_series, label=f'Original Data ({label})', color='blue')
    plt.plot(range(input_sequence_length, len(time_series)), predictions_rescaled, label=f'Predicted Data ({label})', color='red')
    plt.xlabel('Time Steps')
    plt.ylabel('Time (Seconds)')
    plt.title(f'Time Series Prediction using Informer Transformer - {label}')
    plt.legend()
    plt.text(0.05, 0.95, f"MSE: {mse:.4f}\nMAE: {mae:.4f}\nRMSE: {rmse:.4f}\nMAPE: {mape:.2f}%\nR²: {r_squared:.4f}",
             transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')
    plt.show()
    
    # Epoch vs Loss grafiği
    plt.figure(figsize=(8, 4))
    plt.plot(range(epochs), losses, label='Training Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Epoch vs Loss')
    plt.legend()
    plt.show()

# CSV dosyalarını sırayla işlemek
for csv_file in csv_files:
    count += 1
    labels = []
    time_data = []
    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            for cell in row:
                match = re.search(r"(\d{1,2}:\d{2}\.\d{3}|\d+\.\d+)", cell.strip())
                if match:
                    time_value = match.group(1)
                    time_data.append(time_value)
                if re.match(r'^[A-Za-z]+$', cell.strip()):
                    labels.append(cell.strip())
    
    label = labels[0] if labels else 'Unknown'
    informerPrediction(time_data, csv_file)
