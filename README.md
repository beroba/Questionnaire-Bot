# Questionnaire-Bot
Discordでアンケートを取るBot

## インストール

1. Clone

    `git clone git@github.com:beroba/Questionnaire-Bot.git`

2. Install

    `pipenv install`

3. .env編集

    `cat .env.sample > .env`

    `{TextEditor} .env`

4. start

    `pipenv run start`

|環境変数名|説明|
|:------:|:-----:|
|DISCORD_TOKEN|Discordのトークン|
|COMMAND_PREFIX|Botの呼び出しを変える際に使用|
|RUN_MODE|DEVと入力しておくと開発モードになります|
|DB_NAME|DBのファイル名を指定します|
