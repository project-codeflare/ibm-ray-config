from lithopscloud.modules.vpc import VPCConfig
from typing import Any, Dict

class LithopsVPCConfig(VPCConfig):
    
    def __init__(self, base_config: Dict[str, Any]) -> None:
        super().__init__(base_config)

        self.vpc_name = 'lithops-cluster-vpc'

    def update_config(self, vpc_obj, zone_obj, sec_group_id, subnet_id):
        self.base_config['ibm_vpc']['vpc_id'] = vpc_obj['id']
        self.base_config['ibm_vpc']['zone_name'] = zone_obj['name']
        self.base_config['ibm_vpc']['resource_group_id'] = vpc_obj['resource_group']['id']
        self.base_config['ibm_vpc']['security_group_id'] = sec_group_id
        self.base_config['ibm_vpc']['subnet_id'] = subnet_id


        

