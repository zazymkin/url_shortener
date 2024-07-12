from tests import TestCase


class TestUrls(TestCase):
    async def test_generate_short_url(self):
        async with self.client.request(
            "POST",
            "/api/generate_short_url/",
            json={"long_url": "https://example.com"},
        ) as resp:
            self.assertEqual(resp.status, 200)
            result = await resp.json()
            self.assertIn("short_url", result)

    async def test_count(self):
        async with self.client.request("GET", "/api/count/NOT_EXIST") as resp:
            self.assertEqual(resp.status, 404)

        async with self.client.request(
            "POST",
            "/api/generate_short_url/",
            json={"long_url": "https://example.com"},
        ) as resp:
            self.assertEqual(resp.status, 200)
            result = await resp.json()
            self.assertIn("short_url", result)
            short_url = result["short_url"]

        async with self.client.request(
            "GET", f"/api/count/{short_url}"
        ) as resp:
            self.assertEqual(resp.status, 200)
            result = await resp.json()
            self.assertEqual(result["click_count"], 0)

        async with self.client.request("GET", short_url):
            pass

        async with self.client.request(
            "GET", f"/api/count/{short_url}"
        ) as resp:
            self.assertEqual(resp.status, 200)
            result = await resp.json()
            self.assertEqual(result["click_count"], 1)
