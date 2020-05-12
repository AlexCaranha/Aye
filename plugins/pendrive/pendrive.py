from yapsy.IPlugin import IPlugin
from plugins.categories import HandleFile
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

    def get_data(self):
        strComputer = "."
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")

        # 1. Win32_DiskDrive
        colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_DiskDrive WHERE InterfaceType = \"USB\"")
        DiskDrive_DeviceID = colItems[0].DeviceID.replace('\\', '').replace('.', '')
        DiskDrive_Caption = colItems[0].Caption

        # 2. Win32_DiskDriveToDiskPartition
        colItems = objSWbemServices.ExecQuery("SELECT * from Win32_DiskDriveToDiskPartition")
        for objItem in colItems:
            if DiskDrive_DeviceID in str(objItem.Antecedent):
                DiskPartition_DeviceID = objItem.Dependent.split('=')[1].replace('"', '')

        # 3. Win32_LogicalDiskToPartition
        colItems = objSWbemServices.ExecQuery("SELECT * from Win32_LogicalDiskToPartition")

        for objItem in colItems:
            if DiskPartition_DeviceID in str(objItem.Antecedent):
                LogicalDisk_DeviceID = objItem.Dependent.split('=')[1].replace('"', '')

        # 4. Win32_LogicalDisk
        colItems = objSWbemServices.ExecQuery("SELECT * from Win32_LogicalDisk WHERE DeviceID=\"" + LogicalDisk_DeviceID + "\"")

        print('Unidade:', LogicalDisk_DeviceID)
        print('Nome:', colItems[0].VolumeName)

    def run(self, input):
        # Search for something
        sentence = self.is_simple_question(r'localizar pendrive', input)
        if sentence is not None:
            self.get_data()
            return