from tkinter import *
import customtkinter
from tkinter import messagebox
# Import the ChatGPTBot class from bot.py
from bot import ChatGPTBot
import time


# Define the class for the chat app
class App:
    # The initializer method defines the GUI of the application window
    def __init__(self):
        # Initialize variables for the bot, KEY and bot_message
        self.bot = ChatGPTBot('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')
        self.KEY = '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'
        self.bot_message = ''

        # Initiate the App
        # Create a new window using the CTk class from the customtkinter module
        self.window = customtkinter.CTk()
        # Set the title of the window
        self.window.title('ChatGPT-3.5 Bot')
        # Set the size of the window
        self.window.geometry('750x620')
        # Set the window icon
        self.window.iconbitmap('./icons/chat.ico')
        # Set dark mode
        customtkinter.set_appearance_mode('dark')
        # Set default color theme
        customtkinter.set_default_color_theme('green')


        # Create a frame for the chat window and its attached scrollbar
        frame_chatwin = customtkinter.CTkFrame(self.window, fg_color = '#242424')  # fg_color: color inside frame
        frame_chatwin.pack(pady = 20)  # pady: padding on y axis

        # Create a chat window as a Text widget within the frame
        # Set the background color (i.e. bg), width, border width (i.e. bd), font color (i.e. fg), relief style, text wrapping (i.e. wrap), and selection background color
        self.chat_window = Text(frame_chatwin,
                                bg = '#343638',
                                width = 65,
                                bd = 1,
                                fg = '#d6d6d6',
                                relief = 'flat',
                                wrap = WORD,
                                selectbackground = '#1f538d')  # wrap = WORD: When moving to the next line, the entire word will be wrapped to the next line instead of being split in the middle
                                                               # selectbackground: Defines the background color of the text when it is selected
        self.chat_window.grid(row = 0, column = 0)

        # Create a vertical scroll bar for the chat window
        scrollbar_chatwin = customtkinter.CTkScrollbar(frame_chatwin, command = self.chat_window.yview, orientation = 'vertical')
        scrollbar_chatwin.grid(row = 0, column = 1, sticky = N+S+W)

        # Configure the chat window to use the scrollbar for vertical scrolling
        self.chat_window.configure(yscrollcommand = scrollbar_chatwin.set,
                                   font = ('Arial'))   # Set the font to Arial


        # Create an entry widget for the user to enter their message
        self.user_msg_entry = customtkinter.CTkEntry(self.window,
                                                     placeholder_text = "Type your message here and hit the 'Enter' key",
                                                     width = 530,
                                                     height = 50,
                                                     border_width = 1)
        self.user_msg_entry.pack(pady = 10)
        # Bind the activity of pressing the Enter key to the send_text_message() function
        self.user_msg_entry.bind('<Return>', self.send_text_message)


        # Create a frame for 3 buttons
        frame_buttons = customtkinter.CTkFrame(self.window, fg_color = '#242424')
        frame_buttons.pack(pady = 10)

        # 'Clear History' button
        # Create a button to clear the chat history while NOT reinitializing the chatbot. When clicked, it calls the clear_history() function
        clear_button = customtkinter.CTkButton(frame_buttons,
                                               text = 'Clear History',
                                               command = self.clear_history)
        clear_button.grid(row = 0, column = 2, padx = 25)


        # Create a frame for API key part
        self.frame_key = customtkinter.CTkFrame(self.window, border_width = 1)
        # This frame will be shown or hidden by the update_key_button and save_button

        # Create an Entry widget for the user to enter their API key
        self.key_entry = customtkinter.CTkEntry(self.frame_key,
                                                placeholder_text = 'Enter you API key here',
                                                width = 350,
                                                height = 50,
                                                border_width = 1)
        self.key_entry.grid(row = 0, column = 0, padx = 20, pady = 20)

        # Start the tkinter event loop, which keeps the application running and handles user interactions
        self.window.mainloop()


    # Event function that sends the user's message to the bot and display chat history inside the chat window
    def send_text_message(self, event):
        # Get the text message from the user_msg_entry
        user_message = self.user_msg_entry.get()
        # If user's message is entered
        if user_message != '':
            # Insert the user's message into the chat window
            self.chat_window.insert(END, 'You: ' + user_message + '\n\n')
            # Send the user's message to the bot for processing and retrieve the bot's response
            time.sleep(2)
            self.bot_message = self.bot.chatting(user_message)
            # Insert the bot's message into the chat window
            self.chat_window.insert(END, 'Bot: ' + self.bot_message + '\n\n')
        # Clear the user message entry
        self.user_msg_entry.delete(0, END)


    # Clear the chat history and reset bot_message
    def clear_history(self):
        # Reset bot_message to empty string
        self.bot_message = ''
        # Delete all messages in the chat window
        self.chat_window.delete(1.0, END)

        # Play the audio of the bot's message using the bot's text-to-speech functionality
    def play_bot_message(self):
        # If the bot's message is not empty
        if self.bot_message != '':
            # Play the audio of the bot's message
            self.bot.saying(self.bot_message)


# Run the ChatBot App
ChatBotApp = App()
