
__INSTRUCTION TO RUN ON WINDOWS FOR TESTING__

1) Windows DOES NOT have python installed by default. Visit Python's website to download it. You are going to want the exe for installation
	rather that getting it from windows store for a good reason. 

2) Once you have downloaded the python exe run it and BE SURE TO " ADD PYTHON TO PATH ". This is a selection during the install process. 
	You also want to select the ".py extension" option. Installing python & pycharm (the IDE) you want to always " ADD TO PATH ". 
	If you forget or skip the step by chance you will have to uninstall the software and reinstall it with the correct config. 
	Trust me you don't want to manually " ADD TO PATH ". You can also "disable the path length limit" if you want. It does exactly
	what it sounds like it does. 

3) Now head over to jetbrains.com to install pycharm-community. It is a super bad-ass python IDE. The best imo. You can just type pycharm in a 
	browser and it should take you right to the website. Be sure it's jetbrains. We don't want any infected IDEs lol. Be sure to pay
	attention to the installation process.

4) Now that you have the inturpreter and the IDE downloaded. It's time to instally dependencies or "packages". Head over to your command
	prompt and run as admin. You will use the "pip" tool to install all of the packages. If we have any trouble the rest can be taken care
	of in the IDE. (what makes pycharm so damn cool). 
	
	RUN THESE COMMANDS. 
	
	pip help				# read over the commands real fast
	pip freeze				# lists packages in a certian order (use can use "pip list" as well)
	pip install tkinter			# installs the GUI package (if the does not work run these)
						pip install tk | pip install tkinter as tk			
	pip install pillow			# this is the dumb package that keeps my program from compiling correctly I plan to get rid of it
	pip freeze 				# again to check the packags are there

5) Now you can go to where the sec program is and right click and you should see an option to open with pycharm if you installed everything
	correctly. Go ahead and open that up. 

6) On the left you will see the files "main.py" and a couple others. Double click "main.py". Generically all programs main code is in a "main"
	file. You should see the code there. 

7) Here is where a couple of thigs can start to go wrong but they are easy fixes if you know what to do. 

	1) check the import statements at the top of the code. All import statemets are is "importing" the extra packages or libraries are what 
		they are actually called, to allow extra functionallity per-say. If there are any errors they will be there. The PIL 
		import statement may be underlined red. This means basically its being dumb. So Hover over the underlined word and there is
		an option somewhere in there to "install pillow" or something sililar. I can't re-create this at the moment.. That should fix 
		that issuse. 
	2) Another issue you may run into is not having an "inturpretuer" configured. (yea I cant spell)
		go ahead and select the configure inturpreter option. It should be pretty simple.

8) with all of that done you should not have any more issues. Now you should see the greeb "play" button at the top right. If not
	right click on "main.py" on the left side and select the "run" option. 

9) you should be good to go now. Test this out. you can write down any issues you see or if you want you can even go to the database page and 
	correct the errors in the correct python array. Either way is fine but please at least not the errors in a text file or something. 

10) Be sure to read the instructions on how the game works. Everything should NOT be case sensitive and there should be no hyphens required
	for the anwser. I try to remove them all together because it is just faster that way. I know for a fact there are going to be errors
	in the grammer but this should help learn a little, I will be breaking it up into two programs because there is a 1 in 355 chance to 
	get any given term and that could take a long time to iterate through them to see every term like is expected. I may just go through 
	and remove all the terms you should already know by the time you get to sec plus. Not sure so please leave feedback. 
  
