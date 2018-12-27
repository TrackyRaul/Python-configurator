# Python-configurator

### This python script allows for developers to create a custom config files that can be used in any python project.

---

#### You must know this before using it:

* There is a basic config file structure that needs to be followed for the configurator to work: 
  
        {
            "profiles": {
                "default": {}
                }
            },
            "selected_profile": "default"
        }
    In here you can add as many profiles as you want and each profile can contain as much information as you want.

* The default profile must always exist!
* If the selected profile is the default one, the program will prompt you a message asking you to choose or create another profile