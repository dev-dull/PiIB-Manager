import yaml
import gpiozero

from CONSTS import C

def load_config():
    fin =  open('config.yaml', 'r')
    confs =  fin.read()
    fin.close()
    conf = yaml.load(confs, Loader=yaml.SafeLoader)
    
    for k,v in conf.items():
        setattr(C, k, v)
        
    return C

def main():
    load_config()
    print('yup, that\'s right')

if __name__ == '__main__':
    main()
