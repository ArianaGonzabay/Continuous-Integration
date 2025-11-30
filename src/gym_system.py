class GymSystem:
    def __init__(self):
        self.plans = {
            "Basic": 50,
            "Premium": 100,
            "Family": 150
        }
        self.features = {
            "Personal Training": 30,
            "Group Classes": 20
        }
        self.premium_features = {
            "Spa Access": 40,
            "Specialized Program": 50
        }
        
    def calculate_base_cost(self, plan_name):
        return self.plans.get(plan_name, 0)

    def calculate_features_cost(self, selected_features):
        total = 0
        for feature in selected_features:
            if feature in self.features:
                total += self.features[feature]
            elif feature in self.premium_features:
                total += self.premium_features[feature]
        return total

    def is_premium_feature(self, feature):
        return feature in self.premium_features

    def validate_plan(self, plan_name):
        return plan_name in self.plans

    def validate_features(self, selected_features):
        all_available = self.features.copy()
        all_available.update(self.premium_features)
        for feature in selected_features:
            if feature not in all_available:
                return False
        return True

    def calculate_total(self, plan_name, selected_features, num_members=1):
        if not self.validate_plan(plan_name) or not self.validate_features(selected_features):
            return -1

        base_cost = self.calculate_base_cost(plan_name)
        features_cost = self.calculate_features_cost(selected_features)
        subtotal = (base_cost + features_cost) * num_members

        # 6. Premium Surcharge (15%)
        has_premium = any(self.is_premium_feature(f) for f in selected_features)
        if has_premium:
            subtotal *= 1.15

        # 4. Group Discount (10%)
        if num_members >= 2:
            subtotal *= 0.90

        # 5. Special Offer Discounts
        if subtotal > 400:
            subtotal -= 50
        elif subtotal > 200:
            subtotal -= 20

        return int(subtotal) if subtotal > 0 else 0
