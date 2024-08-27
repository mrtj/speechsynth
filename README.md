# SpeechSynth

Simple [streamlit](https://streamlit.io) app wrapping [Amazon Polly](https://aws.amazon.com/polly/) service.

## Install and run

1. Get [poetry](https://python-poetry.org) or `pip install .`
2. Create a `.streamlit/secrets.toml` file with this template:

    ```toml
    output_prefix_uri = "s3://my-bucket/prefix"
    password = "password"
    ```

3. [Configure your AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

4. `streamlit run st_app.py`
