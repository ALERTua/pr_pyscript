from pprint import pformat

DEFAULT_PLAYER_IDS = [
    "media_player.office_speaker",
    "media_player.kitchen_speaker",
    "media_player.bedroom_speaker",
    "media_player.living_room_speaker",
]

@service("pyscript.tts")
def speak(message=None, player_ids=DEFAULT_PLAYER_IDS, language='en', **kwargs):
    """yaml
name: Pyscript TTS
description: Pyscript TTS Service
fields:
  message:
    name: message
    description: message
    example: message
    default: test message
    required: true
    selector:
      text:
  player_ids:
    name: player_ids
    description: player ids
    example: media_player.office_speaker
    required: true
    default: [media_player.office_speaker]
    selector:
      entity:
        multiple: true
        domain: media_player
  language:
    name: language
    description: language
    example: en
    default: en
    required: false
    selector:
      text:
"""
    if not message:
        log.warning(f"{__name__}: No message to say")
        return

    cache = kwargs.get('cache', True)  # note that a service can accept optional arguments

    log.info(f"""{__name__}
    message: {message}
    player_ids: {player_ids}
    language: {language}
    kwargs:
    {pformat(kwargs)}
    """)
    if state.get('binary_sensor.internet') == 'on':
        tts.speak(
            message=message,
            media_player_entity_id=player_ids,
            entity_id='tts.google_translate_say',
            language=language,
            cache=cache,
        )
    else:
        tts.speak(
            message=message,
            media_player_entity_id=player_ids,
            entity_id='tts.piper',
            cache=cache,
        )
