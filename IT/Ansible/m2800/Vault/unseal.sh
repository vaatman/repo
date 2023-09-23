#!/bin/bash

KEYSFILE=${1}
VAULT_KEYS=$(grep ^Unseal ${KEYSFILE} |awk '{print $4}')

for KEY in ${VAULT_KEYS}
do
 payload=$(echo "{ \"key\": \"${KEY}\" }")
 curl --request POST --data "${payload}" http://rhel86-2.local:8200/v1/sys/unseal
done
