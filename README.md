
  

<ins>**Run:**</ins>

  

1. Create a python virtual environment and activate it(i.e 'virtulenv venv', 'source venv/bin/activate').

  

2. Install the dependancies('pip install requirements.txt').

  

3. To run the programm run "python main.py" from the files main directory.

  
  

<ins>**Project structure:**</ins><br  />

  

The project is structured as folows;<br  />

  

&nbsp;&nbsp;&nbsp;**1. Entry point:**<br  />

  

&nbsp;&nbsp;&nbsp;&nbsp;-main.py<br  />

  

&nbsp;&nbsp;&nbsp;**2. Databases:**<br  />

  

&nbsp;&nbsp;&nbsp;&nbsp;-db.json - This is a json database of the full list catalogue of the cart application.<br  />

  

&nbsp;&nbsp;&nbsp;&nbsp;-db2.json - This is json database of the cart as it stands before being confirmed as an order (It is truncted after &nbsp;&nbsp;&nbsp;&nbsp; every order confirmation).<br  />

  

&nbsp;&nbsp;&nbsp;&nbsp;-db3.json - This is json database of all the confirmed orders made on the application.<br  />

  

&nbsp;&nbsp;&nbsp;**3. Test cases:**<br  />

  

&nbsp;&nbsp;&nbsp;&nbsp;-kyostestcases.xlsx - File in tests contains the test cases of the application functionality in excel format.<br  />

  

<ins>**Unit Tests:**</ins><br  />

  

I've configured my application to have functions that don't take any arguments; I will only test whether there is an output from my function call - and the output type in my functional testing.<br  />

  

&nbsp;&nbsp;&nbsp;&nbsp;-To run the tests:<br  />

  

&nbsp;&nbsp;&nbsp;&nbsp;-Make sure you are in the root directory, then <br  />

&nbsp;&nbsp;&nbsp;&nbsp;-run py.test test.py -s<br  />