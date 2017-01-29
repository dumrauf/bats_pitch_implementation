from django.conf import settings
from django.test import TestCase, Client

__author__ = 'Dominic Dumrauf'


class ViewsTest(TestCase):

    def test_upload_get(self):
        c = Client()
        response = c.get('/')
        self.assertTemplateUsed(response, template_name='upload.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_upload_without_file(self):
        c = Client()
        response = c.post('/')
        self.assertTemplateUsed(response, template_name='upload.html')
        self.assertFormError(response, 'form', 'file', 'This field is required.')
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_upload_with_non_gzip_file(self):
        c = Client()
        with open('bats_pitch_web/tests/non_gzip_file') as fp:
            response = c.post('/', {'file': fp})
        self.assertTemplateUsed(response, template_name='gzip_error.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('file', response.context)

    def test_upload_with_gzip_file(self):
        c = Client()
        with open('bats_pitch_web/tests/bats_pitch_examples.tar.gz') as fp:
            response = c.post('/', {'file': fp})
        self.assertTemplateUsed(response, template_name='upload_results.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn('file', response.context)
        self.assertEqual(response.context['IS_INCLUDING_ANALYSIS_IN_RETURNED_HTML'],
                         settings.IS_INCLUDING_ANALYSIS_IN_RETURNED_HTML)
        self.assertIn('detected_messages', response.context)
        for line in response.context['analysis']:
            self.assertIn('line_nr', line)
            self.assertIn('raw_line', line)
            self.assertIn('clean_line', line)
            self.assertIn('detected_messages_type', line)
