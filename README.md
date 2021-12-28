# Mario Kart Wii Character/Vehicle Randomizer

## About
##### Hello! This is a character/vehicle combination randomizer made by Andrew Myers.
##### The goal of this project was to randomize combinations for my friends and I in one line of code!
##### Hope you enjoy using it!

## Tutorial

### Quick Setup

1. Click the green *Code* button above
2. Click download zip
  * Save the zip file in a place you will remember
  * Open the zip file by double-clicking on it
3. Open up the command line
  * On Mac, hit Command+Space and search for Terminal
  * On Windows, hit Windows+R, type cmd and hit Enter
4. Locate the directory where you saved the zip file
  * In the command line, type ``` cd path_to_folder ```
  * Let's say I saved the zip file in my Documents folder. The folder after I double-clicked on the zip file should be called 'mario_kart_randomizer-main'
  * My command would look like: ``` cd Documents/mario_kart_randomizer-main ```
5. You're all set up! You should now be able to run the below commands on your command line
To use the randomizer, you can clone or download this repo. You'll be executing the bash script on the command line to run it.
```
./kart
```
Run the bash script with no arguments to see a sample run of the randomizer!
```
./kart --help
```
The above command will give you lots of information on the different flags you can define. I will also outline them below.

## Flags

### -c
This flag allows you to tell the randomizer what weight class of characters you want to include.\
Mario Kart Wii has **light**, **middle**, and **heavy** weight characters. Here's an example:
```
./kart -c light
```
Will only choose your characters from the light weights.\
If this flag is omitted, the randomizer will select from all available characters.
### -v
This flag allows you to tell the randomizer what type of vehicles you want to include.\
Mario Kart Wii has both **bikes** and **karts**. Here's an example of using the v flag:
```
./kart -v bikes
```
Will only choose a bike for your character.\
If this flag is omitted, the randomizer will select from all available vehicles.

### -n
This flag allows you to tell the randomizer how many players you want to randomize for.\
You **must** give it an integer, and this number **must match the number of player names you give the randomizer**.\
Example:
```
./kart -n 4
```
Will run the randomizer for 4 players.\
If this flag is omitted, the randomizer will run for 1 player.

### -p
This flag allows you to specify the names of the different players you are randomizing for.\
In your command, specify the names of the players separated by a space. Here's an example:
```
./kart -n 3 -p 'Andrew Patrick Joey'
```
Will run the randomizer 3 times, once for Andrew, once for Patrick, and once for Joey.\
If this flag is omitted, the randomizer will run depending on the number of players specified with the -n flag, and each player will be named: *Doug Dimmaclone*.

### -f
If you're pressed for time and just want the summary, you can specify this flag.\
Here's an example:
```
./kart -f
```
Will omit most of the output.\
If this flag is omitted, the randomizer will print verbose output to the screen.
## A Few Examples

Let's say I want to randomize for 4 people. I want us all to be on bikes, but I don't care about the weight class. I'm not in a rush, so I'll let the randomizer print its full output. I would use this command:
```
./kart -v bikes -n 4 -p 'Andrew Patrick Joey Kyle'
```
The output would look like:

![A screenshot with full output.](/images/sample_1.png "This is a sample image.")

Let's say I'm in a hurry. I'm randomizing for 2 people, I want all available characters and karts, and I don't want all the fancy schmancy ouput. I would use this command:

```
./kart -n 2 -p 'Andrew Patrick' -f
```

The output would look like:

![A screenshot with fast mode output.](/images/sample_2.png "This is a sample image.")

## Final Notes
That's about it from me! If you see any bugs, feel free to throw it in the Issues tab on Github. Happy randomizing!
