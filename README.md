
# telegram-chooser-bot

Indecisive? Never again, with the help of this bot.



## Demo

![](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW00ZDEwNTV6Nnd1dnhkZnNubW8xdjJ4NW9hcnllb3MxdHppd2QxNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bv9Mig4A88yoZfXHLH/giphy.gif)
## Features

- /winner option1 option2 option3 option4 etc
    - /winner beach museum arcade chill
    - /winner xiao_long_bao fish_n_chips big_mac

## Installation

Clone this repo, and just use 
```
    docker compose up --build. 
```
Remember to set a .env file:
    



    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

    `TOKEN=#Telegram authtoken`

    `WEBHOOK_HOST=ngrok tunnel port`

    `WEBHOOK_PORT=local port for webhook`

    `NGROK_AUTHTOKEN=ngrok_authtoken`
## Tech Stack

**Client:** PyTelegramBotApi

**Server:** Flask, FastAPI, xvfb-run, ffmpeg, Ubuntu-22.04


## Authors

- [@jensenhuangyankai](https://www.github.com/jensenhuangyankai)


## License

[MIT](https://choosealicense.com/licenses/mit/)

