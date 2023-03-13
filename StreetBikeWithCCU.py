class StreetBikeWithCCU():

    def __init__(self, name, vin, color):
        self.name = name
        self.vin = vin
        self.color = color

    def start_navigation(self):
        raise NotImplementedError("Subclasses have to implement this method!")

    def open_main_screen(self):
        raise NotImplementedError("Subclasses have to implement this method!")

    def open_navigation_menu(self):
        raise NotImplementedError("Subclasses have to implement this method!")

    def open_bluetooth_settings_menu(self):
        raise NotImplementedError("Subclasses have to implement this method!")  

    def enable_hbs_commands(self):
        raise NotImplementedError("Subclasses have to implement this method!")

    def disable_hbs_commands(self):
        raise NotImplementedError("Subclasses have to implement this method!")

    def start_restbus_simulation(self):
        raise NotImplementedError("Subclasses have to implement this method!")

    def stop_restbus_simulation(self):
        raise NotImplementedError("Subclasses have to implement this method!")

