import streamlit as st
import requests

st.title("Astro Chat🚀")


######## Title and introduction #######
st.write("Astro Chat will answer all of your questions about the ARSSDC and the RFP!!")
st.sidebar.success("You've Selected Chat Bot Page")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
################################## Set API #########


## the first one useless####
# API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=64a6d8e57f17eae62d53dc62&org=a2b18288-c473-4bfb-8291-f07d0cabf827"
# headers = {'Authorization':
#            'Bearer fa95120b-578e-40f4-b38b-5a69080e2ed4',
#            'Content-Type': 'application/json'
#            }


# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()

# ///////////////////////////////////////////////////////////#
# API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=652d65f78430aaf63cfcf815&org=f18675dd-f661-4d3f-8dab-a5c345de78db"
# headers = {'Authorization':
#            'Bearer 9556663b-898b-4feb-98c6-f9536811b433',
#            'Content-Type': 'application/json'
#            }


# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()


#################

# API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=64a6d8e57f17eae62d53dc62&org=a2b18288-c473-4bfb-8291-f07d0cabf827"
# headers = {'Authorization':
#            'Bearer fa95120b-578e-40f4-b38b-5a69080e2ed4',
#            'Content-Type': 'application/json'
#            }

# ASEA API
API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=659e84417c04c17941237900&org=54bd58b7-9ffa-4161-91f0-565405a9d32d"
headers = {'Authorization':
           'Bearer cfc3f051-23da-4dc6-b3e8-0fce0dabe449',
           'Content-Type': 'application/json'
           }
#########################################


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


################## CHAT BOT############
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Write down your prompt here:"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    answer = query({"in-1": prompt})
    # Extract the string from the response dictionary
    response = answer.get('out-4', '')

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
