An outsourced company (one of the market leaders) is preparing for a corporate event. The HR department sent a questionnaire about the types of beer that can be distributed at the holiday. Most of the company's employees like a few types of beer, and will be very offended if at least one of the beers they like is not available at the party. Since you are the market leader, you cannot insult employees.
On the other hand, buying all possible types of beer is expensive. Your task will be to find out how many different types of beer you need to bring to the corporate party.


Input:
The first line contains the numbers N - the number of employees and B - the number of available beers. The second line contains N*B letters N or Y. If letter i*N + j - Y, then employee i likes beer j

Output data:
The smallest number of types of beer that should be on the holiday

Limitation:
Every employee likes at least one type of beer
0 < N < 50
0 <B < 50
Examples:
In:
2 2
YN NY
Out:
2
(The first employee only likes beer 1, and the second only likes beer 2, so you will have to buy two types of beer)

In:
6 3
YNN YNY YNY NYY NYY NYN
Out:
2
(Although the majority - four employees - like the third beer, it will be optimal to buy 1 and 2 varieties)
