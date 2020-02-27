# :cat: Kittenz – Pyro-Skeleton-Async: :cat:

This project was built to demonstrate how we at [@baivaru](https://t.me/Baivaru) structures - 
our async [pyrogram](https://docs.pyrogram.org/) projects. I could have written a skeleton (directory structures, modules 
showing where plugins are loaded from and etc) which you could simply clone and build upon. 
However, doing that could have left you halfway through the whole purpose of “making it easier” 
and having a skeleton. Therefore, the following project is a fully functional [bot](https://t.me/Kittenzbot) that demonstrates 
most of the common methods, functionalities that [pyrogram](https://docs.pyrogram.org/) offers you to start programing a simple telegram bot 
and some clean practices that we at [@baivaru](https://t.me/Baivaru) follow which you could refer and imply with your projects.

## Cloning & Run:

1. `git clone https://github.com/eyaadh/pyro-sekeleton-async.git`, to clone the repository.
2. `cd pyro-sekeleton-async`, to enter the directory.
3. `pip3 install -U https://github.com/pyrogram/pyrogram/archive/asyncio.zip`, to install pyrogram-asyncio.
4. `pip3 install -r requirements.txt`, to install rest of the dependencies/requirements.
5. Create a new `config.ini` using the sample available at `pyro-sekeleton-async\working_dir`.
6. Run with `python3.8 -m pyro`, stop with <kbd>CTRL</kbd>+<kbd>C</kbd>.
> It is recommended to use [virtual environments](https://docs.python-guide.org/dev/virtualenvs/) while running the app, this is a good practice you can use at any of your python projects as virtualenv creates an isolated Python environment which is specific to your project.

## Directory Structures:

```
pyro-sekeleton-async/
└── pyro/
    ├── plugins/
    ├── utils/
    │   └── helpers/
    └── working_dir/
```
#### plugins:
This directory consists of Pyrogram's a smart, lightweight yet powerful plugin's which enables 
us to simplify and organize large projects with modular base components. More in regards to 
smart plugins can be found [here.](https://docs.pyrogram.org/topics/smart-plugins) 

#### utils:
The name utils define exactly what this directory is for. All the 3rd party utilities (which do not deal with telegram & pyrogram) 
that helps the application to work through is kept in this directory, such as DB module (if that exists), a module called common 
which loads the required external variables(mostly configurations from configs.ini) and etc.

#### helpers:
Helpers directory consists of modules that connects to 3rd party APIs to help the application gather 
the data it requires.

#### working_dir:
This directory basically consists of the config.ini file/s, the session file/s generated by the 
application. Also if there are temporary files that are generated by the application we tend to leave them 
within this directory at the course of their existence.

## Config.ini:

As explained on the pyrogram [configuration](https://docs.pyrogram.org/intro/setup#configuration), the library allows us to make 
use of a `config.ini` file: in which we could specify the credentials, api keys and other variables that we do not want
to share within our source code. \
The configuration file consists of sections, each led by a `[section]` header, followed by 
key/value entries separated by a specific string (= or : by default). By default, section names are case sensitive 
but keys are not. Leading and trailing whitespace is removed from keys and values. Values can be omitted, in which 
case the key/value delimiter may also be left out. Values can also span multiple lines, as long as they are indented 
deeper than the first line of the value. The values mentioned on configuration files are parse using the `pyro/utils/common.py` module. \
More details on config files and configparser can be found [here.](https://docs.python.org/3/library/configparser.html)

## Credits/Mentions of the additional APIs and libraries used with the demonstration:

1. [cataas.com](https://cataas.com/)
2. [catfact.ninja](https://catfact.ninja/)
3. [youtube-data-api](https://pypi.org/project/youtube-data-api/)
4. [youtube-dl](https://youtube-dl.org/)
5. [aiohttp](https://pypi.org/project/aiohttp/3.6.2/)
6. [aiofiles](https://pypi.org/project/aiofiles/)

