#!/usr/bin/env python3

# Script:                       Ops 301 Ops Chall #12
# Author:                       Brad Baack
# Date of latest revision:      04/10/2024
# Purpose:                   

# PowerShell script to add Franz Ferdinand to Active Directory

# User details
$name = "Franz Ferdinand"
$samAccountName = "ferdinandf"
$userPrincipalName = "ferdi@GlobeXpower.com"
$email = "ferdi@GlobeXpower.com"
$department = "TPS Department"
$title = "TPS Reporting Lead"
$office = "Springfield, OR"

# Creating the user
New-ADUser `
    -Name $name `
    -GivenName "Franz" `
    -Surname "Ferdinand" `
    -SamAccountName $samAccountName `
    -UserPrincipalName $userPrincipalName `
    -EmailAddress $email `
    -Department $department `
    -Title $title `
    -Office $office `
    -Enabled $true `
    -AccountPassword (Read-Host -AsSecureString "Set User Password") `
    -PassThru `
    -Verbose

# Note: The script prompts for a password for the new user. This needs to be typed interactively.
