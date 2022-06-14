<ins>Run:</ins>
1. Create a python virtual environment and activate it(i.e 'virtulenv venv', 'source venv/bin/activate')
2. Install the dependancies('pip install requirements.txt')
3. To run the programm run "python main.py" from the files main directory.

<ins>Project structure:</ins>
The project is structured as folows;
    entry point:
        -main.py
    Databases:
        -db.json - This is a json database of the full list catalogue of the cart application
        -db2.json - This is json database of the cart as it stands before being confirmed as an order (It is truncted after every order confirmation)
        -db3.json - This is json database of all the confirmed orders made on the application
    Tests:
        -test.py
        -kyostestcases.xlsx - Contains the test cases of the application functionality in excel format

<ins>Unit Tests:</ins>
Since Ive configured my application to have functions that dont take any arguments, I have used the **patch** method to to add mock data to my function testing.
To run the tests:
    -python run tests.py

