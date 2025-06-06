import os
from dotenv import load_dotenv
import openai

# Load .env variables
load_dotenv()
USE_DUMMY = os.getenv("USE_DUMMY_OUTPUT", "false").lower() == "true"
API_KEY = os.getenv("OPENAI_API_KEY")

# Configure the OpenAI client
openai.api_key = API_KEY

def generate_blog_post(keyword: str, seo_data: dict) -> str:
    if USE_DUMMY or not API_KEY:
        return f"""## {keyword.title()} Blog Post (Dummy)

**Search Volume:** {seo_data.get("search_volume", "N/A")}
**Keyword Difficulty:** {seo_data.get("keyword_difficulty", "N/A")}
**CPC:** ${seo_data.get("avg_cpc", "N/A")}

### Introduction
This is a placeholder post for **{keyword}**, generated during testing.

### Why This Matters
It helps developers test the app without using OpenAI tokens.

### Call to Action
Visit {{AFF_LINK_1}} to learn more.
"""

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": (
                    f"You are a professional blog writer. Write an SEO-optimized blog post "
                    f"about the keyword: '{keyword}'.\n\n"
                    f"Include:\n"
                    f"- Search Volume: {seo_data.get('search_volume')}\n"
                    f"- Keyword Difficulty: {seo_data.get('keyword_difficulty')}\n"
                    f"- CPC: ${seo_data.get('avg_cpc')}\n"
                    f"- Title, intro, 3 subheadings, markdown, and these affiliate placeholders: "
                    f"{{AFF_LINK_1}}, {{AFF_LINK_2}}, {{AFF_LINK_3}}"
                )
            }],
            max_tokens=1000,
            temperature=0.7
        )
        content = response.choices[0].message.content
        return (
            content.replace("{{AFF_LINK_1}}", "https://example.com/affiliate1")
                   .replace("{{AFF_LINK_2}}", "https://example.com/affiliate2")
                   .replace("{{AFF_LINK_3}}", "https://example.com/affiliate3")
        )
    except Exception as e:
        return f"## Error\nOpenAI API call failed: {str(e)}"
