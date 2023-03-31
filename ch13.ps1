# does powerhsell even have a shabang?

# Active Directory automation
# Stanley L. Ferguson III
# 30 Mar 2023
# Create a powershell scrip that adds users to the Active Directory

# Tyler helped me catch up on this one he said he's not great with powershell but I think he's lying

# assign variable to the user and his credentials
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$description = "TPS Reporting Lead at GlobeX USA in Springfield, OR office"
$office = "Springfield, OR"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"
$username = "ferdinand"
$password = "b@lls4ck"  
# define new user path
$ouPath = "OU=Users,OU=GlobeX USA,DC=Corp,DC=globexpower,DC=com" 
# Create new user
New-ADUser -Name $displayName -GivenName $firstName -Surname $lastName -Description $description `
    -Office $office -Department $department -EmailAddress $email -SamAccountName $username `
    -AccountPassword (ConvertTo-SecureString $password -AsPlainText -Force) -Enabled $true -Path $ouPath
