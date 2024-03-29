from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, service_name):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        new_service = self.VALID_SERVICES[service_type](service_name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        new_robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return "Unsuitable service."

        elif isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name, service_name):
        service = [s for s in self.services if s.name == service_name][0]
        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))

        except StopIteration:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name):
        service = [s for s in self.services if s.name == service_name][0]
        for robots in service.robots:
            robots.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name):
        service = [s for s in self.services if s.name == service_name][0]
        prices_list = []

        for robot in service.robots:
            prices_list.append(robot.price)

        return f"The value of service {service_name} is {sum(prices_list):.2f}."

    def __str__(self):
        details = [s.details() for s in self.services]
        return "\n".join(map(str, details))