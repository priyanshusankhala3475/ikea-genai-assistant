import pandas as pd
import random
import os

# Random results same rahenge
random.seed(42)

# ==========================================
# 1. PRODUCT DATA
# ==========================================

product_names = [
    "KALLAX", "BILLY", "MALM", "HEMNES",
    "LACK", "BESTA", "PAX", "EKET",
    "MICKE", "POANG", "ALEX", "BRIMNES",
    "TROFAST", "IVAR"
]

categories = [
    "Sofa",
    "Chair",
    "Table",
    "Desk",
    "Bed",
    "Wardrobe",
    "Bookshelf",
    "Storage",
    "Cabinet",
    "TV Unit",
    "Dining Furniture"
]

designers = [
    "IKEA Design Team",
    "Jon Karlsson",
    "Henrik Preutz",
    "Monika Mulder",
    "Ola Wihlborg"
]

colors = [
    "White",
    "Black",
    "Brown",
    "Oak",
    "Grey",
    "Beige",
    "Blue",
    "Green"
]

descriptions = [
    "Modern Scandinavian furniture with a simple and functional design.",
    "Compact furniture suitable for small apartments.",
    "Durable furniture with practical storage space.",
    "Minimalist design suitable for modern homes.",
    "Affordable and stylish furniture for everyday use.",
    "Space-saving furniture with easy assembly.",
    "Simple design with clean Scandinavian lines."
]

# ==========================================
# 2. GENERATE 1200 PRODUCTS
# ==========================================

products = []

for i in range(1, 1201):

    product = {
        "item_id": f"IKEA{i:05d}",
        "name": random.choice(product_names),
        "category": random.choice(categories),
        "price": random.randint(499, 50000),
        "short_description": random.choice(descriptions),
        "designer": random.choice(designers),
        "depth": random.randint(20, 100),
        "height": random.randint(30, 220),
        "width": random.randint(30, 200),
        "other_colors": ", ".join(random.sample(colors, 3)),
        "sellable_online": random.choice([True, True, True, False]),
        "rating": round(random.uniform(3.0, 5.0), 1),
        "reviews_count": random.randint(5, 500)
    }

    products.append(product)

# DataFrame
products_df = pd.DataFrame(products)

# ==========================================
# 3. GENERATE REVIEWS
# ==========================================

positive_reviews = [
    "Very good quality and easy to assemble.",
    "Excellent product for the price.",
    "Looks great in my room.",
    "Very useful and practical furniture.",
    "Beautiful Scandinavian design.",
    "Good quality and durable.",
    "Perfect for a small apartment."
]

neutral_reviews = [
    "Overall good product.",
    "Decent quality for the price.",
    "Assembly takes some time.",
    "The product is good.",
    "Size was as expected."
]

negative_reviews = [
    "Assembly instructions could be better.",
    "Quality was average.",
    "Some parts were difficult to assemble.",
    "Not completely satisfied.",
    "Product was smaller than expected."
]

reviews = []

for i in range(1, 1501):

    product = random.choice(products)

    rating = random.choices(
        [1, 2, 3, 4, 5],
        weights=[2, 3, 10, 30, 55]
    )[0]

    if rating >= 4:
        review_text = random.choice(positive_reviews)

    elif rating == 3:
        review_text = random.choice(neutral_reviews)

    else:
        review_text = random.choice(negative_reviews)

    review = {
        "review_id": f"REV{i:05d}",
        "item_id": product["item_id"],
        "product_name": product["name"],
        "rating": rating,
        "review": review_text
    }

    reviews.append(review)

reviews_df = pd.DataFrame(reviews)

# ==========================================
# 4. CREATE DATA FOLDER
# ==========================================

os.makedirs("data", exist_ok=True)

# ==========================================
# 5. SAVE PRODUCT DATA
# ==========================================

products_df.to_csv(
    "data/ikea.csv",
    index=False
)

# ==========================================
# 6. CREATE CLEANED DATASET
# ==========================================

cleaned_df = products_df.drop_duplicates(
    subset=["item_id"]
)

cleaned_df = cleaned_df.dropna(
    subset=["name", "category", "price"]
)

cleaned_df.to_csv(
    "data/cleaned_ikea.csv",
    index=False
)

# ==========================================
# 7. SAVE REVIEWS
# ==========================================

reviews_df.to_csv(
    "data/reviews.csv",
    index=False
)

# ==========================================
# 8. SUCCESS MESSAGE
# ==========================================

print()
print("=" * 50)
print(" IKEA DATASET GENERATED SUCCESSFULLY")
print("=" * 50)

print(f"Products generated : {len(products_df)}")
print(f"Reviews generated  : {len(reviews_df)}")

print()
print("Files created:")
print("1. data/ikea.csv")
print("2. data/cleaned_ikea.csv")
print("3. data/reviews.csv")

print()
print("DONE!")