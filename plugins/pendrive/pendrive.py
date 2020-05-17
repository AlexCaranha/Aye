from yapsy.IPlugin import IPlugin
from plugins.categories import HandleFile
import psutil
import win32com.client
import re

class Pendrive(HandleFile):
    def setup(self, parent):
        self.parent = parent        
        print(f"{parent.name} loaded: ok.")

    def is_simple_question(self, pattern, input: str):
        match = re.search(pattern, input, re.IGNORECASE)
        return match

    def is_the_question(self, pattern, input: str):
        match = re.search(pattern, input, re.IGNORECASE)
        return match.group('sentence') if match is not None else None

    def search_devices(self):
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")

        # output = []
        for partition in filter(lambda p: 'removable' in p.opts, psutil.disk_partitions()):        
            LogicalDisk_DeviceID = partition.mountpoint.replace("\\","")
            colItems = objSWbemServices.ExecQuery("SELECT * from Win32_LogicalDisk WHERE DeviceID=\"" + LogicalDisk_DeviceID + "\"")
            LogicalDisk_DeviceName = colItems[0].VolumeName        
            # output.append((LogicalDisk_DeviceID, LogicalDisk_DeviceName))
            return f"unidade: {LogicalDisk_DeviceID} e nome: {LogicalDisk_DeviceName}"

        return None

    def run(self, input):
        # Search for something
        sentence = self.is_simple_question(r'localizar pendrive', input)
        if sentence is not None:
            output = self.search_devices()
            return output

        # Search for something
        sentence = self.is_simple_question(r'localizar pen drive', input)
        if sentence is not None:
            output = self.search_devices()
            return output
