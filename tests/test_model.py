from django.contrib.auth import get_user_model
from django.test import TestCase

from hall.models import WorkCommitments, Foreman


class ModelsTests(TestCase):
    def test_workman_str(self):
        work_commitments = WorkCommitments.objects.create(
            duties="test",
            price=12
        )
        self.assertEqual(
            str(work_commitments),
            work_commitments.duties
        )

    def test_foreman_str(self):
        foreman = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            first_name="first_test",
            last_name="last_test",
            salary=12,
        )

        self.assertEqual(
            str(foreman),
            f"{foreman.first_name} ({foreman.last_name}, {foreman.hired_date})"
        )
