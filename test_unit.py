from unittest import IsolatedAsyncioTestCase
import asyncio
from hackernews import hnews

class TestHnews(IsolatedAsyncioTestCase):

    async def test_async(self):
        list_title_json = await hnews(20)
        self.assertEqual(len(list_title_json), 20)

if __name__ == "__main__":
    unittest.main()
