# HNG STAGE-1 Number Classification API

This project is a FastAPI-based web service that classifies numbers based on various properties such as whether they are prime, perfect, Armstrong numbers, and more. It also provides fun facts about numbers using the Numbers API.

## Features

- Check if a number is prime
- Check if a number is perfect
- Check if a number is an Armstrong number
- Determine if a number is even or odd
- Calculate the sum of the digits of a number
- Get fun facts about numbers

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AyoIbitola/HNG-1.git
    cd HNG-1
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    uvicorn main:app --reload
    ```

5. Open your browser and navigate to:
    ```sh
    http://127.0.0.1:8000/api/classify-number?number=<your number>
    ```
    

## Endpoints

### Endpoint URL
```sh
https://hng-1-production-e822.up.railway.app/api/classify-number?number=<your number>
```
### GET /api/classify-number

Classifies a number based on various properties.

#### Query Parameters

- `number` (required): The number to classify.

#### Response

- `number`: The input number.
- `is_prime`: Boolean indicating if the number is prime.
- `is_perfect`: Boolean indicating if the number is perfect.
- `is_armstrong`: Boolean indicating if the number is an Armstrong number.
- `properties`: List of properties the number satisfies.
- `digit_sum`: Sum of the digits of the number.
- `even_or_odd`: Indicates if the number is even or odd.
- `fun_fact`: A fun fact about the number.

#### Example Request

```sh
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
}

```
