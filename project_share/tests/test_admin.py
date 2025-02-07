from django.contrib.auth import get_user_model
# from rest_framework.test import APITestCase, APITransactionTestCase
from django.test import LiveServerTestCase
from rest_framework.test import APIClient

User = get_user_model()


class ProjectTests(LiveServerTestCase):
    fixtures = ['default.json']

    """@staticmethod
    def setUpClass():
        settings.DEBUG = True

    def tearDown(self):
        sys.stdout.write("Tear down\n")
        sys.stdout.flush()
        from django.db import connection
        pp = pprint.PrettyPrinter(indent=4)
        sys.stdout.write("SQL: ")
        pp.pprint(connection.queries)
        sys.stdout.flush()"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='adminTest',
                                                  email='adminTest@test.test',
                                                  password='adminTest')
        self.assertTrue(self.client.login(username='adminTest', password='adminTest'))

    def test_project_views(self):
        """Go to update, unpublish, etc."""
        url = '/admin/project_share/application/'
        response = self.client.get(url, **{'HTTP_REFERER': url})
        self.assertTrue(response.status_code == 300 or response.status_code == 200,
                        msg="Got code %s on %s" % (response.status_code, url))
        url = '/admin/project_share/project/'
        response = self.client.get(url, **{'HTTP_REFERER': url})
        self.assertTrue(response.status_code == 300 or response.status_code == 200,
                        msg="Got code %s on %s" % (response.status_code, url))
