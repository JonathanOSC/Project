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

- As a __client__, I want __to edit the sales check__, so what __I can change the information here__.

- As a __client__, I want __to see the month/dar sales__, so what __I can get a preview of the monthly/day sales__.

- As a __client__, I want __to make a sale__, so what __I can see the total value and the quantity of products here__.

- As a __client__, I want __to print a sale__, so what __I can give to the client the sales check__.

- As a __client__, I want __to see and print the inventory__, so what __I can keep a daily report to corroborate info__.

- As a __client__, I want __start a sales day__, so what __I can make the start daily sales__.

- As a __client__, I want __end a sales day__, so what __I can make the end daily sales and receive a report of the sales__.

- As a __client__, I want __add a spent__, so what __I can keep a report of this__.

- As a __client__, I want __to keep track of the products on each table__, so what __I can have a report of this__.

## Technical Definitions

### Tools to use

In this case, the backend will be build using python 3.10, and some related technologies as Fast API to server functionalities, PyTest to apply some simple unit test, Postman and SQLAlchemy.

## Entities

- Client: name, password, make_sale(), print_sale(), start_sales_day(), end_sales_day(), , track_table_products()

- Product: product_id, name, price, quantity_available, update_price(), update_quantity()

- Sale: sale_id, products_sold, total_value, time, calculate_total_value(), print_sales_check(), add_product_sale(), delete_product_sale(), remove_sale(), 

- Inventory: product[E], add_product(), delete_product(), update_product(), print_inventory_report()

- SalesRerport(Sale): start_date, total_price, products_quantity[E], products_name[E], add_spent(), view_sales_report(), print_sales_report()

- Table: id_table, sale[E]

## Processes

- Add products:
  
- Delete products: -> Preguntar
- Update products: -> Preguntar
- Delete a sale: -> Preguntar
- Edit the sales check:
  
- See month sales:
- Print a check sale:
- Start day:
- End day:
- Add spent:
- See and print inventory:









