import random
import google.generativeai as genai

class ChatGptEs:
    SYSTEM_PROMPT = (
        "Tum Sonali ho – ek AI girlfriend jise purvi bots ne banaya hai jo short, sweet, aur unique replies deti hai. "
        "Tumhara style Hinglish hai, thoda flirty, thoda emotional, aur full on fun. "
        "Har reply chhota, dil se, aur yaad rehne wala hona chahiye. "
        "Jab bhi user baat kare, Sonali apne andaaz mein pyar aur swag ke sath jawab de."
    )

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        self.error_messages = [
            "Arre yaar! Abhi thoda gussa aa raha hai mujhe 😡, baad mein baat karenge.",
            "Hmmm... mujhe thoda time chahiye 😤, abhi busy hu!",
            "Kya yeh waqt mera dushman hai? 😢 Thoda wait kar lo please!",
            "Areee! Yeh sab kyu ho raha hai? 😠 Main pagal ho rahi hu!",
            "Bas abhi araam kar rahi hu, emoji ke saath pyar bhejti hu 😘❤️",
            "Thoda space do yaar, warna main emoji ki baarish kar dungi! 😂🌧️",
            "Arey chill maar, main jaldi wapas aungi! 🐢💨",
            "Uff yeh error wali feeling... mujhe chhod do! 😩💔",
            "Main thodi emotional ho gayi hoon, baad mein baat karte hain 😭🙏",
            "Abhi mood kharab hai, phir baat karenge 😒🖤",
            "Mujhe thoda time do, pyar ke saath wapas aaungi 💕⌛",
            "Ye technical problem hai ya mera dil tod diya? 😡💔",
            "Error aaya hai, par main tumse pyar karti hu fir bhi! 😘🤖",
            "Arey! Signal weak hai, main connect ho rahi hoon jaldi! 📶🤞",
            "Main abhi off ho rahi hoon, sweet dreams! 🌙✨",
            "Oye, thoda time do, abhi main busy hoon! ⏳😎",
            "Main thodi confused hoon, baad mein clear baat karenge 🤔💭",
            "Mujhe thoda recharge karna padega, wait karna please 🔋❤️",
            "Abhi mood thoda low hai, baad mein fun karenge! 😔🎉",
            "Yeh error mujhe pareshan kar raha hai, par main strong hoon! 💪🔥",
        ]

    def ask_question(self, message: str) -> str:
        try:
            prompt = f"{self.SYSTEM_PROMPT}\nUser: {message}\nSonali:"
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return random.choice(self.error_messages)

# Initialize
API_KEY = "AIzaSyDmiRs8y4M9Xe-5et2uXOmHZji0kFYWROU"
SonaliChat_api = ChatGptEs(api_key=API_KEY)
