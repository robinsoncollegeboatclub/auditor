from django.test import TestCase
from .models import Fault
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """This class defines the test suite for the fault model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")  # ADD THIS LINE

        self.fault_description = "Write world class code"
        self.fault_assignee = "rower@robinsonboatclub.co.uk"
        self.fault_item_name = "Some item name"
        self.fault_item_description = "This is the item that we use in our tests"
        self.fault_status = "Open"

        self.fault = Fault(description=self.fault_description,
                           assignee=self.fault_assignee,
                           item_name=self.fault_item_name,
                           item_description=self.fault_item_description,
                           status=self.fault_status,
                           owner=user)

    def test_model_can_create_a_fault(self):
        """Test the fault model can create a fault."""
        old_count = Fault.objects.count()
        self.fault.save()
        new_count = Fault.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.fault_data = {
            'description': 'Write world class code',
            'assignee': 'rower@robinsonboatclub.co.uk',
            'item_name': 'Some item name',
            'item_description': 'This is the item that we use in our tests',
            'status': 'Open',
            'owner': user.id,
        }

        self.response = self.client.post(
            reverse('create'),
            self.fault_data,
            format='json')

    def test_api_can_create_a_fault(self):
        """Test the api has fault creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/faults/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_fault(self):
        """Test the api can get a given fault."""
        fault = Fault.objects.get()

        response = self.client.get(
            reverse('details',
                    kwargs={'pk': fault.id}), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, fault)

    def test_api_can_update_fault(self):
        """Test the api can update a given fault."""
        fault = Fault.objects.get()
        change_fault = {'description': 'Something new'}

        res = self.client.patch(
            reverse('details', kwargs={'pk': fault.id}),
            change_fault, format='json'
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a fault."""
        fault = Fault.objects.get()

        response = self.client.delete(
            reverse('details', kwargs={'pk': fault.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)