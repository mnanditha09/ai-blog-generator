import os

def save_post(content: str, filename: str, directory: str = "generated_posts") -> None:
    """
    Saves the blog post content into a Markdown file.
    
    If the folder doesn't exist yet, it'll create it.
    Everything goes into a 'generated_posts' directory by default.

    Parameters:
        content (str): The actual blog post text (in Markdown format).
        filename (str): What to name the file (e.g., '2025-06-03_wireless_earbuds.md').
        directory (str): Folder where files are stored. Defaults to 'generated_posts'.

    Returns:
        None
    """
    # Make sure the folder exists (create it if it doesn’t)
    os.makedirs(directory, exist_ok=True)

    # Build the full path to where we’ll save the file
    file_path = os.path.join(directory, filename)

    # Write the content to the Markdown file using UTF-8 encoding
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Saved blog post to: {file_path}")
