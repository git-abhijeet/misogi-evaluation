# Q: 4
# Create a reusable module stats_utils.py containing:
# def analyze_numbers(nums: list[int]) -> dict: that returns:
# {"mean": ..., "median": ..., "mode": ..., "variance": ...}
# Raise custom exceptions for invalid input types or empty lists.

# In your main script, import and use this function with a randomly generated list of integers (random module).

# Submit the GitHub repository link to the code file


def analyze_numbers(nums: list[int]) -> dict:
    if not nums:
        raise ValueError("Invalid input")
    mean = mean(nums)
    median = median(nums)
    mode = mode(nums)
    variance = variance(nums)

    return {mean, median, mode, variance}