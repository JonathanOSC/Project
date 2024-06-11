# Course Project - Managment sales

In this project in the backend system we are using object-orientend design , design-patterns, good code practices to make an app where we can create, delete and update products, make a sell, sales report, among others.

## Business Model 

The project is based on an application in which you can manage the sales of a restaurant, see your daily and monthly earnings, your cats, the management of possible restaurant addresses and management of your products and tables of the premises. 

For this, there is a stakeholder named Jonathan Ochoa, who will be in charge of the decisions about the project. A business model that explains this where the customer/user, the software, the connection with the printer, and connection with the database are taken as elements, all this to be able to generate the total sales and invoice if necessary. 
Figure 1 shows this model graphically.

!

## User Stories

- As a __client__, I want __to add products__, so what __I can define the products__.

- As a __client__, I want __to delete products__, so what __I can remove products__.

- As a __client__, I want __to update products__, so what __I can update the info of the  products__.

- As a __client__, I want __to delete a sale__, so what __I can correct and sell error__.

- As a __client__, I want __to make a sale__, so what __I can see the total value and the quantity of products here__.

- As a __client__, I want __to see the inventory__, so what __I can keep a daily report to corroborate info__.

- As a __client__, I want __to keep track of the products on each table__, so what __I can have a report of this__.

## Technical Definitions

### Tools to use

In this case, the backend will be build using python 3.10, and some related technologies as Fast API to server functionalities, PyTest to apply some simple unit test, Postman and SQLAlchemy.

## Entities



- Product: product_id, name, price, quantity_available

- Sale: sale_id, total_value, time, complete_sale(), get_all_sales(), get_all_products_sales()

- Inventory: product[E], add_product(), remove_product(), update_product(), get_all_products(), get_product

- Table: id_table, sale[E]

- TableService: db, get_all_table(), get_table(), create_table(), add_product_to_table(), remove_product_to_table(), close_table()

## Processes

- Add products
- Delete products
- Update products
- Delete a table
- See inventory
- See all sales






