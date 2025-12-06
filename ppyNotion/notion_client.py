import requests

from .constants.api_constants import API_HEADERS, BASE_API_URL, ME_ENDPOINT


class NotionClient:
    def __init__(self, notion_key: str) -> None:
        self.base_url = BASE_API_URL
        self.notion_key = notion_key

        self.headers = self._format_headers(notion_key)

        self._check_valid_headers()

    def _check_valid_headers(self) -> None:
        """
        Check if the provided Notion key is valid.

        Raises:
            ValueError: If the Notion API key is invalid.
        """
        # Check of the provided Notion key is valid by making a request to
        # the "me" endpoint
        _ = self.get_me()

    def _format_headers(self, notion_key: str) -> dict:
        """
        Format the headers for the Notion API requests.

        Args:
            notion_key (str): The Notion API key.
        Returns:
            dict: A dictionary containing the formatted headers.
        """
        return {
            key: value.format(NOTION_KEY=notion_key)
            if "{NOTION_KEY}" in value
            else value
            for key, value in API_HEADERS.items()
        }

    def get_me(self) -> dict:
        """
        Get information about the current user (given the provided Notion API ).

        Returns:
            dict: A dictionary containing user information.
        """
        response = requests.get(ME_ENDPOINT, headers=self.headers)

        # Handle error if exists
        if response.status_code == 401:
            raise ValueError("Invalid Notion API key provided.")
        response.raise_for_status()

        return response.json()


if __name__ == "__main__":
    import os
    from pprint import pprint

    import dotenv

    dotenv.load_dotenv()

    NOTION_KEY = os.getenv("NOTION_KEY")
    print("NOTION_KEY: ", NOTION_KEY)
    print()

    client = NotionClient(notion_key=NOTION_KEY)
    print("HEADERS")
    pprint(client.headers)
    print()

    me_data = client.get_me()
    print("ME DATA")
    pprint(me_data)
    print()
