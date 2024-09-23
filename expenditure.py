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


////secong try

// Define Fixed and Flexible categories
const fixedCategories = [
    "expense-category-home-contents",
    "expense-category-utilities",
    "expense-category-water-supply",
    "expense-category-care-health",
    "expense-category-pension-insurances"
];

const flexibleCategories = [
    "expense-category-food-housekeeping",
    "expense-category-transport-travel",
    "expense-category-communications-leisure",
    "expense-category-personal"
];

// Initialize the resulting structure
const expenditure = {
    "Expenditure": {
        "SFS": {
            "FixedCosts": {},
            "FlexibleCosts": {}
        }
    }
};

// Function to extract mentionText as number
const extractValue = (item) => {
    const key = Object.keys(item)[0];
    return {
        [key]: parseFloat(item[key].mentionText) // Convert mentionText to float
    };
};

// Mapping FixedCosts
fixedCategories.forEach(category => {
    if (data[category]) {
        expenditure.Expenditure.SFS.FixedCosts[category.replace("expense-category-", "").replace(/-/g, " ")] = {};
        data[category][0].forEach(item => {
            Object.assign(expenditure.Expenditure.SFS.FixedCosts[category.replace("expense-category-", "").replace(/-/g, " ")], extractValue(item));
        });
    }
});

// Mapping FlexibleCosts
flexibleCategories.forEach(category => {
    if (data[category]) {
        expenditure.Expenditure.SFS.FlexibleCosts[category.replace("expense-category-", "").replace(/-/g, " ")] = {};
        data[category][0].forEach(item => {
            Object.assign(expenditure.Expenditure.SFS.FlexibleCosts[category.replace("expense-category-", "").replace(/-/g, " ")], extractValue(item));
        });
    }
});

// Resulting structure
console.log(JSON.stringify(expenditure, null, 2));