from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Machine, Booking, Order, OrderItem


class ModelTests(TestCase):
    def setUp(self):
        """Set up initial database instances for testing."""
        self.machine = Machine.objects.create(
            name="Espresso Master 3000",
            slug="espresso-master-3000",
            description="High-end commercial espresso machine.",
            specs="Dual boiler, PID control",
            price=2500.00
        )
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="securepassword123"
        )

    def test_machine_creation(self):
        """Test Machine model creation and string representation."""
        self.assertEqual(str(self.machine), "Espresso Master 3000")
        self.assertEqual(self.machine.price, 2500.00)

    def test_booking_creation(self):
        """Test Booking model creation."""
        booking = Booking.objects.create(
            user=self.user,
            name="Test Customer",
            email="test@example.com",
            service="routine"
        )
        self.assertEqual(booking.name, "Test Customer")
        self.assertEqual(booking.user, self.user)

    def test_order_creation(self):
        """Test Order model creation and auto-generated order_number."""
        order = Order.objects.create(
            user=self.user,
            full_name="Test Customer",
            email="test@example.com",
            address="123 Coffee St",
            city="London",
            postcode="EC1A 1BB",
            total_price=2500.00
        )
        self.assertTrue(len(order.order_number) > 0)
        self.assertEqual(order.total_price, 2500.00)


class ViewTests(TestCase):
    def setUp(self):
        """Initialize HTTP client and test resources."""
        self.client = Client()
        self.machine = Machine.objects.create(
            name="Commercial Brewer",
            slug="commercial-brewer",
            description="Heavy-duty brewer.",
            price=1200.00
        )
        self.user = User.objects.create_user(
            username="tester",
            password="password123"
        )

    def test_public_pages_status_code(self):
        """Test that key public endpoints return 200 OK status."""
        pages = ['index', 'catalog', 'services', 'booking']
        for page in pages:
            response = self.client.get(reverse(page))
            self.assertEqual(
                response.status_code, 200, f"Failed on page: {page}"
            )

    def test_machine_detail_view(self):
        """Test machine detail page returns 200 for valid slug."""
        url = reverse('machine_detail', kwargs={'slug': self.machine.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Commercial Brewer")

    def test_dashboard_login_required(self):
        """Test unauthenticated users are redirected on dashboard access."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_authenticated(self):
        """Test that logged-in users can access the dashboard."""
        self.client.login(username="tester", password="password123")
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_booking_form_submission(self):
        """Test submitting a new booking request creates a database entry."""
        response = self.client.post(reverse('booking'), {
            'name': 'John Doe',
            'email': 'john@example.com',
            'service': 'routine'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().name, 'John Doe')


class CartLogicTests(TestCase):
    def setUp(self):
        """Set up item for cart testing."""
        self.client = Client()
        self.machine = Machine.objects.create(
            name="Compact Grinder",
            slug="compact-grinder",
            description="Precision bean grinder.",
            price=450.00
        )

    def test_add_to_cart(self):
        """Test adding an item to the session cart."""
        url = reverse('add_to_cart', kwargs={'machine_id': self.machine.id})
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        session = self.client.session
        self.assertIn(str(self.machine.id), session['cart'])
        self.assertEqual(session['cart'][str(self.machine.id)], 1)

    def test_remove_from_cart(self):
        """Test removing an item from the session cart."""
        session = self.client.session
        session['cart'] = {str(self.machine.id): 1}
        session.save()

        url = reverse(
            'remove_from_cart', kwargs={'machine_id': self.machine.id}
        )
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        session = self.client.session
        self.assertNotIn(str(self.machine.id), session.get('cart', {}))


class ExtraViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='test@example.com'
        )
        self.machine = Machine.objects.create(
            name='Test Machine',
            slug='test-machine',
            price=100.00
        )

    def test_checkout_get_view(self):
        """Test GET request to checkout page with session cart."""
        session = self.client.session
        session['cart'] = {str(self.machine.id): 2}
        session.save()

        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)

    def test_checkout_post_empty_cart(self):
        """Test submitting checkout with empty cart redirects to catalog."""
        response = self.client.post(reverse('checkout'), {})
        self.assertRedirects(response, reverse('catalog'))

    def test_checkout_post_successful_order(self):
        """Test successful order placement via POST."""
        session = self.client.session
        session['cart'] = {str(self.machine.id): 1}
        session.save()

        response = self.client.post(reverse('checkout'), {
            'full_name': 'Jane Doe',
            'email': 'jane@example.com',
            'address': '123 Coffee St',
            'city': 'Bean Town',
            'postcode': '12345',
        })

        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.first()
        self.assertEqual(order.full_name, 'Jane Doe')
        redirect_url = reverse(
            'order_success', kwargs={'order_number': order.order_number}
        )
        self.assertRedirects(response, redirect_url)

    def test_order_success_view(self):
        """Test order success template rendering."""
        url = reverse('order_success', kwargs={'order_number': 'TEST1234'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_get_view(self):
        """Test rendering registration form."""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_authenticated_redirect(self):
        """Test authenticated user on register page redirects to dashboard."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('register'))
        self.assertRedirects(response, reverse('dashboard'))