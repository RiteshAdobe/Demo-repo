import base64
import json

import in_toto.models.layout
from in_toto.verifylib import in_toto_verify
from in_toto.models.link import Link

from owner_alice.create_layout import layout

# Load the link metadata for the third step
step_name = 'clone'
link_file_path = f'clone.776a00e2.link'
try:
    with open(link_file_path, 'r') as link_file:
        link_metadata_content = link_file.read()
        link_metadata_dict = json.loads(link_metadata_content)
        link_metadata_dict = json.loads(base64.b64decode(link_metadata_dict["payload"]))
        link_metadata = Link(**link_metadata_dict)
except FileNotFoundError:
    print(f"Link metadata file for {step_name} not found.")
    exit(1)

# Perform the verification for the third step

in_toto_verify(layout, {step_name: link_metadata})
# try:
#     in_toto_verify(layout, {step_name: link_metadata})
#     print(f"Partial verification for {step_name} succeeded.")
# except Exception as e:
#     print(f"Partial verification for {step_name} failed: {e}")
