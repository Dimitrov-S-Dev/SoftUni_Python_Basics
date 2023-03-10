name = input()
adult_tickets = int(input())
kids_tickets = int(input())
adult_t_price = float(input())
service_price = float(input())

kids_t_price = adult_t_price * 0.3 + service_price
adult_t_price += service_price
total_ticket_price = (adult_t_price * adult_tickets)+ (kids_t_price * kids_tickets)
profit = total_ticket_price * 0.2

print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")
