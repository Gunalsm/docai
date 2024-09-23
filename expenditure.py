# Map FixedCosts
    for category_key, category_name in fixed_costs_categories.items():
        category_data = extracted_data.get(f"expense-category-{category_key}", [])
        for subcategory_list in category_data:
            for subcategory in subcategory_list:
                for field, details in subcategory.items():
                    if category_name not in expenditure["SFS"]["FixedCosts"]:
                        expenditure["SFS"]["FixedCosts"][category_name] = {}
                    expenditure["SFS"]["FixedCosts"][category_name][field.replace("-", "")] = float(details["mentionText"])

    # Map FlexibleCosts
    for category_key, category_name in flexible_costs_categories.items():
        category_data = extracted_data.get(f"expense-category-{category_key}", [])
        for subcategory_list in category_data:
            for subcategory in subcategory_list:
                for field, details in subcategory.items():
                    if category_name not in expenditure["SFS"]["FlexibleCosts"]:
                        expenditure["SFS"]["FlexibleCosts"][category_name] = {}
                    expenditure["SFS"]["FlexibleCosts"][category_name][field.replace("-", "")] = float(details["mentionText"])
