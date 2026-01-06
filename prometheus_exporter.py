from prometheus_client import start_http_server, Counter, Histogram, Gauge
import time
import random

# Metrik 1: Counter untuk jumlah request
REQUEST_COUNT = Counter('model_predictions_total', 'Total jumlah prediksi')

# Metrik 2: Histogram untuk durasi prediksi
PREDICT_LATENCY = Histogram('model_prediction_latency_seconds', 'Waktu proses prediksi')

# Metrik 3: Gauge untuk memori
MEMORY_USAGE = Gauge('model_memory_usage_bytes', 'Penggunaan memori model')

def run_model():
    with PREDICT_LATENCY.time(): # Mengukur latency
        REQUEST_COUNT.inc() # Menambah hitungan
        MEMORY_USAGE.set(random.uniform(100, 500)) # Simulasi penggunaan RAM
        time.sleep(random.uniform(0.1, 0.8))

if __name__ == '__main__':
    start_http_server(8000) # Endpoint untuk Prometheus
    while True:
        run_model()
