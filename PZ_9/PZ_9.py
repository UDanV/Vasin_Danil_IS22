sales = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
sales_list = sales.split()
sales_dict = {}
for i in range(0, len(sales_list), 6):
    fruit = sales_list[i]
    sales = list(map(int, sales_list[i+1:i+6]))
    sales_dict[fruit] = sales
    print(f"Максимальные продажи для товара - {fruit}: {max(sales)}")