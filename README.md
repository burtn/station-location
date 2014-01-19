### What is this?

A python script which pulls LAT, LONG & OS GRID REF data for UK railway stations from Wikipedia. I wrote it because I just wanted a list of rail stations and associated locations and it seemed like far too much work figuring out ATOC's CIF format or parsing open street map data.

**The most recent scrape can be found in the file `data.csv`**

###### Other Files

`noGRIDREF.txt` contains a list of the stations which are missing OS GRID REF data.

`noGEODATA.txt` contains a list of the stations which are missing Lat, Long data.

###### Running

Edit the values of `MAX_WAIT`, `MIN_WAIT` and the `useragent` string (*optional*)

Run `python fetchraildata.py`, the files detailed above are stored in the same directory as the script.

# Licence

Copyright (c) 2012 Jake Burton

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
