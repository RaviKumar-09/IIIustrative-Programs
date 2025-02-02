import time


# Start time
start_time = time.time()

# Sample task (e.g., loop running for 1000000 iterations)
for _ in range(1000000):
    pass


# End time
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time\
print(f"Execution Time: {execution_time:.5f} seconds")