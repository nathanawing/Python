temp = open('shadow')
file = temp.read()
temp.close()
temp = open('passwd')
file2 = temp.read()
temp.close()
shadowList = file.splitlines()
passList = file2.splitlines()
numUsers = len(shadowList)
disabled = file.count(':*:')
print("There are " + str(numUsers) + " total accounts")
print(str(disabled) + " accounts are disabled")
locked = file.count(':!:')
print(str(locked) + " accounts are locked")
noPass = file.count(':!!:')
print(str(noPass) + " accounts are locked without passwords")
passwords = file.count(':$6$')
print(str(passwords) + " accounts have passwords")
noExpire = 0
expired = 0
for i in range(numUsers):
    userShad = shadowList[i].split(':')
    try:
        if int(userShad[4]) > 90:
            print(userShad[0] + "'s password expires after more than 90 days")
            noExpire += 1
    except ValueError:
        print(userShad[0] + "'s password does not have an expiration date")
        noExpire += 1
print(str(noExpire) + " account passwords do not expire")
for i in range(numUsers):
    userShad = shadowList[i].split(':')
    if userShad[7] != "":
        print(userShad[0] + "'s password is expired")
        expired += 1
if expired > 0:
    print(str(expired) + " account passwords have expired")
else:
    print("No accounts are expired")
for i in range(numUsers):
    userShad = shadowList[i].split(':')
    userPW = passList[i].split(':')
    userID = userPW[2]
    if int(userID) >= 1000 and userShad[1] == "*":
        print("User account: " + userShad[0] + " does not have a password with UID: " + userID)