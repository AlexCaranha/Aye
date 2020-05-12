import win32com.client

def get_usb_volume_name():  # pragma: no cover
    str_computer = "."
    logical_disk_device_ids = []
    volumes = []
    try:
        obj_wmi_service = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        obj_swbem_services = obj_wmi_service.ConnectServer(str_computer, "root\cimv2")

        # 1. Win32_DiskDrive
        col_items = obj_swbem_services.ExecQuery("SELECT * FROM Win32_DiskDrive WHERE InterfaceType = \"USB\"")
        for item in col_items:
            disk_drive_device_ids = item.DeviceID.replace('\\', '').replace('.', '')

        # 2. Win32_DiskDriveToDiskPartition
        col_items = obj_swbem_services.ExecQuery("SELECT * from Win32_DiskDriveToDiskPartition")
        disk_partition_device_ids = []
        for obj_item in col_items:
            for disk_drive_device_id in disk_drive_device_ids:
                if disk_drive_device_id in str(obj_item.Antecedent):
                    disk_partition_device_ids.append(obj_item.Dependent.split('=')[1].replace('"', ''))
                    break

        # 3. Win32_LogicalDiskToPartition
        col_items = obj_swbem_services.ExecQuery("SELECT * from Win32_LogicalDiskToPartition")
        for objItem in col_items:
            for disk_partition_device_id in disk_partition_device_ids:

                if disk_partition_device_id in str(objItem.Antecedent):
                    logical_disk_device_ids.append(objItem.Dependent.split('=')[1].replace('"', ''))
                    break

        # 4. Win32_LogicalDisk
        col_items = []
        for logical_disk_device_id in logical_disk_device_ids:
            col_items.append(obj_swbem_services.ExecQuery("SELECT * from Win32_LogicalDisk WHERE DeviceID=\"" +
                                                        logical_disk_device_id + "\""))

        for col_item in col_items:
            volumes.append(col_item[0].VolumeName)
    except IndexError:
        pass

    volumes_result = []
    logical_disk_device_ids_result = []
    for i in range(len(volumes)):
        if volumes[i] != "":
            volumes_result.append(volumes[i])
            logical_disk_device_ids_result.append(logical_disk_device_ids[i])

    return logical_disk_device_ids_result, volumes_result


output = get_usb_volume_name()
print(output)