import telebot
from telebot.exceptions import ApiTelegramException
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


def is_admin(chat_id: int, user_id: int) -> bool:
    """Checks whether a given user has administrator or creator privileges in the chat."""
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ['administrator', 'creator']
    except ApiTelegramException:
        return False


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Sends welcome message and bot commands description."""
    welcome_text = (
        "Welcome! I am a Chat Moderation Bot.\n\n"
        "Commands:\n"
        "/ban - Ban a user (must be used as a reply to the target user's message)."
    )
    bot.reply_to(message, welcome_text)


@bot.message_handler(commands=['ban'])
def ban_user(message):
    """Bans a targeted chat member if the command issuer has admin privileges."""
    chat_id = message.chat.id
    issuer_id = message.from_user.id

    # Verify command is used in reply to a message
    if not message.reply_to_message:
        bot.reply_to(message, "This command must be used as a reply to the user you want to ban.")
        return

    # Check if the person issuing the command is an admin
    if not is_admin(chat_id, issuer_id):
        bot.reply_to(message, "Permission denied. Only chat administrators can use this command.")
        return

    target_user = message.reply_to_message.from_user
    target_id = target_user.id
    target_name = target_user.username if target_user.username else target_user.first_name

    # Prevent banning admins or creators
    if is_admin(chat_id, target_id):
        bot.reply_to(message, "Cannot ban a chat administrator or owner.")
        return

    try:
        bot.ban_chat_member(chat_id, target_id)
        bot.reply_to(message, f"User @{target_name} has been successfully banned.")
    except ApiTelegramException as e:
        bot.reply_to(message, f"Failed to ban user. Ensure I have admin permissions. Error: {e.description}")


if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)
