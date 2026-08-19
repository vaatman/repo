#!/bin/bash

sudo cat << 'EOF' > /etc/yum.repos.d/rocky-baseos.repo
[baseos]
name=Rocky Linux 10 - BaseOS
mirrorlist=https://rockylinux.org
gpgcheck=1
enabled=1
countme=1
metadata_expire=6h
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-10
EOF

sudo cat << 'EOF' > /etc/yum.repos.d/rocky-appstream.repo
[appstream]
name=Rocky Linux 10 - AppStream
mirrorlist=https://rockylinux.org
gpgcheck=1
enabled=1
countme=1
metadata_expire=6h
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-10
EOF
