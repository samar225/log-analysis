# log analysis project

this project is a required project in udacity nanodegree. It is about database and queries.
## Requirements
in order to run this project you need:
1. Vagrant.[Vagrant](https://www.vagrantup.com/downloads.html) 
2. VirtualBox.
3. Vagrant file as provided by Udacity.
## Download datahbase
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

## run
to run the code you first have to connect to database
```bash
psql -d news -f newsdata.sql
```
then 
```bash
psql -d news 
```
## Run 
to run the code in terminal type 
```bash
   log-projec.py
```
   
## Questions

1. What	are	the	most	popular	three	articles	of	all	time?		
2. Who	are	the	most	popular	article	authors	of	all	time?		
3. On	which	days	did	more	than	1%	of	requests	lead	to	errors?	
