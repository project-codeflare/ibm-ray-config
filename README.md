# Tool to generate Lithops configuration file

ibm-ray-config is a CLI tool that greatly simplifies user experience by generating Ray configuration files for IBM services.

## Setup

The tool been mostly tested with Ubuntu 18.04/20.04 and Fedora 35, but should work with most Linux systems
Requirements: `ssh-keygen` utility installed:
```
sudo apt install openssh-client
```

Install `ibm-ray-config` from pip repository

```
pip install ibm-ray-config
```

## Usage
Use the configuration tool as follows

```
ibm-ray-config [--iam-api-key IAM_API_KEY] [-i INPUT_FILE] [-o OUTPUT_PATH] [--version] [--defaults] 
```
Get a short description of the available flags via ```ibm-ray-config --help```

<br/>

#### Flags Detailed Description

<!--- <img width=125/> is used in the following table to create spacing --->
 |<span style="color:orange">Key|<span style="color:orange">Default|<span style="color:orange">Mandatory|<span style="color:orange">Additional info|
 |---|---|---|---|
 | iam-api-key   | |yes|IBM Cloud API key. To generate a new API Key, adhere to the following [guide](https://www.ibm.com/docs/en/spectrumvirtualizecl/8.1.3?topic=installing-creating-api-key)
 | input-file    |<compute_backend>/defaults.py| no | Existing config file to be used as a template in the configuration process |
 | output-path   |A randomly generated path to a randomly named yaml file | no |A custom location the config file will be written to |
 | version       | | no |Returns ibm-ray-config's package version|



### Using ibm-ray-config to generate config file without user interaction
In order to let ibm-ray-config generate config file based on some defaults and create vpc and all its peripheral assets automatically, please run:

```
ibm-ray-config -a <API_KEY>  --defaults
```

### Using ibm-ray-config config tool programmatically
Notice, not all fields are mandatory. Unspecified resources will be created automatically on the backend.

E.g.
If existing vpc id not provided - vpc will be created automatically with all required peripheral resources like security groups, gateway.. etc following minimal default requirements
If ssh key details not provided - new ssh key pair will be generated and registered in ibm cloud

###### Ray Gen2
```
from ibm_ray_config import generate_config

api_key = '<IAM_API_KEY>'
region = 'eu-de'
generate_config(iam_api_key=api_key, region=region, image_id='r010-5a674db7-95aa-45c5-a2f1-a6aa9d7e93ad', key_id='r010-fe6cb103-60e6-46bc-9cb5-14e415990849', ssh_key_filename='/home/kpavel/.ssh/id_rsa', profile_name='bx2-2x8', vpc_id='r010-af1adda4-e4e5-4060-9aa2-7a0c981aff8e', min_workers=1, max_workers=1)
```

Mandatory fields are:  api_key, region.
Minimal example:

```
from ibm_ray_config import generate_config

api_key = <IAM_API_KEY>
region = 'eu-de'
config_file = generate_config(iam_api_key=api_key, region=region)
```
