# Commands

## Info!
For user's with default account id in url (https://www.facebook.com/profile.php?id=100063142210972)
some of the scrapers may not work 
- work and education
- contact data
- visited place
- family member 
- recent places
- reviews
- likes 

This issue doesn't occur while facebook account has a custom id in url (https://www.facebook.com/zuck)

I am working on to fix this issue. 

## Basic commands

#### Version
Display current version of the project
```bash
python main.py version
```

## Log in
#### 2-step verification
```bash
python main.py login-2-step
```
#### Default log in
```bash
python main.py login
```

## Account & Page scrapers
- By default this commands were created to scrape accounts but many of them also works for pages 
- If some option doesn't work for a PAGE there is a note like this "🛑 Page not support"

#### Basic scraping 
This command allows to scrape history of employment and education, full name, family members, contact data and visited places

From version v1.2 this command can run all selected scrapers in parallel
```bash
python main.py scrape-basic-data <facebook_id>
```
After running this command use arrows keys to navigate through the list of possible scrapers <br>
- Use Arrow Up/Arrow Down to go Up and Down 
- Use Arrow Right to select scraper 
- User Arrow Left to delete selected scraper

![Basic Scraper Console](https://github.com/DEENUU1/facebook-spy/blob/main/assets/v1_2/basic.gif?raw=true)
![Basic Scraper Console](https://github.com/DEENUU1/facebook-spy/blob/main/assets/scrapebasicdataconsole.png?raw=true)

#### Full scraping
From version v1.2 this command can run all selected scrapers in parallel
- If you provide only 1 username all selected scrapers will be launched in parallel
- By providing more than 1 username it's gonna scrape them in parallel

This command allows to choose all available commands to scrape facebook profiles

Also you are able to add multiply facebook profile ids as a single argument 

To scrape one account your command should looks likes this
```bash
python main.py full-scrape <facebook_id>
```

![Full Scraper Console](https://github.com/DEENUU1/facebook-spy/blob/main/assets/v1_2/full.gif?raw=true)

TO scrape multiply accounts user command should looks like this
```bash
python main.py full-scrape <facebook_id> <facebook_id> <facebook_id> ... 
```

After running this command use arrows keys to navigate through the list of possible scrapers <br>
- Use Arrow Up/Arrow Down to go Up and Down 
- Use Arrow Right to select scraper 
- User Arrow Left to delete selected scraper

![Basic Scraper Console](https://github.com/DEENUU1/facebook-spy/blob/main/assets/fullscrapeconsole.png?raw=true)


#### Friend list 🛑 Page not support
```bash
python main.py scrape-friend-list <facebook_id>
```
#### Image
Scrape and download images from user's facebook profile
```bash
python main.py scrape-images <facebook_id>
```
#### Recent places 🛑 Page not support
```bash
python main.py scrape-recent-places <facebook_id>
```
#### Videos
Scrape only urls of videos from user's facebook profile
```bash
python main.py scrape-video-urls <facebook_id>
```
#### Reels
Scrape only urls of reels from user's facebook profile
```bash
python main.py scrape-reels <facebook_id>
```
#### Reviews
```bash
python main.py scrape-reviews <facebook_id>
```

#### Posts
Scrape post urls from user's facebook profile
```bash
python main.py scrape-person-posts <facebook_id>
```

Scrape post details (content, number of likes;comments;shares etc) based on previously scraped post urls for specified facebook profile
```bash
python main.py scrape-person-post-details <facebook_id>
```

Scrape post details based on post URL 
- In database Posts scraped based on a given URL are in relation with object Person with ID - "Anonymous"
```bash
python main.py scrape-post-details "<post_url>"
```
I recommend to paste post url inside " " to avoid errors 

#### Likes
Scrape likes from facebook account 
```bash
python main.py scrape-person-likes <facebook_id> 
```

#### Groups
Scrape groups from facebook account
```bash
python main.py scrape-person-groups <facebook_id>
```

#### Events
Scrape events from facebook account
```bash
python main.py scrape-person-events <facebook_id>
```



## Local Web Application
#### Run FastAPI application 
App is available under this local url - http://localhost:8000/

```bash
python main.py server
```


## Video downloader
Download Videos based on previously scraped urls from facebook profile 
```bash
python main.py download-person-videos <facebook_id>
```
After running this command use arrows keys to navigate through the list of possible scrapers <br>
- Use Arrow Up/Arrow Down to go Up and Down 
- Use Arrow Right to select scraper 
- User Arrow Left to delete selected scraper

![Basic Scraper Console](https://github.com/DEENUU1/facebook-spy/blob/main/assets/downloadvideosconsole.png?raw=true)

Download single video from facebook 
```bash
python main.py download-video <facebook_video_url>
```


## Analitics 
#### Graph
To create a graph of connections between Person objects based on their Friends use this command
```bash
python main.py graph 
```
![Basic Scraper Console](https://github.com/DEENUU1/facebook-spy/blob/main/assets/graph.png?raw=true)


#### Report
Save scraped data for specified Person object to PDF file 
```bash
python main.py report <facebook_id> 
```

#### AI Summary
Use free open source LLM model to create a short summary for specified Person object based on scraped data 
```bash
python main.py summary <facebook_id>
```

#### Post classification using transformer 

```bash
python main.py posts <option>

Options:
--display-all  // Display all posts from the database
--id // Display a specified post from the database
--person-id //  Display posts for a specified person from the database

```

```bash
python post-classifier <option>

Options:
--all-posts // Run post classification for all posts from the database
--id // Run post classification for specified post from the database
--person-id // Run post classification for a specified person from the database
```


## Friend Crawler 
This command works similarly to the command that scrapes data about a given user's friends list. The difference, however, is that after scraping and creating Friend objects, it also creates objects for the CrawlerQueue model and after successfully scraping friends for one user, it proceeds to scraping the list of friends for the next user in the queue.

![Friend crawler schema](https://github.com/DEENUU1/facebook-spy/blob/main/assets/crawlerfriendscheama.png?raw=true)


#### Run crawler
Start crawler for specified facebook account 
```bash
python main.py friend-crawler <facebook_id>
```

#### Display queue
Display all objects available in the queue
```bash
python main.py display-queue
```

#### Delete queue object
Delete specified queue object 
```bash
python main.py delete-queue-object <id>
```

#### Clear queue
Delete all objects from the queue 
```bash
python main.py clear-queue
```

## Search
This command allows to search for: places, pages, person, groups, events, posts 


```bash
python main.py search < "Search Query" > < number_of_results > 
```

- Search query should be in double " "
- Number of results MUST be an integer 

After running this command you can select which data you would like to scrape 
Result's will be saved in this directory /facebookspy/scraped_data/

![Search  Scraper Console](https://github.com/DEENUU1/facebook-spy/blob/main/assets/v1_2/search.gif?raw=true)