resourceNames = inputProperties.get("resourceNames");

System.log("Old name is: " + resourceNames[0]);

customProperties = inputProperties.get("customProperties");

resourceNames[0] = customProperties.get("customNewName");

System.log("New name is: " + resourceNames[0]);

