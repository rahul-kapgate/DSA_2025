# What is an Exponential Backoff Strategy?
# An exponential backoff strategy is a technique used in network requests, APIs, and distributed systems to gradually increase the delay between retries when an operation fails. The delay time doubles after each failed attempt.

# This helps to:

# Reduce server load by preventing repeated requests in quick succession.
# Handle temporary failures by waiting before retrying.
# Improve efficiency by not retrying too quickly.
# Problem Breakdown
# Start with an initial delay of 1 second.
# Double the delay after each retry.
# Stop after 5 retries.
# This means the delays will be: 1️⃣ 1 second
# 2️⃣ 2 seconds
# 3️⃣ 4 seconds
# 4️⃣ 8 seconds
# 5️⃣ 16 seconds

# After 5 retries, the process stops.

# Python Implementation
# Here's a Python function implementing the exponential backoff strategy:


import time

def exponential_backoff():
    max_retries = 5  # Stop after 5 retries
    delay = 1  # Start with 1 second

    for attempt in range(1, max_retries + 1):
        print(f"Attempt {attempt}: Waiting for {delay} seconds...")
        time.sleep(delay)  # Simulating the wait time
        delay *= 2  # Double the wait time

    print("Max retries reached. Stopping.")

# Run the function
exponential_backoff()