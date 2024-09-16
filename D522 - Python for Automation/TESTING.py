network_devices = ['Switch39', 'Router49', 'Server27', 'Switch58', 'Router44', 'Server31', 'Server34', 'Switch84', 'Hub43', 'Switch80', 'Router20', 'Hub67', 'AccessPoint89', 'Firewall53', 'Server15', 'Router68', 'Router56', 'AccessPoint27', 'Router90', 'Hub33', 'Server51', 'Server12', 'AccessPoint17', 'Firewall73', 'AccessPoint28', 'Switch37', 'Switch92', 'AccessPoint99', 'AccessPoint60', 'Hub10', 'Server56', 'AccessPoint13', 'Hub5', 'Switch65', 'Router4', 'Firewall38', 'Server25', 'AccessPoint57', 'Firewall63', 'Switch17', 'AccessPoint92', 'Hub88', 'AccessPoint23', 'Firewall88', 'Switch74', 'Firewall38', 'Hub84', 'Router30', 'Router79', 'Switch56']

altered_list = []
# do not edit above this line

# remove last 40 devices
altered_list = network_devices.remove[-40:]
# change second and third devices to "removal pending"
altered_list[1:3] = ["removal pending"]
# change device at index 8 to "AccessPoint23"
altered_list[8] = "AccessPoint23"

print(network_devices[-39])

# do not edit below this line
print(f"devices: {len(altered_list)}")
print(altered_list)

# Expected output
# devices: 10
# ['Switch39', 'removal pending', 'removal pending', 'Switch58', 'Router44', 'Server31', 'Server34', 'Switch84', 'AccessPoint23', 'Switch80']