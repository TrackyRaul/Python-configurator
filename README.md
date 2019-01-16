# Python-configurator

### This python script allows for developers to create a custom config files that can be used in any python project.

---

#### You must know this before using it:

* There is a basic config file structure that needs to be followed for the configurator to work: 
  
        {
            "profiles": {
                "default": {}
            },
            "selected_profile": "default"
        }
    In here you can add as many profiles as you want and each profile can contain as much information as you want.

* The default profile must always exist!
* If the selected profile is the default one, the program will prompt you a message asking you to choose or create another profile
  
#### Use example:

##### Config.json

        {
            "profiles": {
                "default": {
                    db:{
                        "user":"root",
                        "password":"1234",
                        "host":"
                        }
                    },
                "profile1": {
                    db:{
                        "user":"root",
                        "password":"1234",
                        "host":"localhost",
                        "database":"mydata"

                    }
                }
            },
            "selected_profile": "profile1"
        }
    
##### Python script

    conf = configurator.configure("config.json")
    
    print("Connecting to db %s" %conf.db.database)

##### Python output

    >>>> Connecting to db mydata
