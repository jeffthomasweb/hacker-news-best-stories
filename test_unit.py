from unittest import IsolatedAsyncioTestCase
import asyncio
from hacker_news_best_stories_list.py import hnews

class TestHnews(IsolatedAsyncioTestCase):

    #Test that the async function hnews() returns a list of 20 items if we request 20 stories.
    async def test_async(self):
        list_title_json = await hnews(20)
        self.assertEqual(len(list_title_json), 20)

if __name__ == "__main__":
    unittest.main()
