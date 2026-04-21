# Cost of Living Project Documentation

## Project Overview
This project aims to provide comprehensive insights into the cost of living across different regions. By aggregating data from various sources, it enables users to compare living expenses and make informed decisions.

## Tech Stack
- **Frontend:** React.js
- **Backend:** Node.js, Express
- **Database:** MongoDB
- **Deployment:** Heroku

## Database Schema
- **Users:** { userId, username, password, email }
- **Expenses:** { expenseId, userId, category, amount, date }
- **Categories:** { categoryId, name }

## API Endpoints
1. **GET /api/expenses** - Retrieve all expenses for the logged-in user.
2. **POST /api/expenses** - Add a new expense.
3. **DELETE /api/expenses/{id}** - Delete an expense by ID.
4. **GET /api/categories** - Retrieve all expense categories.

## Installation Guide
1. Clone the repository:
   ```bash
   git clone https://github.com/SuhasGowda24/Mini_Project-Cost_of_living.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Mini_Project-Cost_of_living
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Configure the database:
   1. Create a `.env` file in the root directory.
   2. Add your MongoDB connection string to the `.env` file.
5. Start the application:
   ```bash
   npm start
   ```

## Features
- User authentication and authorization.
- Expense tracking with detailed categorization.
- Visualized reports of expense trends over time.

## Code Examples
### Fetching Expenses
```javascript
fetch('/api/expenses')
  .then(response => response.json())
  .then(data => console.log(data));
```

### Adding an Expense
```javascript
const addExpense = async (expense) => {
  const response = await fetch('/api/expenses', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(expense)
  });
  return response.json();
};
```

## Deployment Information
To deploy the application:
1. Ensure all dependencies are installed.
2. Push the code to the Heroku repository:
   ```bash
   git push heroku main
   ```
3. Open your Heroku app in the browser.

---
For further questions or issues, please reach out to the project maintainer.