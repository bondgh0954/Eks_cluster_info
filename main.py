import boto3 as bt

client = bt.client('eks')

eks_info = client.list_clusters()['clusters']

cluster_details = client.describe_cluster(
    name=eks_info
)

cluster_d = cluster_details['cluster']
for cluster in cluster_d:
    cluster_endpoint = cluster['endpoint']
    cluster_status = cluster['status']

