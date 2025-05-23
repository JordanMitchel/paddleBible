from prometheus_client import Counter

# Prometheus counters (these should only go up)
from prometheus_client import Counter

# Define labeled counters
info_counter = Counter("log_info_total", "Total INFO logs", ["service"])
warn_counter = Counter("log_warn_total", "Total WARNING logs", ["service"])
error_counter = Counter("log_error_total", "Total ERROR logs", ["service"])

