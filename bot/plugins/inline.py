from pyrogram import types, filters
from bot import bot


@bot.on_inline_query()
async def inline_func(client, query):
    string = query.query.lower()
    answers = []
    if string == '':
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text='Need help? Click here',
            switch_pm_parameter='help_inline',
        )
        return
    if string.split()[0] == 'related':
        if len(string.split()) == 1:
            await client.answer_inline_query(
                query.id,
                results=answers,
                switch_pm_text='Input Song ID',
                switch_pm_parameter='help_inline',
            )
            return
        try:
            track_id = int(string.split(None, 1)[1])
        except ValueError:
            return
        for x in (await bot.related(track_id)):
            try:
                result = (
                    x['images']['coverarthq'],
                    x['images']['coverart'],
                    x['title'], x['subtitle'],
                    x['share']['href'],
                    x['share']['html']
                )
            except KeyError:
                result = (
                    None,
                    None,
                    x['title'],
                    x['subtitle'],
                    x['share']['href'],
                    x['share']['html']
                )
            image, thumb, title, artist, link, share = result
            answers.append(
                types.InlineQueryResultArticle(
                    title=title,
                    description=artist,
                    thumb_url=thumb,
                    input_message_content=types.InputTextMessageContent(
                        f'**Title**: {title}\n**Artist**: {artist}[\u200c\u200c\u200e]({image})'
                    ),
                    reply_markup=types.InlineKeyboardMarkup(
                        [
                            [
                                types.InlineKeyboardButton(
                                    '🔗 Share',
                                    url=f'{share}'
                                )
                            ],
                            [
                                types.InlineKeyboardButton(
                                    '🎵 Listen',
                                    url=f'{link}'
                                )
                            ]
                        ]
                    )
                )
            )
    await client.answer_inline_query(
        query.id,
        results=answers,
        cache_time=0,
    )
