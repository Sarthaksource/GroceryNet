from sql_connection import get_sql_connection

def get_all_products(cnx):
	cur = cnx.cursor()

	query = """select p.product_id, p.name, p.uom_id, p.price_per_unit, u.uom_name from products p inner join 
			   uom u on p.uom_id=u.uom_id"""

	cur.execute(query)

	response = []

	for (product_id, name, uom_id, price_per_unit, uom_name) in cur:
		response.append(
			{
				"product_id": product_id,
				"name": name,
				"uom_id": uom_id,
				"price_per_unit": price_per_unit,
				"uom_name": uom_name
			}
		)

	return response

def insert_new_product(cnx, product):
	cur = cnx.cursor()

	query = "insert into products (name, uom_id, price_per_unit) values (%s, %s, %s)"

	data = (product.get('product_name'), product.get('uom_id'), product.get('price_per_unit'))

	cur.execute(query, data)

	cnx.commit()

	return cur.lastrowid

def get_some_product(cnx, pname):
	cur = cnx.cursor()

	query = """select p.product_id, p.name, p.uom_id, p.price_per_unit, u.uom_name from products p inner join 
			   uom u on p.uom_id=u.uom_id where p.name like %s"""

	cur.execute(query, (f"%{pname}%",))

	response = []

	for (product_id, name, uom_id, price_per_unit, uom_name) in cur:
		response.append(
			{
				"product_id": product_id,
				"name": name,
				"uom_id": uom_id,
				"price_per_unit": price_per_unit,
				"uom_name": uom_name
			}
		)

	return response


def delete_product(cnx, product_id):
	cur = cnx.cursor()

	query = ("delete from products where product_id="+str(product_id))

	cur.execute(query)
	cnx.commit()


if __name__ == "__main__":
	cnx = get_sql_connection()
	# print(get_all_products(cnx))
	# print(insert_new_product(cnx, {'product_name': 'spinach', 'uom_id': '1', 'price_per_unit': '20'}))
	delete_product(cnx, 9)