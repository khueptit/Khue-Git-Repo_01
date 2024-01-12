def handler(context, inputs):

    print(inputs)
    
    old_name = inputs["inputProperties"]["resourceNames"][0]
    print(old_name)
   
    new_name = inputs["inputProperties"]["customProperties"]["customNewName"]+"_"+inputs["inputProperties"]["customProperties"]["customSITeam"]
    
    print(new_name)
    #Windows OS doesn't allow "_" in hostname, so it will be auto-converted to "-"

    outputs = {}
    outputs["resourceNames"] = inputs["inputProperties"]["resourceNames"]

    print(outputs["resourceNames"])

    outputs["resourceNames"][0] = new_name

    print("Setting machine name from {0} to {1}".format(old_name, outputs["resourceNames"][0]))

    return outputs

{
    "resourceNames":["Old"],
    "customProperties":{
        "customNewName":"KhuePM",
        "customSITeam":"Sys"
    }
}


{"customNewName":"KhuePM","customSITeam":"Sys"}