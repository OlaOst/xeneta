1) Explain what a closure is. Give a simple closure example in a
language of your choice. Try to make it somewhat meaningful, a "Hello
world" type of function isn't a great example.

2) Define a Python decorator that will cache the results of an
expensive computation, so if it is called with the same parameters
again, it'll return the result immediately.

3) Define a recursive method that will return the Nth Fibonacci
number. Print out the 10th - fib(10) . What's the computational
complexity of this calculation?

 3a) Print out the 100th Fibonacci number. Make sure this completes in
less than a minute.

 3b) Print out the 1200th Fibonacci number. Make sure this completes
before the universe expires.

4) Create a simple web application in Python, which allows you to
upload a text file. It also displays a list of the already uploaded
files. Don't go overboard thinking about the storage, just putting
them in /tmp/ is fine. When a file is selected, the file will be
analysed - count all unique words in the file and return the top 20
words there. Display those in the browser in a graphical form, any
form of graph/chart you think is suitable. Make sure the word counting
is efficient enough to handle a high number of requests per second
(you're running on a single server and there's no Varnish cache for
you).
