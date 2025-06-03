#did not use open ai because it costs money. Instead, here is a temporary blog post
def generate_blog_post(keyword, seo_data):
    return f"""
# SEO Report for "{keyword}"

1. Search Volume: {seo_data['search_volume']}
2. Keyword Difficulty: {seo_data['keyword_difficulty']}
3. Competition Score: {seo_data['competition']}
4. Click-Through Rate: {seo_data['click_rate'] * 100:.0f}%
5.Top Country: {seo_data['top_country']}
6. Related Terms: {", ".join(seo_data['related_terms'])}

Want to rank higher? Use keyword clusters, target terms, and focus on search intent.

Check out our recommended tools here: [{{AFF_LINK_n}}](https://temp/aff1)
"""
