from sql_connection import get_sql_connection
from datetime import datetime

def get_order_details(cnx, order_id):
	cur = cnx.cursor()

	query = ("""select o.order_id, p.product_id, p.name, o.quantity, o.total_price from order_details o inner join 
			   products p on o.product_id=p.product_id where o.order_id="""+str(order_id))

	cur.execute(query)

	response = []

	for (order_id, product_id, name, quantity, total_price) in cur:
		response.append(
			{
				"order_id": order_id,
				"product_id": product_id,
				"name": name,
				"quantity": quantity,
				"total_price": total_price
			}
		)

	return response

def get_orders(cnx):
	cur = cnx.cursor()

	query = """select * from orders"""

	cur.execute(query)

	response = []

	for (order_id, customer_name, date, total_cost) in cur:
		response.append(
			{
				"order_id": order_id,
				"customer_name": customer_name,
				"date": date,
				"total_cost": total_cost
			}
		)

	return response

def insert_new_order(cnx, order):
	cur = cnx.cursor()

	query = "insert into order_details (order_id, product_id, quantity, total_price) values (%s, %s, %s, %s)"

	data = (order.get('order_id'), order.get('product_id'), order.get('quantity'), order.get('total_price'))

	cur.execute(query, data)

	cnx.commit()

	current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	query = "replace into orders (order_id, customer_name, date, total_cost) values (%s, %s, %s, %s)"

	data = (order.get('order_id'), order.get('customer_name'), current_date, order.get('total_cost'))

	cur.execute(query, data)

	cnx.commit()

	return cur.lastrowid

def delete_order(cnx, values):
	order_id, product_id, quantity, total_price = values
	cur = cnx.cursor()
	query = ("delete from order_details where order_id=%s and product_id=%s and quantity=%s and total_price=%s")

	cur.execute(query, values)
	cnx.commit()

	current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	query = "update orders set total_cost = total_cost - %s, date = %s where order_id = %s"
	cur.execute(query, (total_price, current_date, order_id))
	cnx.commit()

	query = "delete from orders where order_id = %s and total_cost <= 0"
	cur.execute(query, (order_id,))
	cnx.commit()

if __name__ == "__main__":
	cnx = get_sql_connection()
	# print(get_order_details(cnx, 6)) 
	# print(get_orders(cnx)) 
	# print(insert_new_order(cnx, {'order_id': 1, 'product_id': 2, 'quantity': 3, 'total_price': 300})) 