import argparse


class ParkingSlot:
    """
    Creating Parking Slot instance

    :param: file : Output file (Required if needs to write output in a file)
    """

    def __init__(self, file=None):
        self.file = file
        self.total_slots = {}

    def create_parking_lot(self, slots):
        """
            Create Parking Lot

            :param: slots: Number of parking slots to be created
            :type: slots: Integer
            :return: Number of slots created

            """
        if slots > 0:
            self.total_slots = {i: None for i in range(1, slots + 1)}
            # To print in terminal or to write in file directly
            print('Created parking of {} slots'.format(slots), file=self.file)
            # to handle test cases
            return len(self.total_slots)

    def allocateSlot(self, vehicle_number):
        """
            Allocate Parking slot

            :param: vehicle_number: Vehicle instance
            :type: vehicle_number: string
            :return: slot allocated

            """
        try:
            empty_slot = next((key, value) for key, value in self.total_slots.items() if not value)
            if empty_slot:
                self.total_slots[empty_slot[0]] = vehicle_number
                # To print in terminal or to write in file directly
                print(
                    'Car with vehicle registration number "{}" has been parked at slot number {}'.format(vehicle_number,

                                                                                                         empty_slot[0]),
                    file=self.file)
                # To handle test cases
                return empty_slot[0]
        except Exception as e:
            # Error Handling and print in terminal or write in file
            print('No slots available', file=self.file)

    def leaveSlot(self, slot_number):
        """
            Leave Slot

            :param: slot_number: Slot number to be emptied
            :type: slot_number: Integer
            :return: True if slot is emptied else false

            """
        try:
            if self.total_slots[slot_number] == None:
                print('Slot number {} is already vacant'.format(slot_number), file=self.file)
                pass
            vehicle_number = self.total_slots[slot_number].number
            age = self.total_slots[slot_number].age
            self.total_slots[slot_number] = None
            # To print in terminal or write in output file
            print(
                'Slot number {} vacated, the car with vehicle registration number "{}" left the space, the driver of the car was of age {}'.format(
                    slot_number, vehicle_number, age), file=self.file)
            return True
        except Exception as e:
            # Error Handling and print in terminal or write in file
            print("No slot available for the provided slot number", file=self.file)
            return False

    def get_slot_by_number(self, vehicle_number):
        """
            Get slot by vehicle number

            :param: vehicle_number: Vehicle Number to get the slot
            :type: vehicle_number: Integer
            :return: True if slot found else False

            """
        if self.total_slots.keys():
            for key, value in self.total_slots.items():
                if value and value.number == vehicle_number:
                    # To print in terminal or to write in file directly
                    print(key, file=self.file)
                    # To handle test case
                    return True
            # To handle test case
            return False
        else:
            # Error Handling and print in terminal or write in file
            print("No parking slots created yet", file=self.file)

    def get_slots_by_age(self, age):
        """
        Get slot by age

        :param: age: Age of the driver
        :type: age: Integer
        :return: True if any slot found else False

        """
        if self.total_slots.keys():
            slot_keys = []
            for key, value in self.total_slots.items():
                if value and value.age == age:
                    slot_keys.append(key)
            # To print in terminal or to write in file directly
            print(','.join([str(keys) for keys in slot_keys]), file=self.file)
            # To handle test case
            if len(slot_keys):
                return True
            else:
                return False
        else:
            # Error Handling and print in terminal or write in file
            print("No parking slots created yet", file=self.file)

    def get_vehicle_number_by_age(self, age):
        """
            Get Vehicle Number by Age

            :param: age: Driver age
            :type: age: Integer
            :return: True if vehicle found else False

            """
        if self.total_slots.keys():
            vehicle_numbers = []
            for key, value in self.total_slots.items():
                if value and value.age == age:
                    vehicle_numbers.append(value.number)
            # To print in terminal or to write in file directly
            print(','.join([str(keys) for keys in vehicle_numbers]) if len(vehicle_numbers) else "null", file=self.file)
            # To handle test cases
            if len(vehicle_numbers):
                return True
            else:
                return False
        else:
            # Error Handling and print in terminal or write in file
            print("No parking slots created yet", file=self.file)


class Vehicle:
    """
    To create vehicle instance
    """

    def __init__(self, number, age):
        self.number = number
        self.age = age

    def __str__(self):
        return "{}-{}".format(self.number, self.age)


def main():
    """
     Main function to get the commands file as input and calling the associated
    function to perform certain actions defined.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True, help="Commands File")
    args = parser.parse_args()

    if args.f:
        with open(args.f, 'r') as input_file:
            f = open("output.txt", "w+")

            # Uncomment the below statement to create ParkingSlot object and passing file to store output

            # parking = ParkingSlot(file=f)

            # creating ParkingSlot object below
            parking = ParkingSlot()

            # Calling functions on the basis of commands
            for line in iter(input_file.readline, ''):
                command = line.replace('\n', '').split(' ')
                if command[0].lower() == 'create_parking_lot':
                    parking.create_parking_lot(int(command[1]))
                elif command[0].lower() == 'park':
                    vehicle = Vehicle(command[1], int(command[3]))
                    parking.allocateSlot(vehicle)
                elif command[0].lower() == 'slot_numbers_for_driver_of_age':
                    parking.get_slots_by_age(int(command[1]))
                elif command[0].lower() == 'slot_number_for_car_with_number':
                    parking.get_slot_by_number(command[1])
                elif command[0].lower() == 'leave':
                    parking.leaveSlot(int(command[1]))
                elif command[0].lower() == 'vehicle_registration_number_for_driver_of_age':
                    parking.get_vehicle_number_by_age(int(command[1]))
                else:
                    print('Invalid Command')

                    # f.write('Invalid Command\n')

            # Close the output file
            f.close()


if __name__ == '__main__':
    main()
