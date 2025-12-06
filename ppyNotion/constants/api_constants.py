BASE_API_URL = "https://api.notion.com/v1"
ME_ENDPOINT = BASE_API_URL + "/users/me"

API_HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer {NOTION_KEY}",
    "Notion-Version": "2025-09-03",
}
