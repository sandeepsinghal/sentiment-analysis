from stock_sentiment import StockSentiment
import unittest
class TestStockSentiment(unittest.TestCase):

    def setUp(self):
        self.stock_sentiment = StockSentiment()

    def test_get_sentiment_positive(self):
        headline = "The company's stock price surged after the positive earnings report."
        result = self.stock_sentiment.get_sentiment(headline)
        print(result)

    def tests(self):
        test_cases = [
            "Tesla shares surged after the company reported record quarterly earnings.",
            "Amazon stock fell as the company missed revenue expectations for the third quarter.",
            "Microsoft announced a new line of Surface products, boosting investor confidence.",
            "Google's parent company Alphabet saw its shares rise after a strong earnings report.",
            "Facebook faced a significant drop in stock price following a data privacy scandal.",
            "Netflix shares soared after the streaming giant added more subscribers than expected.",
            "Apple's stock price increased as the company unveiled its latest iPhone model.",
            "Nvidia's shares dropped after the company issued a weaker-than-expected revenue forecast.",
            "Intel's stock rose on news of a major partnership with a leading tech firm.",
            "IBM's shares fell after the company reported lower-than-expected quarterly profits.",
            "Adobe's stock price climbed following the announcement of a new suite of creative tools.",
            "Salesforce shares increased as the company posted strong quarterly results.",
            "Oracle's stock fell after the company reported a decline in cloud revenue.",
            "PayPal shares surged on news of a new partnership with a major retailer.",
            "Twitter's stock dropped after the company reported a decline in user growth.",
            "Uber shares rose as the company announced plans to expand its delivery services.",
            "Lyft's stock fell after the company reported a larger-than-expected quarterly loss.",
            "Spotify shares increased following the announcement of a new exclusive podcast deal.",
            "Snap's stock price surged after the company reported strong user growth.",
            "Pinterest shares fell as the company missed revenue expectations.",
            "Zoom's stock rose on news of a major new enterprise customer.",
            "Slack shares dropped after the company reported a decline in user engagement.",
            "Shopify's stock price increased as the company posted strong sales growth.",
            "Square shares surged on news of a new cryptocurrency initiative.",
            "Roku's stock fell after the company reported a decline in streaming hours.",
            "Etsy shares rose as the company announced a new marketing campaign.",
            "Peloton's stock dropped after the company issued a product recall.",
            "DocuSign shares increased following the announcement of a new partnership.",
            "Dropbox's stock fell after the company reported lower-than-expected earnings.",
            "Zillow shares surged on news of a new real estate acquisition."
        ]

        # Test the get_sentiment method with the test cases
        for news in test_cases:
            sentiment = self.stock_sentiment.get_sentiment(news)
            print(f"News: {news}\nSentiment: {sentiment}\n")


if __name__ == '__main__':
    unittest.main()
