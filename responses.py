def get_response(message: str) -> str:
  p_message = message.lower()

  if p_message == 'hi' or p_message == 'hello':
    return 'Hey '
  elif p_message == "good morning" or p_message == 'goodmorning':
    return "Good Morning!"
  elif p_message == "good afternoon" or p_message == 'goodafternoon':
    return "Good Afternoon!"
  elif p_message == "good night" or p_message == 'goodnight':
    return "Good Night!"
  elif p_message == "!help":
    return '`To recieve a Hello, please type hi or hello. To recieve a good morning, good afternoon, or goodnight, please type those respectively first. `'
  elif p_message == "86 is peak":
    return "Facts"
  elif p_message == "henry":
    return "Henry is my master."
  elif p_message == "oyasumi":
    return "Oyasami, Len-kun (Ɔ ˘⌣˘ C)"

  elif p_message == "shinitakunai":
    return "DON'T YOU GET IT, IT CALLS, IT CALLS"
  elif p_message == "wasurenai":
    return "They told me not to forget."
  elif p_message == "nya":
    return "~ichi nii san, Nya arigato~"

  elif p_message == "babe":
    return "mwah"

  elif p_message == "kys" or p_message == "kill yourself":
    return "Chillat Jess"
  