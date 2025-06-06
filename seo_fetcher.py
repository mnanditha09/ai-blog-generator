import random

def get_seo_metrics(keyword: str) -> dict:
    """
    Returns mock SEO metrics for a given keyword.
    This function simulates basic keyword research by returning randomized values
    for search volume, keyword difficulty, and average cost-per-click (CPC).
    
    Parameters:
        keyword (str): The keyword to analyze.
    
    Returns:
        dict: A dictionary containing:
            - search_volume (int)
            - keyword_difficulty (int)
            - avg_cpc (float)
    """
    # Simulated values for demonstration purposes
    search_volume = random.randint(1000, 50000)           # Estimated number of monthly searches
    keyword_difficulty = random.randint(10, 90)           # SEO difficulty (scale from 0 to 100)
    avg_cpc = round(random.uniform(0.5, 5.0), 2)          # Estimated CPC in USD

    return {
        "search_volume": search_volume,
        "keyword_difficulty": keyword_difficulty,
        "avg_cpc": avg_cpc
    }
