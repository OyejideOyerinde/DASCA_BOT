import openai
import PyPDF2

# Set up OpenAI API credentials
openai.api_key = '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'

# Extract text from PDF using PyPDF2
def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        # Initialize an empty string to store the extracted text
        extracted_text = ""

        # Extract text from each page
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            extracted_text += page.extract_text()

        return extracted_text

# Initialize the chatbot
class Chatbot:
    def __init__(self, text):
        self.text = text
        self.chat_history = []

    def chat(self, user_input):
        # Add the user's input to the chat history
        self.chat_history.append(user_input)

        # Generate a response from the model based on the chat history
        response = openai.Completion.create(
            engine='davinci',
            prompt='\n'.join([self.text] + self.chat_history),
            temperature=0.3,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        # Extract the generated response from the API response
        generated_response = response.choices[0].text.strip()

        # Add the generated response to the chat history
        self.chat_history.append(generated_response)

        # Print the response
        print(generated_response)

# Provide the path to the PDF file
pdf_file_path = r"C:\Users\OCTAVE_ANALYTICS_01\Documents\Frequently Asked Questions.pdf"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_file_path)

# Create a new chatbot object with the PDF text
chatbot = Chatbot(pdf_text)

# Start chatting with the chatbot
while True:
    # Get the user's input
    user_input = input("User: ")

    # Chatbot responds to the user's input
    chatbot.chat(user_input)
