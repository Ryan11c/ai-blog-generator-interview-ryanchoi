def generate_blog_post(keyword, seo_data):
    #just a mock version that generates basic blog content
    blog = f"""# SEO Report for "{keyword}"

## 1. Search Volume
{seo_data['search_volume']}

## 2. Keyword Difficulty
{seo_data['keyword_difficulty']}

## 3. Average CPC
${seo_data['avg_cpc']}

Want to improve your rankings? Use keyword clustering, optimize for intent, and analyze your competitors.

[Affiliate](https://example.com/aff_link)
"""
    return blog


#If we use open ai:
"""
Write an SEO-optimized blog post in Markdown format about "{keyword}".
Include:
1. Search Volume: {seo_data['search_volume']}
2. Keyword Difficulty: {seo_data['keyword_difficulty']}
3. Average CPC: ${seo_data['avg_cpc']}

The content should sound professional and include one affiliate link like {{AFF_LINK_n}}.
"""
