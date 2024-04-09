# **BillingCounterAPI**

Billing Counter API is a RESTful API designed to handle billing and inventory management functionalities. It provides endpoints for managing users, products, ordered products, and bills. The API is live at https://billingcounterapi.onrender.com/.

**Database**

The production database for Billing Counter API is powered by PostgreSQL.

**Hosting**

The API is hosted on Render, ensuring reliability and scalability.

**Endpoints**

1. Users
   
GET /users: Retrieve a list of all users.

GET /users/{id}: Retrieve a specific user by ID.

POST /users: Create a new user.

PUT /users/{id}: Update an existing user.

DELETE /users/{id}: Delete a user by ID.

2. Products

GET /products: Retrieve a list of all products.

GET /products/{id}: Retrieve a specific product by ID.

POST /products: Create a new product.

PUT /products/{id}: Update an existing product.

DELETE /products/{id}: Delete a product by ID.

3. Ordered Products

GET /orderedproducts: Retrieve a list of all ordered products.

GET /orderedproducts/{id}: Retrieve a specific ordered product by ID.

POST /orderedproducts: Create a new ordered product.

PUT /orderedproducts/{id}: Update an existing ordered product.

DELETE /orderedproducts/{id}: Delete an ordered product by ID.

4. Bill
 
GET /bills: Retrieve a list of all bills. 

GET /bills/{id}: Retrieve a specific bill by ID.
 
POST /bills: Create a new bill.

PUT /bills/{id}: Update an existing bill.

DELETE /bills/{id}: Delete a bill by ID.

**Authentication**

Authentication is required to access the endpoints. JWT (JSON Web Token) is used for authentication. Endpoints /token/ and /token/refresh/ are provided for user authentication. To be authenticated, users must send the following header in each request

## Authorization: Bearer ${access_token}

Replace ${access_token} with the actual access token obtained after successful authentication.

Usage
You can use any HTTP client (such as cURL, Postman, or Axios) to interact with the API endpoints. Ensure you include the required authentication headers for each request.

Sample cURL Request
bash
Copy code
curl -X GET "https://billingcounterapi.onrender.com/users" -H "Authorization: Bearer ${access_token}"
Replace ${access_token} with the actual access token.

Note
Ensure that only authenticated users have access to these endpoints to maintain the security and integrity of the system.
