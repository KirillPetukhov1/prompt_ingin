from decouple import config
from pathlib import Path
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

ca = Path(__file__).parent.parent / 'resources' / 'russian_trusted_root_ca.cer'

with GigaChat(
    credentials=config('AUTH_KEY'),
    ca_bundle_file=str(ca),
    model='Gigachat-2-Pro',
    scope='GIGACHAT_API_B2B'
) as giga:
    payload = Chat(
        messages=[
            Messages(
                role=MessagesRole.SYSTEM,
                content='Ты -- помощник, который объясняет сложные вещи простыми словами.'
            ),
            Messages(
                role=MessagesRole.USER,
                content='Объясни, что такое искусственный интеллект.'
            ),
        ]
    )
    response = giga.chat(payload)
    print(response.choices[0].message.content)