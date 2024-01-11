import requests

api_key = ""


def main():
    voice_id = get_voice_selection()
    text = get_text()
    model = get_model_selection()
    response = send_api_request(voice_id, text, model, api_key)
    write_audio_file(response)


def send_api_request(voice_id, text, model, api_key):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key,
    }
    data = {
        "text": text,
        "model_id": model,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
    }
    response = requests.post(url, json=data, headers=headers)
    return response


def write_audio_file(response):
    with open("output.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def get_voice_selection():
    print(
        """
Enter a number to select a voice:
1. Rachel
2. Drew
3. Clyde
    """
    )
    selection = input("")
    match selection:
        case "1":
            return "21m00Tcm4TlvDq8ikWAM"
        case "2":
            return "29vD33N1CtxCmqQRPOHJ"
        case "3":
            return "2EiwWnXFnvU5JabPnv8n"
        case _:
            return "21m00Tcm4TlvDq8ikWAM"


def get_text():
    text = input("Enter text: ")
    return text


def get_model_selection():
    print(
        """
Enter number to select model:
1. Eleven Multilingual v2
2. Eleven Multilingual v1
3. Eleven English v1
4. Eleven Turbo v2
5. Eleven English v2
"""
    )
    selection = input("")
    match selection:
        case "1":
            return "eleven_multilingual_v2"
        case "2":
            return "eleven_multilingual_v1"
        case "3":
            return "eleven_monolingual_v1"
        case "4":
            return "eleven_turbo_v2"
        case "5":
            return "eleven_english_sts_v2"
        case _:
            return "eleven_multilingual_v1"


if __name__ == "__main__":
    main()
