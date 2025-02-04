import psutil

usb_hwid = 'USBSTOR\DiskKingstonDataTraveler_3.0PMAP' #hardware ID of the USB drive

for partition in psutil.disk_partitions(all=True):
    if partition.opts.startswith('removable'):
        try:
            partition_hwid = psutil.disk_usage(partition.mountpoint).fstype.split('\\')[-1]
            if partition_hwid == usb_hwid:
                print(f"USB drive found at {partition.device}")
                break
        except Exception:
             print("Opps! there was an error!")
else:
    print("USB drive not found")