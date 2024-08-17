# info7375-chatbot-rag-vector-db

### Report and Video

[Report](./Ruis_Report.pdf)
[Video](https://youtu.be/3rSdGStHiIc)

### Installation

1. Clone the repository.
2. Navigate to your repository directory: ‘cd your-repository’.
3. Create a virtual environment: 'pipenv shell'.
4. Install the required packages: 'pipenv install'.
5. Set up environment variables:
   Create a `.env` file in the root directory of your project and add your Pinecone API key, OpenAI API key
   ```
   PINECONE_API_KEY=
   OPENAI_API_KEY=
   ```
6. Fetch data from the MongoDB website:
   mkdir mongodb-docs
   wget -r -P mongodb-docs -E https://www.mongodb.com/docs/manual
7. Pre-process the data by running the process_data.py script. You should see the following message if successful:
   Going to add xxx to Pinecone
   Loading to vectorstore done
8. Start the app: streamlit run main.py.

### Contact me
zhou.rui3@northeasten.edu

I would like NOT to share the project on public platforms.
