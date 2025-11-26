Alexander Al. D
November 25th, 2025

  While I was originally a little bit intimidated by the concept of doing one homework assignment 5 different times, I was interested in finding new ways to solve the problem. My original idea
was to break down each movies title and quote into numerical digits that I could use to hash a random index.  This method was simple and didn't require much thought. I decided to add a little more randomness to the hash by multiplying the index by
7 as I thought the algorithm required to hash the index should be more complex. I chose 7 because during class we were told to keep prime numbers in mind as they would be useful later. After using seven to randomize the hash index a little bit more uniquely
I had brought down the time required to hash all the data from ~8 seconds to .23. My next attempt at making a hash function ended up being a little bit more complex, with a more layered algorithm that did more than 
just a simple mathmatic equation. My second hash function would append the numerical value of a letter in a movies quote/title if the index of that letter was even. Otherwise it would multiply the entire index, thus far, by that letters numerical value. The 
added check for even and odd indexes was helpful but ultimately was not resource efficient and was slower than my original hash function by .1 seconds for a total of .33 seconds. For my third hash function I had simply attempted to mix both my first and second hash functions, however,
before beginning the loop through a movie's title/quote, I would reverse that title/quote. This method was by far the slowest and the least efficient at .64 seconds. My fourth hash function was by far the most interesting, I had viewed it as just a way to redeem 
my third hash function. I had decided instead of trying to compute one hash with two different algorithms, I would just calculate two different hashs' at once and add them up. Overall my fourth method was the most interesting to 
develop, yet it fell short of being the quickest as it was clocked at around .24 seconds. My final and fifth hash method was much simpler in coding but much more complicated mathematically. I had realized I used 
every other mathematical operation besides exponents. I had decided to apply the same logic as the first hash function but with the inclusion of exponential multiplication. This method was fast but not the fastest, coming in at .26 seconds. Overall the fastest 
method was the first, at .23 seconds, as it was the simplest and least expensive method, while the slowest was the fourth hash function at .6 seconds.
