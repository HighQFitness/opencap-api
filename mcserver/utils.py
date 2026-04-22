from django.conf import settings
import boto3


def submit_custom_metric(namespace, metric_name, value):
    """
    Submit a custom metric to AWS CloudWatch.

    Parameters:
    - namespace (str): The namespace for the metric data.
    - metric_name (str): The name of the metric.
    - value (float): The value associated with the metric.
    """
    client = boto3.client('cloudwatch', region_name=settings.AWS_S3_REGION_NAME)
    response = client.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': metric_name,
                'Value': value,
                'Unit': 'Count',
            }
        ]
    )
    return response


def get_processing_trials_count():
    from mcserver.models import Trial
    return Trial.objects.filter(status='stopped').count()


def submit_number_of_pending_trials_to_cloudwatch():
    # Submit the metric
    response = submit_custom_metric(
        'Custom/opencap-dev' if settings.DEBUG else 'Custom/opencap',
       'opencap_trials_pending',
        get_processing_trials_count(),
    )
    print("Metric submitted successfully:", response)
