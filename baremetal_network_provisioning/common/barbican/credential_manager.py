# Copyright 2016 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from barbicanclient import client as barbican_client

from baremetal_network_provisioning.common.barbican import keystone

from oslo_config import cfg

CONF = cfg.CONF


def create_secret(payload, name='bnp', payload_content_type=None,
                  payload_content_encoding_type=None, algorithm='aes',
                  bit_length=256, secret_type=None, mode='cbc',
                  expiration=None):
    keystone_session = keystone.get_session()
    barbican_client_session = barbican_client.Client(keystone_session)
    secret = barbican_client_session.secrets.create()
    secret.name = name
    secret.payload = payload
    secret.payload_content_type = payload_content_type
    secret.payload_content_encoding_type = payload_content_encoding_type
    secret.algorithm = algorithm
    secret.bit_length = bit_length
    secret.secret_type = secret_type
    secret.mode = mode
    secret.expiration = expiration
    href = secret.store()
    return href


def retrieve_secret(href):
    keystone_session = keystone.get_session()
    barbican_client_session = barbican_client.Client(keystone_session)
    return barbican_client_session.secrets.get(href).payload


def delete_secret(href):
    keystone_session = keystone.get_session()
    barbican_client_session = barbican_client.Client(keystone_session)
    barbican_client_session.secrets.delete(href)


def list_secret(name=None, limit=None, offset=None, algorithm=None, mode=None,
                bits=None):
    keystone_session = keystone.get_session()
    barbican_client_session = barbican_client.Client(keystone_session)
    secret = barbican_client_session.secrets.list(
        name=name, limit=limit, offset=offset, algorithm=algorithm, mode=mode,
        bits=bits)
    return secret
