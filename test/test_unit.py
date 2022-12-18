import unittest
from mock import patch
from apple_apps_getter import customize_app_data, categorize_app, is_kids_friendly


class TopAppleAppsGetterTestCase(unittest.TestCase):

    @patch("apple_apps_getter.get_top_free_apps")
    @patch("apple_apps_getter.get_app_data")
    def test_customize_app_data(self, mock_get_app_data, mock_get_top_free_apps):
        mock_get_top_free_apps.return_value = [{'id': {'attributes': {'im:id': '1643890882'}}}]
        mock_get_app_data.return_value = {
                    "kind": "software",
                    "contentAdvisoryRating": "4+",
                    "primaryGenreName": "Graphics & Design",
                    "trackName": "Dawn - AI Avatars",
                    "averageUserRating": 4.62319000000000013272938303998671472072601318359375
        }

        expected_value = {
            'Dawn - AI Avatars':
                {
                    'id': '1643890882',
                    'category': 'Other(Graphics & Design)',
                    'kids_friendly': True,
                    'rating': 4.62319
                }
        }

        self.assertEqual(customize_app_data('us', 1), expected_value)

    def test_categorize_app(self):
        categories = [{"primaryGenreName": "TV"}, {"primaryGenreName": "Graphics & Design"},
                      {"primaryGenreName": "Music"}, {"primaryGenreName": "News"}, {"primaryGenreName": "Games"}]

        expected_tags = ["TV app", "Other(Graphics & Design)", "Music app", "Other(News)", "Game"]

        for i in range(len(categories)):
            self.assertEqual(categorize_app(categories[i]), expected_tags[i])

    def test_is_is_kids_friendly(self):
        kids_content = [{"contentAdvisoryRating": "4+"}, {"contentAdvisoryRating": "18+"},
                       {"contentAdvisoryRating": "6+"}, {"contentAdvisoryRating": "4+"}]

        expected_tags = [True, False, False, True]

        for i in range(len(kids_content)):
            self.assertEqual(is_kids_friendly(kids_content[i]), expected_tags[i])
