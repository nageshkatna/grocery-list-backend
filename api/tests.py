from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import GroceryItem
import uuid

class GroceryItemModelTests(TestCase):
    def test_create_grocery_item(self):
        """Test creating a grocery item"""
        item = GroceryItem.objects.create(
            name="Test Item",
            quantity="2",
            unit="pieces",
            description="Test description"
        )
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.quantity, "2")
        self.assertEqual(item.unit, "pieces")
        self.assertEqual(item.description, "Test description")
        self.assertFalse(item.purchased)
        self.assertIsInstance(item.id, uuid.UUID)

    def test_grocery_item_str(self):
        """Test the grocery item string representation"""
        item = GroceryItem.objects.create(name="Test Item")
        self.assertEqual(str(item.name), "Test Item")

class GroceryItemAPITests(APITestCase):
    def setUp(self):
        """Setup data for tests"""
        self.grocery_item = GroceryItem.objects.create(
            name="Test Item",
            quantity="2 pcs",
            description="Test description"
        )
        self.url = reverse('groceryitem-list')

    def test_create_grocery_item(self):
        """Test creating a grocery item through API"""
        data = {
            "name": "New Test Item",
            "quantity": "3 pcs",
            "description": "New test description",
            "purchased": False
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GroceryItem.objects.count(), 2)
        self.assertEqual(GroceryItem.objects.filter(name="New Test Item").exists(), True)

    def test_get_grocery_items(self):
        """Test retrieving grocery items"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_grocery_item_detail(self):
        """Test retrieving a specific grocery item"""
        url = reverse('groceryitem-detail', args=[str(self.grocery_item.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.grocery_item.name)

    def test_update_grocery_item(self):
        """Test updating a grocery item"""
        url = reverse('groceryitem-detail', args=[str(self.grocery_item.id)])
        data = {
            "name": "Updated Test Item",
            "quantity": "4 pcs",
            "description": "Updated description",
            "purchased": True
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.grocery_item.refresh_from_db()
        self.assertEqual(self.grocery_item.name, "Updated Test Item")
        self.assertEqual(self.grocery_item.purchased, True)

    def test_delete_grocery_item(self):
        """Test deleting a grocery item"""
        url = reverse('groceryitem-detail', args=[str(self.grocery_item.id)])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(GroceryItem.objects.count(), 0)

    def test_invalid_grocery_item_creation(self):
        """Test creating a grocery item with invalid data"""
        data = {
            "name": "",  
            "quantity": "3 pcs"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_grocery_item_creation(self):
        """Test creating a grocery item with a duplicate name"""
        data = {
            "name": "Test Item",  
            "quantity": "3 pcs",
            "description": "This should fail"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("already exists", response.data["error"])
        
        data["name"] = "TEST ITEM"  
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("already exists", response.data["error"])
        
        self.assertEqual(GroceryItem.objects.count(), 1)

    def test_grocery_item_list_ordering(self):
        """Test that grocery items are returned in correct order"""
        purchased_item = GroceryItem.objects.create(
            name="Purchased Item",
            purchased=True
        )
        unpurchased_item1 = GroceryItem.objects.create(
            name="Unpurchased Item 1"
        )
        unpurchased_item2 = GroceryItem.objects.create(
            name="Unpurchased Item 2"
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        
        purchased_position = next(
            i for i, item in enumerate(results)
            if item['id'] == str(purchased_item.id)
        )
        unpurchased1_position = next(
            i for i, item in enumerate(results)
            if item['id'] == str(unpurchased_item1.id)
        )
        unpurchased2_position = next(
            i for i, item in enumerate(results)
            if item['id'] == str(unpurchased_item2.id)
        )
        
        self.assertLess(unpurchased1_position, purchased_position)
        self.assertLess(unpurchased2_position, purchased_position)
