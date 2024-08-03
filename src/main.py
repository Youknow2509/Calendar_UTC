from get_data import get_data
from gg_handle import *

def main():
    """
        Main function
    """
    # get_data()
    # get_all_events()
    # create_event(title='Test create event with api')
    
    create_event_adv(title='Test create "adv" event with api', days=[2, 3])
    # delete_all_events()
    
if __name__ == "__main__":
    main()
    
    