from django.test import TestCase


class ViewsTests(TestCase):
    def test_name_is_html_escaped(self):
        response = self.client.get('/hello/%3Cscript%3Ealert(1)%3Cscript%3E/20')
        self.assertNotContains(response, '<script>')

    def test_division_by_zero_returns_bad_request(self):
        response = self.client.get('/divisao/10/0')
        self.assertEqual(response.status_code, 400)

    def test_sum(self):
        response = self.client.get('/soma/2/3')
        self.assertContains(response, '= 5')
