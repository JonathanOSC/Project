"""
    This module contains the User class, which represents a user of the system.

    Author: Jonathan
"""



from datetime import datetime

from sale_subsystem import SaleFacade

class User:

    def __init__(self, username: str, password: SecretStr, sale_facade: SaleFacade):
        self.username = username
        self.password = password
        self.start_time = None
        self.end_time = None
        self.sale_facade = sale_facade
        self.sales_completed_today = []

    def start_day(self) -> datetime:
        """ Starts the day of sales """
        self.start_time = datetime.now()
        print(f"{self.username} ha iniciado su día a las {self.start_time}")
        return self.start_time

    def end_day(self) -> datetime:
        """ Ends the day of sales """
        self.end_time = datetime.now()
        print(f"{self.username} ha terminado su día a las {self.end_time}")
        self.sales_completed_today = [sale for sale in self.sale_facade.sales_history if self.start_time <= sale.time <= self.end_time]
        return self.end_time