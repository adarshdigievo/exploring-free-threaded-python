| File                      | GIL Enabled | Free Threaded |
|---------------------------|-------------|---------------|
| 1_single_threaded.py      | ~3.0s       | ~3.9s         |
| 2_io_bound_single_thread  | ~5.6s       | ~4.5          |
| 2_io_bound_multithread    | ~4.3s       | ~4.4          |
| 3_cpu_bound_single_thread | ~3.6        | ~3.8          |
| 3_cpu_bound_multithread   | ~3.54       | ~1.38         |
| flask_app_cpu_bound       | 36 req/20s  | 80 reqs/20s   |
| flask_app_io_bound        | 95 req/20s  | 66 req/20s    |