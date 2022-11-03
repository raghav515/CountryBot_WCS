# WEC GDSC RECS 2022

### Task Country Bot:

- Telegram is one of the most popular real-time messaging platform with robust support for programmable bots.Bots are ubiquitous on Telegram and provide a wide range of services, including moderation assistance, games, music, internet searches, payment processing, and more.

- In this task, you are expected to create a interactive Telegram bot that displays interesting facts and information about a particular country. Users should be able to find the capital, currency, languages spoken, flag etc. Any additional features are appreciated and graded accordingly.You can use any freely available APIs to fetch information about a country. (Recommended:  [https://restcountries.com/](https://restcountries.com/))

## Solution
### Bot Details:
- Name: Factbot
- UserName: @wecfc_bot
### Configuring the bot
-  @BotFather a telegram bot helps in making a bot. Once a chat is started, it will show multiple commands to use. 
- Use the command /newbot to create a new bot. Next, it will ask details like Username and Bot Name. 
- After the process, a HTTP API Token will be generate. Save this Token as it will be necessary in the code.
### Running the Python File
- Install all the required Dependencies.
`python3 pip install -r requirements.txt`
- Run the python file using the following command.
`python3 main.py`
- This will make the bot functional. Once the code stops running, the bot also stops functioning. 
### Hosting the code on Digital Ocean
- Create a Droplet with sufficient resources to handle the program. 
- Open the console for this Droplet.
- Add all the necessary files in the Droplet. Here, I had my code pushed on GitHub. I cloned it in the Droplet.
- Go to the file and follow the steps mentioned under Running the Python File segment.
- If the code and bot is working properly, stop the code execution.
- Now, even if the code is not stopped, but if the console is closed, the bot will stop functioning.
- To stop this from happening, first navigate to the file location and make the python file an executable.
`chmod +x main.py`
- Now, execute the following commands:
`nohup /path/to/main.py &`
`nohup python /path/to/main.py &`
`Path > main.py /> output.log > python /path/to/main.py > output.log > etc`
- Now executing the python file.
`python3 main.py bygrep`
- Check whether the bot is online. 
#### To Stop the script
`pkill -f main.py`