# Course Project - Managment sales

In this project in the backend system we are using object-orientend design , design-patterns, good code practices to make an app where we can create, delete and update products, make a sell, sales report, among others.

## Business Model 

The project is based on an application in which you can manage the sales of a restaurant, see your daily and monthly earnings, your cats, the management of possible restaurant addresses and management of your products and tables of the premises. 

For this, there is a stakeholder named Jonathan Ochoa, who will be in charge of the decisions about the project. A business model that explains this where the customer/user, the software, the connection with the printer, and connection with the database are taken as elements, all this to be able to generate the total sales and invoice if necessary. 
Figure 1 shows this model graphically.

!

## User Stories

- As a __client_administrator__, I want __to create profiles__, so what __I can administrate/get privacity in the information__.

- As a __client_administrator__, I want __to add products__, so what __I can define the products__.

- As a __client_administrator__, I want __to delete products__, so what __I can remove products__.

- As a __client_administrator__, I want __to update products__, so what __I can update the info of the  products__.

- As a __client_administrator__, I want __to delete a sale__, so what __I can correct and sell error__.

- As a __client_administrator__, I want __to edit the sales check__, so what __I can change the information here__.

- As a __client_administrator__, I want __to see the month sales__, so what __I can get a preview of the month sales__.

- As a __client__, I want __to make a sale__, so what __I can see the total value and the products here__.

- As a __client__, I want __to print a sale__, so what __I can give to the client the sales check__.

- As a __client__, I want __to see and print the inventory__, so what __I can keep a daily report and corroborate info__.

- As a __client__, I want __start a sales day__, so what __I can make the start daily sales__.

- As a __client__, I want __end a sales day__, so what __I can make the end daily sales and receive a report of the sales__.

- As a __client__, I want __add a spent__, so what __I can keep a report of this__.

- As a __client__, I want __to keep track of the products on each table__, so what __I can have a report o this__.

## Technical Definitions

### Tools to use

In this case, the backend will be build using python 3.10, and some related technologies as Fast API to server functionalities, PyTest to apply some simple unit test, Postman and SQLAlchemy.

## Entities

- Client: name, email, make_sale(), print_sale(), print_inventory(), start_sales_day(), end_sales_day(), add_spent()
  
- Adiminitrator(Client): create_profile(), add_product(), delete_product(), update_product(), delete_sale(), edit_sale(), view_monthly_sales(), track_table_products()

- Product: product_id, name, price, quantity_available, update_price(), update_quantity()

- Sale: sale_id, products_sold, total_value, time, calculate_total_value(), print_sales_check()

- Inventory: products, add_product(), delete_product(), update_product(), print_inventory_report()

## Processes

- Create profiles:
- Add products:
- Delete products:
- Update products:
- Delete a sale:
- Edit the sales check:
- See month sales:
- Print a check sale:
- Start day:
- End day:
- Add spent:
- See and print inventory:









