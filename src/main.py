from gym_system import GymSystem

def display_menu(options, title):
    print(f"\n{title}:")
    for i, (name, cost) in enumerate(options.items(), 1):
        print(f"{i}. {name} (${cost})")
    return list(options.keys())

def get_selection(options_list):
    try:
        choice = int(input("Select an option (number): ").strip())
        if 1 <= choice <= len(options_list):
            return options_list[choice - 1]
    except ValueError:
        pass
    return None

def main():
    gym = GymSystem()
    
    print("\n--- Gym Membership System ---")
    
    # 1. Select Plan
    plans_list = display_menu(gym.plans, "Available Plans")
    plan_name = get_selection(plans_list)
    
    if not plan_name:
        print("Error: Invalid plan selection.")
        return

    # 2. Select Features
    all_features = {**gym.features, **gym.premium_features}
    features_list = display_menu(all_features, "Available Features")
    
    print("\nEnter feature numbers separated by comma (e.g., 1,3) or leave empty:")
    features_input = input().strip()
    
    selected_features = []
    if features_input:
        try:
            indices = [int(x.strip()) for x in features_input.split(",")]
            for idx in indices:
                if 1 <= idx <= len(features_list):
                    selected_features.append(features_list[idx - 1])
                else:
                    print(f"Error: Feature number {idx} is invalid.")
                    return
        except ValueError:
            print("Error: Invalid input format.")
            return

    # Number of members
    try:
        num_members = int(input("\nEnter number of members: ").strip())
        if num_members < 1:
            raise ValueError
    except ValueError:
        print("Error: Invalid number of members.")
        return

    # 8. Confirmation
    base_cost = gym.calculate_base_cost(plan_name)
    features_cost = gym.calculate_features_cost(selected_features)
    
    print("\n--- Confirmation ---")
    print(f"Plan: {plan_name} (${base_cost})")
    print(f"Features: {', '.join(selected_features) if selected_features else 'None'} (${features_cost})")
    print(f"Members: {num_members}")
    
    confirm = input("\nConfirm purchase? (1: Yes, 2: No): ").strip()
    if confirm != '1':
        print("Purchase cancelled.")
        return

    # Calculate total
    total = gym.calculate_total(plan_name, selected_features, num_members)
    
    if total == -1:
        print("Error: Calculation failed due to invalid inputs.")
    else:
        print(f"\nTotal Cost: ${total}")

if __name__ == "__main__":
    main()
