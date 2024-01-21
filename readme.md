# NGL Spammer

NGL Spammer is a command-line interface (CLI) application written in Python that allows you to spam people in the NGL community with a specified username and count.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/JethroNatividad/ngl-spammer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ngl-spammer
    ```
3. Create a virtual environment:

    ```bash
    python -m venv env
    ```

4. Activate the virtual environment:

    On Windows:

    ```bash
    .\env\Scripts\activate
    ```

    On Linux and Mac:

    ```bash
    source env/bin/activate
    ```

5. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the NGL Spammer, use the following command:


```bash
python main.py --username <target_username> --count <spam_count>
```

Replace `<target_username>` with the NGL username you want to spam and `<spam_count>` with the number of spam messages you want to send.

### Example:

```bash
python main.py --username john_doe --count 100
```

### Alternatively, you can run the file directly:

```bash
python main.py
```

### Additional Options:

- `--help`: Display help and information about available parameters.

```bash
python main.py --help
```

## Disclaimer

**Use this tool responsibly!** The NGL Spammer is intended for educational and testing purposes only. Misuse of this tool for spamming or any malicious activities is strictly discouraged. The developer is not responsible for any consequences resulting from the misuse of this application.