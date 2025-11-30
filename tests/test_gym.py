import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from gym_system import GymSystem

class TestGymSystem(unittest.TestCase):
    def setUp(self):
        self.gym = GymSystem()

    def test_base_cost(self):
        self.assertEqual(self.gym.calculate_base_cost("Basic"), 50)
        self.assertEqual(self.gym.calculate_base_cost("Premium"), 100)
        self.assertEqual(self.gym.calculate_base_cost("Family"), 150)

    def test_features_cost(self):
        features = ["Personal Training", "Group Classes"]
        self.assertEqual(self.gym.calculate_features_cost(features), 50)

    def test_premium_surcharge(self):
        # Basic (50) + Spa (40) = 90. Premium Surcharge 15% -> 103.5 -> 103
        self.assertEqual(self.gym.calculate_total("Basic", ["Spa Access"]), 103)

    def test_group_discount(self):
        # Basic (50) * 2 = 100. Group Discount 10% -> 90
        self.assertEqual(self.gym.calculate_total("Basic", [], 2), 90)

    def test_special_offer_200(self):
        # Family (150) + Specialized (50) + Spa (40) = 240.
        # Premium surcharge (15%): 240 * 1.15 = 276.
        # Total > 200, discount $20 -> 256
        self.assertEqual(self.gym.calculate_total("Family", ["Specialized Program", "Spa Access"]), 256)
    
    def test_special_offer_400(self):
         # Premium (100) + Specialized (50) + Spa (40) = 190.
         # 3 members = 570.
         # Premium surcharge (15%): 570 * 1.15 = 655.5
         # Group discount (10%): 655.5 * 0.9 = 589.95
         # Total > 400, discount $50 -> 539.95 -> 539
         self.assertEqual(self.gym.calculate_total("Premium", ["Specialized Program", "Spa Access"], 3), 539)

    def test_invalid_inputs(self):
        self.assertEqual(self.gym.calculate_total("InvalidPlan", []), -1)
        self.assertEqual(self.gym.calculate_total("Basic", ["InvalidFeature"]), -1)

if __name__ == '__main__':
    unittest.main()
