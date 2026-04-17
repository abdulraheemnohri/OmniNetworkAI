from pysnmp.hlapi import *

class SwitchController:
    def __init__(self, ip, community='public'):
        self.ip = ip
        self.community = community

    def get_port_status(self, port_index):
        # SNMP OID for ifOperStatus
        oid = f'1.3.6.1.2.1.2.2.1.8.{port_index}'
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity(oid)))
        )

        if errorIndication:
            return f"Error: {errorIndication}"
        elif errorStatus:
            return f"Error: {errorStatus.prettyPrint()}"
        else:
            for varBind in varBinds:
                status = varBind[1]
                return "Up" if status == 1 else "Down"

    def get_traffic_stats(self, port_index):
        # SNMP OID for ifInOctets and ifOutOctets
        in_oid = f'1.3.6.1.2.1.2.2.1.10.{port_index}'
        out_oid = f'1.3.6.1.2.1.2.2.1.16.{port_index}'
        # Simplified implementation
        return f"Port {port_index} Traffic: Mock stats (In: 100MB, Out: 50MB)"
