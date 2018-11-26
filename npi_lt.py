import urllib.request, json

input_valid = True
run = True

def main():
   while run == True:

   
      postal_code = input("Enter Postal Code (Press enter for none): ")
      last_name = input("Enter Last Name (Press enter for none): ")
      first_name = input("Enter First Name  (Press enter for none): ")

      pv information_json = getNPIInformationJSON(postal_code, last_name, first_name)
      
      print("\n\nResults:\n")

      print("NPI          Last Name                      First Name                   ")
      print("-------------------------------------------------------------------------")
      
      
      for pv in pv_information_json['results']:
         print('{:10}'.format(str(pv['number'])) + "   " + '{:31}'.format(pv['basic']['last_name']) + '{:30}'.format(pv['basic']['first_name']))

      print("\n")

def getNPIInformationJSON(ZIP, lastName, firstName):
   nppes_url = urllib.request.urlopen("https://npiregistry.cms.hhs.gov/api/?limit=200&number=&enumeration_type=1&taxonomy_description=&last_name=" + last_name + "&firstname=" + first_name + "&postal_code=" + postal_code)
   providerJSONData = json.loads(nppes_url.read())
   return providerJSONData
   
   
if __name__ == '__main__':
   main()
   
