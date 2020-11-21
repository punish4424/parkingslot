import unittest

from parkingslot import ParkingSlot, Vehicle


class TestParkingSlot(unittest.TestCase):
    """
    Test cases to check if functions are working properly
    """

    def test_create_parking_lot(self):
        parking = ParkingSlot()
        response = parking.create_parking_lot(6)
        self.assertEqual(6, response)

    def test_allocate_slot(self):
        parking = ParkingSlot()
        parking.create_parking_lot(6)
        vehicle1 = Vehicle("KA-01-HH-1234", 21)
        response = parking.allocateSlot(vehicle1)
        self.assertEqual(1, response)

    def test_leave_slot(self):
        parking = ParkingSlot()
        parking.create_parking_lot(6)
        vehicle1 = Vehicle("KA-01-HH-1234", 21)
        parking.allocateSlot(vehicle1)
        response = parking.leaveSlot(1)
        self.assertEqual(True, response)

    def test_leave_slot_2(self):
        parking = ParkingSlot()
        parking.create_parking_lot(6)
        vehicle1 = Vehicle("KA-01-HH-1234", 21)
        parking.allocateSlot(vehicle1)
        response = parking.leaveSlot(2)
        self.assertEqual(False, response)

    def test_get_slot_by_number(self):
        parking = ParkingSlot()
        parking.create_parking_lot(6)
        vehicle1 = Vehicle("KA-01-HH-1234", 21)
        vehicle2 = Vehicle("PB-01-HH-1234", 21)
        parking.allocateSlot(vehicle1)
        parking.allocateSlot(vehicle2)
        slot = parking.get_slot_by_number("PB-01-HH-1234")
        self.assertEqual(1, slot)
        self.assertNotEqual(2, slot)

    def test_get_slot_by_age(self):
        parking = ParkingSlot()
        parking.create_parking_lot(6)
        vehicle1 = Vehicle("KA-01-HH-1234", 21)
        vehicle2 = Vehicle("PB-01-HH-1234", 21)
        parking.allocateSlot(vehicle1)
        parking.allocateSlot(vehicle2)
        slot = parking.get_slots_by_age(21)
        self.assertEqual(True, slot)

    def test_get_vehicle_number_by_age(self):
        parking = ParkingSlot()
        parking.create_parking_lot(6)
        vehicle1 = Vehicle("KA-01-HH-1234", 21)
        vehicle2 = Vehicle("PB-01-HH-1234", 21)
        parking.allocateSlot(vehicle1)
        parking.allocateSlot(vehicle2)
        slot1 = parking.get_vehicle_number_by_age(21)
        slot2 = parking.get_vehicle_number_by_age(18)
        self.assertEqual(True, slot1)
        self.assertNotEqual(True, slot2)


if __name__ == '__main__':
    unittest.main()
