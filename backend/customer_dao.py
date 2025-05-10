from sql_connection import get_sql_connection

def get_all_customers(cnx):
	cur = cnx.cursor()

	query = """select customer_id, customer_name from customers"""

	cur.execute(query)

	response = {}

	for (customer_id, customer_name) in cur:
		response[customer_name] = customer_id

	return response

def insert_new_customer(cnx, customer_name):
	cur = cnx.cursor()

	query = "insert into customers (customer_name) values (%s)"

	data = (customer_name,)

	cur.execute(query, data)

	cnx.commit()

	return cur.lastrowid

if __name__ == "__main__":
	cnx = get_sql_connection()
	# print(get_all_customers(cnx)) 
	print(insert_new_customer(cnx, "Sagar")) 