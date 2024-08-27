import boto3

from .s3_utils import parse_s3_uri, create_presigned_url

def wait_for_completion(task_id, session=None):
    session = session or boto3.Session()
    polly = session.client("polly")
    while True:
        task = polly.get_speech_synthesis_task(TaskId=task_id)
        if task["SynthesisTask"]["TaskStatus"] == "completed":
            break
    return task["SynthesisTask"]["OutputUri"]

def synthesize(output_prefix_uri, text, session=None):
    session = session or boto3.Session()
    polly = session.client("polly")
    output_bucket, output_prefix = parse_s3_uri(output_prefix_uri)
    result = polly.start_speech_synthesis_task(
        LanguageCode="en-GB",
        OutputFormat="mp3",
        OutputS3BucketName=output_bucket,
        OutputS3KeyPrefix=output_prefix,
        SampleRate="24000",
        Text=text,
        VoiceId="Amy",
    )
    task_id = result["SynthesisTask"]["TaskId"]
    wait_for_completion(task_id)
    output_uri = output_prefix_uri + "." + task_id + ".mp3"
    return create_presigned_url(output_uri)
