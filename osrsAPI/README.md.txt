This project is using a osrs_highscores module that cleans up the terrible API created by Runescape which only exports the number values of items without giving them any other values.

For example, using the normal API if I were to call a hiscores name to retrieve the values I would receive this as the response:

b'170771,1875,83546285\n1279963,60,284510\n601573,75,1232284\n318666,95,9457293\n375683,93,7485878\n234455,97,11348210\n208902,77,1502443\n179140,96,10398752\n225448,90,5384550\n352630,76,1448723\n309851,81,2259323\n425742,74,1113984
\n246973,85,3276117\n210757,77,1526177\n107473,84,2970314\n37343,93,7725570\n189480,78,1672122\n207331,75,1274105\n224014,73,1044925\n247927,85,3505496\n147816,87,4087433\n179689,66,537354\n202737,75,1242166\n104852,83,2768556
\n-1,-1\n-1,-1\n-1,-1\n358617,40\n-1,-1\n689419,2\n256370,16\n283977,21\n339937,1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n11437,107\n-1,-1\n45288,92\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1
\n-1,-1\n116095,60\n-1,-1\n-1,-1\n61197,30\n-1,-1\n101484,144\n-1,-1\n42303,60\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n-1,-1\n121406,130\n154730,189\n22478,161\n-1,-1\n'

While it is possible to use this, each set of 3 values is corresponding to 1 skill, it would be easier to use an module which already converts the information into variables we can use.


To use this python script install the module

pip install osrs_highscores

To make sure the script properly works, make sure to change the line at the end which is outputting the file, to a directory on your machine that is valid. The current one on this project is C:\IT3038C\osrsAPI\input.csv.


You can either run the script by opening the file with python installed, or running the script in your IDE.

After it is run it will prompt you for an account name to use. Currently there are 4 types of acccounts one can have, a Default, Ironman, Hardcore Ironman, Ultimate Ironman.
As there are different hiscores for each type of account you can filter them out this way to get further filters by type. 

These hiscore pages are heavily used, and so the default accounts occasionally do not get grabbed and will recieve an error of "Unable to pull data from hiscores". 

For the purposes of this lab I have chosen to use an Ironman account specifically as they will generally have less traffic and will almost always generate the data needed. 
All Ironman account names can be found here on these hiscores: 

https://secure.runescape.com/m=hiscore_oldschool_ironman/overall


We can then verify our data in the CSV with the hiscores directly.


Finish Pre-reqs before continuing

1. Run the script
2. Enter any name of a Ironman account from the hiscores
3. Script will run and pull all of the skills and their levels for the account
4. Script pulls the data to a dataframe
5. Dataframe is exported to CSV
6. Confirm data in CSV.


