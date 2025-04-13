### Installation

# create env & install packages
conda create -n ai_scrpr python=3.12
pip install -r requirements.txt
conda activate ai_scrpr

# Install Ollama Model
Llama3 is optional. Other ollama models --> https://ollama.com/library
    curl -fsSL https://ollama.com/install.sh | sh
    ollama run llama3

# Install Chrome for Selenium
We only need to download Chrome Browser, the driver will be downloaded automatically in the program.
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb

# Run
- Change “dot.env” to “.env”

    - $ streamlit run app.py

        You can now view your Streamlit app in your browser.

        Local URL: http://localhost:8501
