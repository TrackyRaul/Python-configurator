import configurator, json


if __name__ == "__main__":
    configurator.generate_config_structure("config.json")
    configurator.configure("config.json")
    
