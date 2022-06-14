<ins>Run:</ins>
&nbsp;&nbsp;&nbsp;1. Create a python virtual environment and activate it(i.e 'virtulenv venv', 'source venv/bin/activate')
&nbsp;&nbsp;&nbsp;2. Install the dependancies('pip install requirements.txt')
&nbsp;&nbsp;&nbsp;3. To run the programm run "python main.py" from the files main directory.

<ins>Project structure:</ins><br />
The project is structured as folows;<br />
&nbsp;&nbsp;&nbsp;1. entry point:<br />
&nbsp;&nbsp;&nbsp;&nbsp;-main.py<br />
&nbsp;&nbsp;&nbsp;2. Databases:<br />
&nbsp;&nbsp;&nbsp;&nbsp;-db.json - This is a json database of the full list catalogue of the cart application<br />
&nbsp;&nbsp;&nbsp;&nbsp;-db2.json - This is json database of the cart as it stands before being confirmed as an order (It is truncted after every order confirmation)<br />
&nbsp;&nbsp;&nbsp;&nbsp;-db3.json - This is json database of all the confirmed orders made on the application<br />
&nbsp;&nbsp;&nbsp;3. Tests:<br />
&nbsp;&nbsp;&nbsp;&nbsp;-test.py<br />
&nbsp;&nbsp;&nbsp;&nbsp;-kyostestcases.xlsx - Contains the test cases of the application functionality in excel format<br />

<ins>Unit Tests:</ins><br />
Since Ive configured my application to have functions that dont take any arguments, I have used the **patch** method to to add mock data to my function testing.<br />
&nbsp;&nbsp;&nbsp;:- To run the tests:<br />
&nbsp;&nbsp;&nbsp;&nbsp;:-python run tests.py<br />

