# import Constants as keys
# from telegram.ext import *
# import Responses as R

# print("Bot started...")


# def start_command(update, context):
#     update.message.reply_text('Goodday, How do you do? I can help you create and manage Telegram bots. If you are new to the Bot API, please see the manual. You can control me by sending these commands:/newbot - create a new bot /mybots - edit your bots [beta]')
#     update.message.reply_text('Goodday, How do you do? I can help you create and manage Telegram bots. If you are new to the Bot API, please see the manual. You can control me by sending these commands:/newbot - create a new bot /mybots - edit your bots [beta]')



# def help_command(update, context):
#     update.message.reply_text('If you need help, See here')


# def handle_message(update, context):
#     text = str(update.message.text).lower()
#     response = R.decabot_responses(text)

#     update.message.reply_text(response)


# def error(update, context):
#     print(f"Update {update} caused error {context.error}")


# def main():
#     updater = Updater(keys.API_KEY, use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start_command))
#     dp.add_handler(CommandHandler("help", help_command))

#     dp.add_handler(MessageHandler(Filters.text, handle_message))

#     dp.add_error_handler(error)

#     updater.start_polling()
#     updater.idle()


# main()