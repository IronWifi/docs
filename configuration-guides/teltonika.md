## Step 1: ironwifi.com configuration

### Login screen

We need to login into **console.ironwifi.com/login** system using our credentials. If you don't have a registered account then you need to create one. You can do that by clicking **Create Account**. 

![firstScreen](teltonika/teltonika1.png)

### Create new network

In the opened browser window click **Networks**

![firstScreen](teltonika/teltonika2.png)

Click **New Network**

![firstScreen](teltonika/teltonika3.png)

Type **name** of new network and select **region**

Click **Create network** 

![firstScreen](teltonika/teltonika4.png)

Click on your **created network** 

![firstScreen](teltonika/teltonika5.png)

**Network details**

Here are the data that we will need in the next step:

**Radius ip Address** : 130.211.107.8

**Authentication Port** : 6375

**Accounting Port**  : 6376

**Shared Secret**  : goDkt2Abuv74PQ0 

![firstScreen](teltonika/teltonika6.png)

**Create new user**

Click **Users** 

![firstScreen](teltonika/teltonika7.png)

Click **New User** 

![firstScreen](teltonika/teltonika8.png)

Type **Username** and click **Create User**

![firstScreen](teltonika/teltonika9.png)

Click on your user 

![firstScreen](teltonika/teltonika10.png)

Set new password and click **ENTER**

![firstScreen](teltonika/teltonika11.png)

## Step 2: Router configuration

Now we need to open our RUT homepage. You can access the website by entering 192.168.1.1 in your internet browser's URL bar.

Open the hotspot configuration panel by clicking **Services → Hotspot** 

![firstScreen](teltonika/teltonika12.png)

Click **Edit**

![firstScreen](teltonika/teltonika13.png)

Use configuration details from **Step 1**.

Check **enable** and **Terms of service** box

Select **External radius** from **Authentication mode** dropbox

Type configuration details **RADIUS Server, Authentication port, Accounting port** and **Radius secret key**

![SecondScreen](teltonika/teltonika14.png)

Click **save**

Wait up to **5** minutes from the time you saved the changes.

## Test your hotspot

Try connecting to your router using computer or mobile phone.

Select your router

![firstScreen](teltonika/teltonika15.png)

Type your username and password.

Click **Login** 

![firstScreen](teltonika/teltonika16.png)

You should see a message **Authorization Successful**

![firstScreen](teltonika/teltonika17.png)
