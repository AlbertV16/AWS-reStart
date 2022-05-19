How to download WSL on NOT the root drive or mount the home folder to a seperate drive (ie not the root drive)

The web page is a step by step process on how to move wsl from the c drive to another drive
https://avinal.space/posts/development/wsl1.html

Note: all reference to Ubuntu should be changed to Ubuntu<version>
    In my case, it was Ubuntu20.04

Following the steps, I exported Ubuntu to the directory I want it installed

On step 6, Windows powershell is returning "Access is denied"
    Trying to unzip the file using the GUI
    Error involved this command
        wsl --import Ubuntu "Z:\wsl2" "Z:\export\ubuntu-ex.tar"
        I was typing 'wsl --import Ubuntu "Z:\wsl2" "Z:\export\wsl2"'
    
    As a result the system did not understand how to import a folder into another folder
    Need to ensure the zipped file is being imported

Could not change default user-name from root
