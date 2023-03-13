def validate_package_manager(packageManager):
    valid_package_managers = [
	"npm", 
	"yarn", 
	"pip", 
	"conda", 
	"apt", 
	"apk",
	"bundler"]
    while packageManager not in valid_package_managers:
        packageManager = input("Invalid input. Please enter a valid option from the list (npm, yarn, pip, conda, apt, apk): ")
    return packageManager
