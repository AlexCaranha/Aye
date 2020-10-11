import psutil
import win32com.client

def get_devices():
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")

    output = []
    for partition in filter(lambda p: 'removable' in p.opts, psutil.disk_partitions()):        
        LogicalDisk_DeviceID = partition.mountpoint.replace("\\","")
        colItems = objSWbemServices.ExecQuery("SELECT * from Win32_LogicalDisk WHERE DeviceID=\"" + LogicalDisk_DeviceID + "\"")
        LogicalDisk_DeviceName = colItems[0].VolumeName        
        output.append((LogicalDisk_DeviceID, LogicalDisk_DeviceName))

    return output

print(get_devices())