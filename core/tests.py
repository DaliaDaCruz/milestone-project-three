from django.test import TestCase
from django.urls import reverse
from .models import Category, Product, ServiceRequest
from .forms import ServiceRequestForm


class ModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Espresso Machines", slug="espresso-machines")
        self.product = Product.objects.create(
            category=self.category,
            title="BFC Monza",
            price=3289.99,
            condition="Refurbished",
            description="Commercial espresso machine."
        )
        self.service_request = ServiceRequest.objects.create(
            customer_name="John Doe",
            machine_model="DeLonghi Dedica",
            issue_description="Low pressure."
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), "Espresso Machines")

    def test_product_str(self):
        self.assertEqual(str(self.product), "BFC Monza")

    def test_service_request_str(self):
        self.assertEqual(str(self.service_request), "John Doe - DeLonghi Dedica")


class ViewTests(TestCase):
    def setUp(self):
        self.service_request = ServiceRequest.objects.create(
            customer_name="Jane Smith",
            machine_model="Gaggia Classic",
            issue_description="Leaking group head."
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('request_list'))
        self.assertEqual(response.status_code, 200)

    def test_request_create_view(self):
        response = self.client.post(reverse('request_create'), {
            'customer_name': 'Alex Taylor',
            'machine_model': 'Rancilio Silvia',
            'issue_description': 'Not heating up.'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect on success
        self.assertEqual(ServiceRequest.objects.count(), 2)

    def test_request_delete_view(self):
        response = self.client.post(reverse('request_delete', args=[self.service_request.pk]))
        self.assertEqual(response.status_code, 302)  # Should redirect after delete
        self.assertEqual(ServiceRequest.objects.count(), 0)


class FormTests(TestCase):
    def test_valid_service_request_form(self):
        form = ServiceRequestForm(data={
            'customer_name': 'Sam Wilson',
            'machine_model': 'Sage Barista Touch',
            'issue_description': 'Grinder jammed.'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_service_request_form(self):
        form = ServiceRequestForm(data={
            'customer_name': '',
            'machine_model': '',
            'issue_description': ''
        })
        self.assertFalse(form.is_valid())