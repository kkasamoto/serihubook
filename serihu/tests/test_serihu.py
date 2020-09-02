from django.test import TestCase
from django.core.exceptions import ValidationError

from serihu.models import Serihu


class TestSerihu(TestCase):
    def test_save_model_successfully(self):
        instance = Serihu(serihu="aaaaaaaaaaaa", owner="kkkkk", created_by="admin")
        instance.save()
        print(instance)
        actual = Serihu.objects.all()[0]
        self.assertEqual(instance, actual)

    def test_work_valid_to_exceed_length(self):
        instance = Serihu(serihu="a"*501, owner="kkk", created_by="admin")
        with self.assertRaises(ValidationError) as e:
            instance.full_clean()
