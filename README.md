# Span

My approach to the span coding test. I had at least 4 different designs on how this could be done.
They all had their pros and cons - the one I settled on is probably overkill for this simple task,
however it does have the advantage of utilising some of python's most elegant functionalities 
especially as it relates to data abstraction. In a larger project, they could be the difference
between elegant, readable code or spaghetti.

## Usage:
The code was written and tested on a Linux system running python 3.7.0 - but should work in pretty much any unix-like system
with python 3. No external dependencies were used, only python native libraries.

To run the main program:
`./leaguetable -m sampleInput.txt`
You can replace 'sampleinput.txt' with any valid match-results input file. As per the given instructions I didn't add any input validation so it will break if the format is invalid.

To run the unit tests:
`./test.py`

The bulk of the actual logic is in the module: leagueTable.py

