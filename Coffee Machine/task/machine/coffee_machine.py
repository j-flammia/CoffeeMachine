print("Write how many ml of water the coffee machine has:")
water = int(input())

print("Write how many ml of milk the coffee machine has:")
milk = int(input())

print("Write how many grams of coffee beans the coffee machine has:")
coffee = int(input())

print("Write how many cups of coffee you will need:")
cups = int(input())

water = water - (cups * 200)
milk = milk - (cups * 50)
coffee = coffee - (cups * 15)

if water > 0:
    if milk > 0:
        if coffee > 0:

print("For" + str(cups) + "cups of coffee you will need:\n"
      + str(cups * 200) + "ml of water\n"
      + str(cups * 50) + "ml of milk\n"
      + str(cups * 15) + "g of coffee beans")
