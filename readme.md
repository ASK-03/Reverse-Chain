# Reverse Chain
Implementation of paper: [Reverse Chain: A Generic-Rule for LLMs to Master Multi-API Planning](https://arxiv.org/abs/2310.04474v2). This implementation uses FAISS vector database to retrieve API documentation on the basis of the query.

**THIS IS NOT AN OFFICIAL IMPLEMENTATION OF REVERSE CHAIN**

## Dependencies
- **Python3**: Ensure that you have Python 3 installed on your system. You can download and install Python 3 from the official Python website: https://www.python.org.
- **pip**: pip is the package installer for Python. It is usually installed by default when you install Python. However, make sure you have pip installed and it is up to date. You can check the version of pip by running the following command:
  ```
  pip --version
  ```
## Installation
To install and use Reverse-Chain, follow the steps given below:
- Fork the Reverse-Chain repository by clicking the "Fork" button at the top right corner of the repository page. This will create a copy of the repository under your GitHub account.
- Clone the forked repository to your local machine:
    ```
    git clone https://github.com/{YOUR-USERNAME}/Reverse-Chain
    ```
- Navigate to the project directory: 
    ```
    cd Reverse-Chain
    ```
- Install the necessary Python packages by running the following command:
  ```
  pip install -r requirements.txt
  ```
(NOTE: It is recommended to install these requirements in a new python environment)

## How to use?

Follow the steps given below:

- Add the documentation of the APIs in the `data/api_documentation` folder in `.txt` format. The format in which the documentation is required is given in the folder.
- Make changes in the `example.config.ini` file
    - Add your OpenAI Secret Key in the `secret_key` variable in the `openai` section.
    - Add your query in the `query` variable in the `query` section.
    - Other parameters can also be changed in the config file like, model, temperature, huggingface embedding model that FAISS database will use.
     
  **Change the name to `config.ini`**
- Initialize the FAISS database by executing the command below:
  ```
  python3 create_vector_db.py
  ```
  This will create the FAISS database using the documentation added in the `data/api_documentation`
- Now, the setup is complete :)
- Run the model by executing the command below:
  ```
  python3 main.py
  ```

## Output
The output of the run is saved in `output/run.json` file and the logs are saved in `logs/run.log` file.

## Future Developement
It is not completely correct and maynot produce similar results as claimed in the paper. The following are few points of developement that can be done in the implementation:

### Code & Prompts
1. Prompts can be made better.
2. Code in `main.py` can be refactored to look prettier.
3. `ArgumentExtractor` class returns the arguments found in the query, its prompt can be updated in a way that it selects arguments only that are needed for the current API.

## Contributions
Contributions to Reverse-Chain are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## Author
[Abhishek Singh Kushwaha](https://github.com/ASK-03)
