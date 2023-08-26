from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch


class CharacterResultViewTest(TestCase):

    @patch('search.views.requests.get')
    def test_search_character(self, mock_get):
        api_response = {
            "rows": [
                {
                    "serverId": "cain",
                    "characterId": "c54f3097ef542dca63d604d78f13d626",
                    "characterName": "blindRaiden",
                    "level": 110,
                    "jobId": "40132cbc8b2b5eedfe035e35c322472e",
                    "jobGrowId": "ec6a93f4d14bb36ccc541183291197a7",
                    "jobName": "Slayer (M)",
                    "jobGrowName": "Neo: Asura",
                    "fame": 49408
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = api_response

        url = reverse('search:character_result')
        response = self.client.get(url, {'character_search_query': 'blindRaiden'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/characterResult.html')

        character = response.context['character']['rows'][0]
        self.assertEqual(character['characterName'], "blindRaiden")
        self.assertEqual(character['jobName'], "Slayer (M)")
        self.assertEqual(character['jobGrowName'], "Neo: Asura")
