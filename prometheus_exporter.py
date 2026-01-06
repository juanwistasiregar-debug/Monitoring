from prometheus_client import start_http_server, Counter, Histogram, Gauge
import time
import random

# 1. Metrik Counter (Jumlah request)
REQUEST_COUNT = Counter('predict_requests_total', 'Total prediksi')

# 2. Metrik Histogram (Latensi)
LATENCY_BUCKETS = Histogram('predict_latency_seconds', 'Waktu proses')

# 3. Metrik Gauge (Resource/Memory)
MEM_USAGE = Gauge('predict_memory_usage_bytes', 'Penggunaan memori')

def process_inference():
    with LATENCY_BUCKETS.time():
        REQUEST_COUNT.inc()
        # Simulasi proses
        time.sleep(random.uniform(0.1, 0.5))
        MEM_USAGE.set(random.randint(500, 1000))

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        process_inference()
