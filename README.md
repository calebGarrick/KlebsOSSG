# KlebsOSSG

A repository to track my progress working on my open smart glasses

## Progress Notes

### 5/12/23

I just received my tinyPico, I will begin by just getting used to the development environment of coding off of it.

Bashed my head into a wall flashing the micropython, I just didn't read how to put it in boot mode like a buffoon. Now following the [micropython tutorial](https://youtu.be/5W3WvXAmDJc?list=PL6F17pWypPy_KSmpnR5CV8x78QhAiKBIl), installing dependencies and all that bs.

Starting to get the hang of the Pin interface, back in the swing of writing python. Going to invest in the capture card so I can tinker with display code before I get the actual display.

My plan for the weekend is to figure out bluetooth and loading pdfs and breaking them up if they are too large. Not sure if it's worth, buy I may upgrade to the [pro or feather s3](https://esp32s3.com/) for the extra memory.

### 5/13/23

I'm starting off by installing the [smart glasses manager app](https://github.com/TeamOpenSmartGlasses/SmartGlassesManager) on an old pixel 3. Took me too long to realize I needed to load the app in via [android studio](https://developer.android.com/studio), and once I reached out in the [OSSG discord](https://discord.gg/5ukNvkEAqT) it was pointed out I needed my phone in developer mode and with USB Debugging on. Huge thanks to [Alex](https://github.com/alex1115alex)!

Another bit of a gut-punch was that the microcontroller I got(TinyS3) was incompatible with the display I got as it lacks a DAC(digital audio converter). For anyone following please ensure your board of choice can output composite video or has an onboard dac.

Now that SGM is on my phone, I can flash the OSSG firmware to my s3 and play with the comms side of things.
