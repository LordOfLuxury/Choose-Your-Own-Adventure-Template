# Modules
from UserChoice import user_choice
import First_First
import First_Second

def branch():
	print("You come across a large door.")
	user_choice({
		"Open the door": ["open", First_First.branch],
		"Do a barrel roll": ["roll", First_Second.branch]
	})

if __name__ == "__main__":
	branch() # The ONLY one of these to call immediately.