import random
import math


class Station:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def calculate_distance(self, drone_x, drone_y):
        # İstasyon ile belirli bir drone arasındaki mesafeyi hesapla
        return math.sqrt((self.x - drone_x) ** 2 + (self.y - drone_y) ** 2)


class Drone:
    def __init__(self, model, transmissionConsp, receiveConsp, sleepConsp, idleConsp, maxAltitude, maxSpeed):
        self.model = model
        self.transmissionConsp = transmissionConsp
        self.receiveConsp = receiveConsp
        self.sleepConsp = sleepConsp
        self.idleConsp = idleConsp
        self.maxAltitude = maxAltitude
        self.maxSpeed = maxSpeed


def generate_stations(num_stations, area_size):
    stations = []
    for i in range(num_stations):
        station_name = f"k{i + 1}"
        station_x = random.uniform(0, area_size)  # Rastgele x koordinatı (0-area_size arasında)
        station_y = random.uniform(0, area_size)  # Rastgele y koordinatı (0-area_size arasında)
        stations.append(Station(station_name, station_x, station_y))
    return stations


def calculate_energy_consumption(self):
        # Saniyeler cinsinden zamanı alır ve enerji tüketimini hesaplar
        total_consp = self.transmitConsp + self.receiveConsp + self.sleepConsp
        energy_consumption = total_consp * 100
        return energy_consumption



num_drones = 6
def generate_drones(num_drones):
    drone_models = [
        {"name": "DJI Mavic Air 2", "transmissionConsp": 2.5, "receiveConsp": 2.0, "sleepConsp": 0.5, "idleConsp": 1.0, "maxAltitude": 5000, "maxSpeed": 68},
        {"name": "Parrot Anafi", "transmissionConsp": 2.0, "receiveConsp": 1.5, "sleepConsp": 0.7, "idleConsp": 0.9, "maxAltitude": 4500, "maxSpeed": 55},
        {"name": "Skydio 2", "transmissionConsp": 2.2, "receiveConsp": 1.8, "sleepConsp": 0.8, "idleConsp": 1.2, "maxAltitude": 3000, "maxSpeed": 58},
        {"name": "DJI Phantom 4 Pro", "transmissionConsp": 3.0, "receiveConsp": 2.5, "sleepConsp": 1.0, "idleConsp": 1.5, "maxAltitude": 6000, "maxSpeed": 72},
        {"name": "Autel Robotics EVO 2", "transmissionConsp": 2.5, "receiveConsp": 2.0, "sleepConsp": 0.7, "idleConsp": 1.2, "maxAltitude": 7000, "maxSpeed": 72},
        {"name": "Yuunec Typhoon H Pro", "transmissionConsp": 2.2, "receiveConsp": 1.8, "sleepConsp": 0.8, "idleConsp": 1.2, "maxAltitude": 5000, "maxSpeed": 70}
    ]

    drones = []
    for i in range(num_drones):
        for model_data in drone_models:
            model = model_data["name"]
            transmissionConsp = model_data["transmissionConsp"]
            receiveConsp = model_data["receiveConsp"]
            sleepConsp = model_data["sleepConsp"]
            idleConsp = model_data["idleConsp"]
            maxAltitude = model_data["maxAltitude"]
            maxSpeed = model_data["maxSpeed"]
            drones.append(Drone(model, transmissionConsp, receiveConsp, sleepConsp, idleConsp, maxAltitude, maxSpeed))
    return drones


def assign_stations_to_drones(stations, drones):
    assigned_stations = {station.name: [] for station in stations}

    # Her bir drone için istasyonları sırala ve atanacak istasyonları belirle
    for drone in drones:
        sorted_stations = sorted(stations,
                                 key=lambda s: s.calculate_distance(random.uniform(0, 100), random.uniform(0, 100)))
        for station in sorted_stations:
            assigned_stations[station.name].append((drone, drone.battery_life))
            break  # En yakın istasyona atandıktan sonra döngüden çık
    return assigned_stations


if __name__ == "__main__":
    # İstasyon sayısı
    num_stations = 5

    # Alan boyutu
    area_size = 100

    # Drone konumlarını oluştur
    drones = generate_drones(num_drones)

    # İstasyonları oluştur
    stations = generate_stations(num_stations, area_size)

    # İstasyonları dronelara ata
    assigned_stations = assign_stations_to_drones(stations, drones)

    # Atanan istasyonları ve diğer istasyonların sıralamasını yazdır
    for station_name, drone_info in assigned_stations.items():
        if drone_info:
            sorted_drones = sorted(drone_info, key=lambda x: x[1])
            lowest_energy_drone = sorted_drones[0][0]
            print(
                f"{station_name} istasyon önceliği: {', '.join(drone.brand + '-' + drone.model for drone, _ in drone_info)} - En düşük enerjili drone: {lowest_energy_drone.brand}-{lowest_energy_drone.model}")
            for drone, energy in sorted_drones:
                print(
                    f"{drone.brand}-{drone.model}: Enerji seviyesi: {energy}")
        else:
            print(f"{station_name} istasyonu hiçbir drone'a atanmadı.")
