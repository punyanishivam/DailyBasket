# DailyBasket

Daily Basket is an e-commerce platform from LikeMinds. The various functionalities
required to be implemented are listed below.

Functionalities added
1. Create an item
2. Add item to inventory
3. Add user in the system
4. Add/remove items to the user’s current cart. Orders can only be placed from
the user’s wallet.
5. Get the current cart info of the user
6. Cart checkout for a user

Project structure

- Models
      base_models.py

- Service
      CartCheckoutService.py

- driver.py


**Most of the functionality has been added as class methods
**Only cart checkout has been designed as a separate service
**CartCheckoutServiceInterface could not be implemented due to time constraint
