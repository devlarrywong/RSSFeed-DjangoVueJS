from django.test import TestCase

from django.urls import reverse  # get the endpoint instead of path

from rss.models import Feed

import json


# class RssIndexViewTests(TestCase):

#     """
#         We know we want our application to do a couple of things:

#             1. Respond successfully
#             2. Accept user input
#             3. Return an RSS feed
#     """

#     def test_no_feed(self):
#         """
#             To describe how our application should behave when there is no RSS feed supplied.
#         """
#         response = self.client.get(reverse("index"))

#         # Whether or not the view responded successfully (HTTP 200)
#         self.assertEqual(response.status_code, 200)
#         # Whether or not the feed object is None
#         self.assertEqual(response.context["feed"], None)

#     def test_user_feed(self):
#         """
#             Testing for user input
#             a test for the real functionality of our application.
#         """

#         response = self.client.get(reverse("index") + "?url=https://www.djangoproject.com/rss/weblog/")

#         self.assertEqual(response.status_code, 200)

#         # to ensure that the feed object is not None.
#         self.assertNotEqual(response.context["feed"], None)


class RssFeedModelTests(TestCase):
    def setUp(self):
        Feed.objects.create(
            url="https://www.djangoproject.com/rss/weblog/"
        )

    def test_model_has_url(self):
        django_feed = Feed.objects.get(
            url="https://www.djangoproject.com/rss/weblog/"
        )

        self.assertEqual(
            django_feed.url,
            "https://www.djangoproject.com/rss/weblog/"
        )


class RssRestFeedsViewTests(TestCase):

    def test_create_feed(self):
        url = "https://www.djangoproject.com/rss/weblog/"
        json_data = json.dumps({"url": url})

        response = self.client.post(
            reverse("rest-feeds"),
            json_data,
            content_type="application/json"
        )

        feeds = Feed.objects.all()

        self.assertEqual(response.status_code, 201)
        self.assertQuerysetEqual(
            feeds,
            ["<Feed '{}'>".format(url)]
        )

    def test_get_feeds(self):
        url = "https://www.djangoproject.com/rss/weblog"

        Feed.objects.create(
            url=url
        )

        response = self.client.get(reverse('rest-feeds'))
        feed = response.json()[0]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(feed["url"], url)

    def test_update_feed(self):
        url = "https://www.djangoproject.com/rss/weblog/"
        new_url = "https://utan.io/?feed=rss2"

        Feed.objects.create(
            url=url
        )

        json_data = json.dumps({
            "url": new_url
        })

        response = self.client.put(
            "/rss/feeds/1/",
            json_data,
            content_type="application/json"
        )

        feeds = Feed.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            feeds,
            ["<Feed '{}'>".format(new_url)]
        )

    def test_delete_feed(self):
        Feed.objects.create(
            url="https://www.djangoproject.com/rss/weblog/"
        )

        response = self.client.delete("/rss/feeds/1/")

        feeds = Feed.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            feeds,
            []
        )


class RssRestItemsViewTests(TestCase):

    def test_get_items(self):
        Feed.objects.create(
            url="https://www.djangoproject.com/rss/weblog/"
        )

        response = self.client.get(reverse("rest-items"))

        self.assertEqual(response.status_code, 200)
