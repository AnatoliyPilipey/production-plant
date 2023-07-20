from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from hall.models import Foreman, Shift, Workman, WorkCommitments

FOREMAN_URL = reverse("hall:foreman-list")
SHIFT_URL = reverse("hall:shift-list")
WORKMAN_URL = reverse("hall:workman-list")
WORKCOMMITMENTS_URL = reverse("hall:work-commitments-list")


class PublicTests(TestCase):

    def test_foreman_login_required(self):
        res = self.client.get(FOREMAN_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_shift_login_required(self):
        res = self.client.get(SHIFT_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_workman_login_required(self):
        res = self.client.get(WORKMAN_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_work_commitments_login_required(self):
        res = self.client.get(WORKCOMMITMENTS_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateManufacturerTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "user123test"
        )
        self.client.force_login(self.user)

    def test_retrieve_work_commitments(self):
        WorkCommitments.objects.create(
            duties="test1",
            price=33
        )
        WorkCommitments.objects.create(
            duties="test2",
            price=22
        )

        response = self.client.get(WORKCOMMITMENTS_URL)
        work_commitments = WorkCommitments.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["work_commitments_list"]),
            list(work_commitments)
        )
        self.assertTemplateUsed(response, "hall/work_commitments_list.html")

    def test_create_foreman(self):
        form_data = {
            "username": "test2",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "salary": 12345
        }
        self.client.post(reverse("hall:foreman-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.salary, form_data["salary"])

    def test_search_field_workman(self):
        commitments = WorkCommitments.objects.create(
            duties="test1",
            price=25
        )
        Workman.objects.create(
            first_name="first_name_test1",
            last_name="last_name_test1",
            rate=1,
            commitment=commitments
        )
        Workman.objects.create(
            first_name="first_name_test2",
            last_name="last_name_test2",
            rate=1,
            commitment=commitments
        )

        response = self.client.get(WORKMAN_URL + "?value_=1")
        self.assertEqual(
            list(response.context["workman_list"]),
            list(Workman.objects.filter(first_name__icontains="1"))
        )
