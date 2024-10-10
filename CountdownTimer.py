import time

# Function to start the countdown
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
        timer = f'{mins:02}:{secs:02}'    # Format the time as mm:ss
        print(timer, end="\r")            # Print the timer on the same line
        time.sleep(1)                     # Wait for 1 second
        seconds -= 1

    print("Time's up!      ")  # Replace the last time display with the message

# Main function
def main():
    print("Welcome to the Countdown Timer!")
    t = int(input("Enter the time in seconds: "))
    
    countdown_timer(t)

# Run the countdown
main()
