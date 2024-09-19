user_input = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if "sunny" == user_input:
    print("Wear a t-shirt and sunglasses.")
elif "rainy" == user_input:
    print("Don't forget your umbrella and a raincoat.")
elif "cold" == user_input:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
