def get_value_from_category(category_data, key):
    # Iterates over the nested objects to find the value for the given key
    for items in category_data:
        for obj in items:
            if key in obj:
                return float(obj[key]["mentionText"])
    return 0.0  # Default value if the key is not found

def map_expenditure(extracted_data):
    return {
        "Expenditure": {
            "SFS": {
                "FixedCosts": {
                    "HomeContents": {
                        "Rent": get_value_from_category(extracted_data.get("expense-category-home-contents", []), "rent"),
                        "CouncilTaxRates": get_value_from_category(extracted_data.get("expense-category-home-contents", []), "council-tax"),
                        "TVLicence": get_value_from_category(extracted_data.get("expense-category-home-contents", []), "tv-license")
                    },
                    "Utilities": {
                        "Gas": get_value_from_category(extracted_data.get("expense-category-utilities", []), "gas"),
                        "Electricity": get_value_from_category(extracted_data.get("expense-category-utilities", []), "electricity")
                    },
                    "Water": {
                        "WaterSupply": get_value_from_category(extracted_data.get("expense-category-water-supply", []), "water")
                    },
                    "CareHealth": {
                        "PrescriptionsMedicines": get_value_from_category(extracted_data.get("expense-category-care-health", []), "prescriptions-and-medicines"),
                        "DentistryOpticians": get_value_from_category(extracted_data.get("expense-category-care-health", []), "dentistry-and-opticians")
                    },
                    "TransportTravel": {
                        "CarInsurance": get_value_from_category(extracted_data.get("expense-category-transport-travel", []), "car-insurance"),
                        "RoadTax": get_value_from_category(extracted_data.get("expense-category-transport-travel", []), "car-tax"),
                        "FuelParkingTollRoadCharges": get_value_from_category(extracted_data.get("expense-category-transport-travel", []), "fuel"),
                        "VehicleFinance": get_value_from_category(extracted_data.get("expense-category-transport-travel", []), "vehicle-finance"),
                        "CarMaintenance": get_value_from_category(extracted_data.get("expense-category-transport-travel", []), "car-maintenance")
                    },
                    "PensionsInsurances": {
                        "LifeInsurance": get_value_from_category(extracted_data.get("expense-category-pension-insurances", []), "life-insurance")
                    }
                },
                "FlexibleCosts": {
                    "FoodHousekeeping": {
                        "Groceries": get_value_from_category(extracted_data.get("expense-category-food-housekeeping", []), "groceries"),
                        "HouseRepairsMaintenance": get_value_from_category(extracted_data.get("expense-category-food-housekeeping", []), "house-repairs-and-maintenance"),
                        "SchoolWorkMeals": get_value_from_category(extracted_data.get("expense-category-food-housekeeping", []), "school-and-work-meals"),
                        "LaundryDryCleaning": get_value_from_category(extracted_data.get("expense-category-food-housekeeping", []), "laundry-and-dry-cleaning")
                    },
                    "CommunicationsLeisure": {
                        "HomePhoneInternetTV": get_value_from_category(extracted_data.get("expense-category-communications-leisure", []), "home-phone-internet-tv-package"),
                        "MobilePhone": get_value_from_category(extracted_data.get("expense-category-communications-leisure", []), "mobile-phones"),
                        "Gift": get_value_from_category(extracted_data.get("expense-category-communications-leisure", []), "gift"),
                        "HobbiesLeisureSports": get_value_from_category(extracted_data.get("expense-category-communications-leisure", []), "hobbies-leisures-sports")
                    },
                    "Personal": {
                        "ClothingFootwear": get_value_from_category(extracted_data.get("expense-category-personal", []), "clothing-and-footwear"),
                        "Hairdressing": get_value_from_category(extracted_data.get("expense-category-personal", []), "hair-dressing"),
                        "Toiletries": get_value_from_category(extracted_data.get("expense-category-personal", []), "toiletries")
                    }
                }
            }
        }
    }

# Example usage:
extracted_data = {
    # Your JSON structure here
}

# Get the mapped data
mapped_data = map_expenditure(extracted_data)
print(mapped_data)
