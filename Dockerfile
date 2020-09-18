FROM olegpolisan/tg_userbot
ENV PATH="/app/bin:$PATH"
WORKDIR /app
RUN git clone https://github.com/PolisanTheEasyNick/Telegram-UserBot.git -b master /app
#
# Copies session and config(if it exists)
#
COPY ./userbot.session ./google.json* ./config.env* ./client_secrets.json* ./secret.json* /app/
#
# Finalization
#
CMD ["init/start.py"]
