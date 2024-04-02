import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
import pandas as pd
from tqdm import tqdm


# Read the 'shortfall_filtered.csv' file into a DataFrame
df = pd.read_csv('bipin_df.csv')

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

text_model=genai.GenerativeModel("gemini-pro")


def get_gemini_response(input, row_data):
    response = text_model.generate_content([input, row_data])
    return response.text
"""
for index, row in df.iterrows():
    dialogue_text = row['dialogue']
    response_text = get_gemini_response(prompt_to_gemini, dialogue_text)
    
    df.at[index, 'summary'] = response_text

df.to_csv('shortfall_filtered_prompted.csv', index=False)


counter = 0

for index, row in df.iterrows():
    dialogue_text = row['text']
    
    response_text = get_gemini_response(prompt_to_gemini, dialogue_text)
    
    df.at[index, 'summary'] = response_text
    
    counter += 1
    
    if counter >= 5:
        break

df.to_csv('shortfall_filtered_prompted.csv', index=False)

"""
counter = 0
for index, row in tqdm(df.iterrows(), total=len(df)):
    dialogue_text = row['text']
    lable = row['label']
    prompt_to_gemini = f"""you are expert in text summarization. I have a text data of {lable} of an applications. 
                    your task is generate summary of the given text in one paragraph not list and less than 20 token. 
                    Also do not give markdown"""

    try:
        response_text = get_gemini_response(prompt_to_gemini, dialogue_text)
        #print(response_text)

        df.at[index, 'summary'] = response_text
        #print(f"Processed Index : {index}")
    except:
        print(f"Error in {index}")
    
    time.sleep(1.2)

df.to_csv('bipin_prompted_summary.csv', index=False)

