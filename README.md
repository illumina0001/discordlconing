# Discord Cloning

## Clone messages from one server to another with discord.py-self & webhooks

a service i've provided with tuxer services for ~2 years, finally open source

## Background

This script will only run as long as your computer is on. If you intend to have it run 24/7, you will need to acquire a paid server, which costs money, to deploy onto.

You will need an account that's a **member** in the server you desire to clone, alongside being in & having a role with the **manage channels** permission within the server you want to clone TO.  
Ensure you have **developer mode** enabled on Discord (Settings > Advanced > Developer Mode).

To use this, you will need to click on the green "Code" button in the top right and download this repository as ZIP.  
**Extract the folder once downloaded.**

You will need the latest release of [python](https://www.python.org/downloads/) if you don't have it already.

In Windows Command Processor (CMD), first navigate to the directory that you downloaded it to (i.e., `"C:\Users\John\Downloads\discordcloning\"`) with:

```

cd (directory)

```

Then, run the code:

```

pip install -r requirements.txt

```

Keep this window open. You'll use it later.

## Basic Setup

### 1. Get necessary values

**User Token**

a. Go to discord.com/app while logged into the account you will use.  

b. Open your browser's DevTools (**F12** or **Ctrl+Shift+C**)  

c. Navigate to **"Console"** at the top bar if not already on it  

d. Paste and run the below code.

```

(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()

```

(Depending on your browser, pasting may be blocked at first. Type **"allow pasting"** and enter if this happens.)  

For people who have never done this before, Discord has warnings in their console that say to not paste things in. This is for a good reason. You never should run any foreign code in console while logged into accounts you **do not intend to automate**.  

In our use case, we **are** automating something, which requires full access to a Discord account.  

e. Copy the value that is returned. This will be the account token we use.



**Receiver & Source Guild ID**

a. For those who didn't heed my warning about developer mode before, do it now.  

b. Right-click on the icon for the server you want to clone. Click on **"Copy Server ID"** at the bottom.  
   This will be the **source guild ID**, or the ID of the server that the messages will be retrieved **FROM**.  

c. Do the same for the server you want to use for receiving cloned messages. This will be the **receiver guild ID**, or the ID of the server that messages will be forwarded **TO**.  

### 2. Setup

a. Open the file **"setup.py"** in a text editor, i.e. Notepad.  

b. Paste in the values you acquired in step 1 into the variables at the top.  

c. In the Windows Command Processor window you used to install the requirements, run this command:

```

python setup.py

```

d. This will set up the cloning and generate a **webhooks.txt** file. Open this file in Notepad and copy the contents.

---

### 3. Deployment

a. Open the other file, **"main.py"**, in a text editor.  

b. Within the **"channels"** table, paste in the contents of the **webhooks.txt**.  

c. **IMPORTANT**: Make sure your pasted content is indented correctly. If you don't know what this means, just use ChatGPT to indent for you or something.  

d. Set the value of the **"token"** variable to the same account token as before.  

e. In your command processor, now run the command:

!!!

python main.py

!!!

Enjoy!

## made by vor 3/12/2025
