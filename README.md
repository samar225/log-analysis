# log analysis project

this project is a required project in udacity nanodegree. It is about database and queries.
## Requirements
in order to run this project you need:
1. [Vagrant](https://www.vagrantup.com/downloads.html) .
2. [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
3. [Vagrant](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile) file as provided by Udacity.

## Download datahbase
[newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
### Database content 
it contain 3 tables:
1. artiales
 Column | Type         |
------------------------
 author | integer        
 title  | text           
 slug   | text           
 lead   | text            
 body   | text      
 time   | timestamp 
 id     | integer                 

2.author
   1. has author name , id and bio.
   
3.log 
   1.The log table has a database row for each time a reader access a web page.
   2.The log table includes a column status that indicates the HTTP status code
that the news site sent to the user's browser.
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
