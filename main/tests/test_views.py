from django.test import TestCase

# Create your tests here.
class TestPage(TestCase):
    def test_home_page(self):
        """
        Test the company name exist in the main html document
        Test if the status code is OK
        Test if the home.html template was used
        """
        response = self.client.get("/")
        # print(response.status_code)
        self.assertContains(response, "BookTime")
        self.assertTemplateUsed(response, "main/home.html")
        self.assertEqual(response.status_code, 200)

    def test_about_us_page(self):
        """
        Test the presence of the name BOOKTIME
        Test the statuscode == 200
        Test the template about.html was used
        Test if the template contains the word ABOUT
        """
        response = self.client.get("/about/")
        self.assertContains(response, "BookTime")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/about.html")
        self.assertContains(response, "ABOUT")
