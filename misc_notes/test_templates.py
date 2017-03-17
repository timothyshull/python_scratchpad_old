import os

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__))))

template = env.get_template('tgt-cluster.rc.j2')

print(template.render(myvipname='testvipname', myvip='testvip', myvip_netmask='testnetmask',
                      myvip2='testvip2', myvip2_netmask='testnetmask2'))

print(template.render(myvip='testvip', myvip_netmask='testnetmask',
                      myvip2='testvip2', myvip2_netmask='testnetmask2'))


# MYVIPNAME={{ myvipname }}
# MYVIP={{ myvip }}
# NETMASKVIP1={{ myvip_netmask }}
# MYVIP2={{ myvip2 }}
# NETMASKVIP2={{ myvip2_netmask }}
