import urllib.request, json

input_valid = True
run = True

while run == True:

   
   postal_code = input("Enter Postal Code (Press enter for none): ")
   last_name = input("Enter Last Name (Press enter for none): ")
   first_name = input("Enter First Name  (Press enter for none): ")

   nppes_url = urllib.request.urlopen("https://npiregistry.cms.hhs.gov/api/?limit=200&number=&enumeration_type=1&taxonomy_description=&last_name=" + last_name + "&firstname=" + first_name + "&postal_code=" + postal_code)

   pv_information_json = json.loads(nppes_url.read())


   
   print("\n\nResults:\n")

   print("NPI          Last Name                      First Name                   ")
   print("-------------------------------------------------------------------------")
      
      
   for pv in pv_information_json['results']:
      print('{:10}'.format(str(pv['number'])) + "   " + '{:31}'.format(pv['basic']['last_name']) + '{:30}'.format(pv['basic']['first_name']))


   print("\n")

