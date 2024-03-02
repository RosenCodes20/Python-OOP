class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app, app_memory):
        if self.memory >= app_memory and self.is_on == True:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"

        elif self.memory >= app_memory and self.is_on == False:
            return f"Turn on your phone to install {app}"

        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
smartphone.power()
print(smartphone.install("Instagram", 20))
print(smartphone.install("Instagram", 40))
smartphone.power()
print(smartphone.install("Facebook", 20))
smartphone.power()
print(smartphone.install("YouTube", 40))
print(smartphone.status())