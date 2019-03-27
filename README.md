# Scripts

- checkpass.py is a simple python script can be used for checking whether a password has been leaked or not by looking up haveibeenpwned API. It just sends the prefix of SHA1'd password and looks for if there is a match in response. 

**Note: It's just an implementation which is mentioned in a Computerphile [video.](https://www.youtube.com/watch?v=hhUb5iknVJs) I do not recommend running it on the console to check the actual passwords because your password will remain in the command line history. It can be used by importing in another program or reading passwords from a file.**
