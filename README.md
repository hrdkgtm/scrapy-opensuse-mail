# scrapy-opensuse-mail

This is a scrapy project that sole purpose is to crawl OpenSUSE Mailing List page **based on year and month**, parse them, and output them in the form of JSON lines. 

An oversimplified steps of this spider are :

- Get the link based on the category and date (e.g. https://lists.opensuse.org/opensuse-announce/2018-12/all.html), where `opensuse-announce` is the category and `2018-12` is the date
- Get into each and every link in that page that contains `msgXXXXX.html` where X is a number
- Parse the needed fields into a scrapy item
- Return that item

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for production, development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project was created using :

- Python 3.7
- Scrapy 1.5.1
- BeautifulSoup 4.7.0

Incompatibility with older and newer versions of software are unknown.

All the prerequisites are python prerequisites and can be installed using pip

```
$ pip install --user BeautifulSoup==4.7.0 #for beautifulsoup
$ pip install --user scrapy==1.5.1 #for scrapy
```

### Installing

To get a development env running, first, clone this repository to your folder, and cd into it


```
$ git clone https://gitlab.s8i.io/hrdkgtm/scrapy-opensuse-mail.git
$ cd scrapy-opensuse-mail
```

Then, try to run the spider with :

```
$ scrapy crawl mail_spider -a category=opensuse-bugs -a date='2018-12' -s FEED_URI=bugs.json
```

This will call the `mail_spider` to crawl the opensuse-bugs category for **December 2018**, and then save the parsed output to a file (bugs.json) inside your current directory. 

Try to cat or head the parsed data and you should see something like this :
```
$ head -1 bugs.json
{"subject": "[Bug 1117086] Automatic cleanup of old kernels not working", "origin": "bugzilla_noreply@xxxxxxxxxx", "date": "Sat, 01 Dec 2018 00:47:41 +0000", "src_link": "https://lists.opensuse.org/opensuse-bugs/2018-12/msg00000.html", "reference_link": ["http://bugzilla.opensuse.org/show_bug.cgi?id=1117086", "http://bugzilla.opensuse.org/show_bug.cgi?id=1117086#c3"], "msg_body": "\n\n\nhttp://bugzilla.opensuse.org/show_bug.cgi?id=1117086\nhttp://bugzilla.opensuse.org/show_bug.cgi?id=1117086#c3\n\nbob wheater <bwheater@xxxxxxx> changed:\n\n           What    |Removed                     |Added\n----------------------------------------------------------------------------\n                 CC|                            |bnc-team-screening@xxxxxxxx\n                   |                            |ovo.novell.com\n   Target Milestone|---                         |Leap 15.0\n              Flags|                            |needinfo?(bnc-team-screenin\n                   |                            |g@xxxxxxxxxxxxxxxxxxxxxx)\n\n--- Comment #3 from bob wheater <bwheater@xxxxxxx> ---\nWhat is the status of this bug report?\n\n-- \nYou are receiving this mail because:\nYou are on the CC list for the bug.\n\n\n\n\n"}

```

Here are all the fields that this spider will parse
- `subject` = the subject of the message
- `origin` = the sender of the message
- `date` = the date the message was sent
- `src_link` = the origin url that the message was parsed from
- `referece_link` = any links that is mentioned in the mail

## Deployment

For production use, ideally you would have a `scrapyd` server running somewhere, and then you can deploy this project to that server using `scrapyd-deploy` which can be run from inside the project.

`scrapy.cfg` is the file to configure if you are going to deploy this to a live environment. which looks like this and very straightforward

```
[settings]
default = opensuse_mail.settings

[deploy]
url = http://localhost:6800/
project = opensuse_mail
version = 1.0.0
```

Change the [deploy] section to match your scrapyd server.

If you want the crawler to actively checks for changes, theres a separate [project](https://gitlab.s8i.io/hrdkgtm/scrapyd-opensuse) that wraps everything to a bash script and systemd unit files. 



## Built With

* Python
* Scrapy web crawler
* BeautifulSoup html parser

## Versioning
   
Semantic Versioning

## Known issues
   
* All the known problems, bugs listed here. Add link to issues if any.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE.md file for details
