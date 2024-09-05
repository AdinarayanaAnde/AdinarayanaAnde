"""
Problem statement:
Given multiple vegetable shops and prices of the vegetables along with available quantities,
what is the minimum amount required to buy the vegetables
Special scenarios to be considered are as below
1. If amount is not sufficient to buy all the vegetables, return "Amount not sufficient"
2. If vegetable is not available in the market, return "One or more vegetables not available"
3. If quantity to be bought is not available in the market, return "No sufficient vegetable quantities"

Examples:
Input:
# Example usage
prices_by_shop = [('s1', 'v1', 10, 1), ('s2', 'v1', 15, 2), ('s3', 'v2', 20, 5)]
vegetables_to_buy = [('v1', 2), ('v2', 3)]
amount_in_hand = 100

Output:
85
--------------------------------------------------------------------------------
Input:
# Example usage
prices_by_shop = [('s1', 'v1', 10, 1), ('s2', 'v1', 15, 2), ('s3', 'v2', 20, 5)]
vegetables_to_buy = [('v1', 2), ('v2', 3)]
amount_in_hand = 10

Output:
Amount not sufficient
--------------------------------------------------------------------------------
Input:
# Example usage
prices_by_shop = [('s1', 'v1', 10, 1), ('s2', 'v1', 15, 2), ('s3', 'v2', 20, 5)]
vegetables_to_buy = [('v1', 2), ('v3', 3)]
amount_in_hand = 10

Output:
One or more vegetables not available
--------------------------------------------------------------------------------
Input:
# Example usage
prices_by_shop = [('s1', 'v1', 10, 1), ('s2', 'v1', 15, 2), ('s3', 'v2', 20, 5)]
vegetables_to_buy = [('v1', 2), ('v2', 300)]
amount_in_hand = 10000

Output:
No sufficient vegetable quantities
"""
def minimum_vegetable_cost(prices_by_shop, vegetables_to_buy, amount_in_hand):
    amount_in_hand_before_purchase = amount_in_hand
    # vegetable_id: [price_per_kg,...]
    vegetable_prices = {}
    # (vegetable_id, price_per_kg): total_quantity_available
    vegetable_quantities = {}

    for (_, vegetable_id, price_per_kg, total_quantity_available) in prices_by_shop:
        vegetable_prices.setdefault(vegetable_id, []).append(price_per_kg)
        vegetable_quantities.setdefault((vegetable_id, price_per_kg), 0)
        vegetable_quantities[(vegetable_id, price_per_kg)] += total_quantity_available

    for vegetable_id, prices_per_kg in vegetable_prices.items():
        prices_in_sorted_order = sorted(set(prices_per_kg))
        vegetable_prices[vegetable_id] = prices_in_sorted_order

    for vegetable_id, quantity_to_purchase_in_kg in vegetables_to_buy:
        if vegetable_id not in vegetable_prices:
            return "One or more vegetables not available"

        for price_per_kg in vegetable_prices[vegetable_id]:
            total_quantity_available = vegetable_quantities[(vegetable_id, price_per_kg)]

            if total_quantity_available >= quantity_to_purchase_in_kg:
                amount_to_be_paid = quantity_to_purchase_in_kg * price_per_kg
                amount_in_hand -= amount_to_be_paid
                if amount_in_hand < 0:
                    return "Amount not sufficient"
                quantity_to_purchase_in_kg = 0
            else:
                amount_to_be_paid = total_quantity_available * price_per_kg
                amount_in_hand -= amount_to_be_paid
                if amount_in_hand < 0:
                    return "Amount not sufficient"
                quantity_to_purchase_in_kg -= total_quantity_available

            if quantity_to_purchase_in_kg == 0:
                break

        if quantity_to_purchase_in_kg > 0:
            return "No sufficient vegetable quantities"

    best_price = amount_in_hand_before_purchase - amount_in_hand
    return best_price
