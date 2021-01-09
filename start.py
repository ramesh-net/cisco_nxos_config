import os
print('''Select config template:
                        1. Vlan config
                        2. Interface config
                        3. OSPF config
                        4. BGP Config
                        5. One or more config
                        6. Exit \n''')
config_option=input("Enter Option: ")
vlan_option=ospf_option=bgp_option=interface_option='no'                                          
def variable(template_type):
    cmd="cp host_vars/"+template_type+" roles/basic_nxos_config/vars/main.yml"
    os.system(cmd)
    cmd="vim roles/basic_nxos_config/vars/main.yml"
    os.system(cmd)
def ansible(config_option,vlan_option,interface_option,ospf_option,bgp_option):
    cmd="ansible-playbook nxos_config.yml -u cisco -k -e option="+str(config_option)+" -e interface_option="+str(interface_option)+" -e vlan_option="+str(vlan_option)+" -e ospf_option="+str(ospf_option)+" -e bgp_option="+str(interface_option)
    os.system(cmd)
if (config_option==1):
    #host=raw_input("Enter hostname :")
    variable("vlan_template.yml")
    ansible(config_option,vlan_option,interface_option,ospf_option,bgp_option)
elif (config_option==2):
    #host=raw_input("Enter hostname :")
    variable("l2_interface_template.yml")
    ansible(config_option,vlan_option,interface_option,ospf_option,bgp_option)
elif (config_option==3):
    #host=raw_input("Enter hostname :")
    variable("ospf_template.yml")
    ansible(config_option,vlan_option,interface_option,ospf_option,bgp_option)
elif (config_option==4):
    #host=raw_input("Enter hostname :")
    variable("bgp_template.yml")
    ansible(config_option,vlan_option,interface_option,ospf_option,bgp_option)    
elif (config_option==5):
    print("Type 'yes' whichever config is required")
    vlan_option= raw_input("VLAN Config: ").lower()
    interface_option= raw_input("Interface Config: ").lower()
    ospf_option=raw_input("OSPF Config: ").lower()
    bgp_option=raw_input("BGP Config: ").lower()
    variable("multi_config_template.yml")
    ansible(config_option,vlan_option,interface_option,ospf_option,bgp_option)
    
    


