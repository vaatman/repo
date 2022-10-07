#!/bin/bash

curl --request POST -k "https://rhel8-node1.local/api/v4/runners" \
	--form "token=8b8sxD7nJJr9abmJiuPW" --form "description=rhel8-node2.local" \
	--form "tag_list=ci,dev,rhel8,hv"
