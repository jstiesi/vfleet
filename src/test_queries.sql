--capital would be a cost variable chosen from a dropdown menu
SELECT VEHICLE.VIN, Name, Vehi_type, Fuel_type, Mileage_yr, Capital 
FROM VEHICLE 
INNER JOIN COST ON VEHICLE.VIN=COST.VIN 
WHERE Capital < 20000 
ORDER BY Capital ASC;

SELECT VEHICLE.VIN, Name, Vehi_type, Fuel_type, Mileage_yr, Maintenance 
FROM VEHICLE 
INNER JOIN COST ON VEHICLE.VIN=COST.VIN 
WHERE Maintenance < 10000 
ORDER BY Maintenance ASC;

SELECT VEHICLE.VIN, Name, Vehi_type, Fuel_type, Mileage_yr, Battery 
FROM VEHICLE 
INNER JOIN COST ON VEHICLE.VIN=COST.VIN 
WHERE Battery < 500 
ORDER BY Battery ASC;

SELECT POLLUTANT.Name, Amount, VIN, VEHICLE.Name, Vehi_type, Fuel_type, Mileage_yr 
FROM VEHICLE 
INNER JOIN POLLUTANT ON VEHICLE.VIN=POLLUTANT.PVIN 
WHERE Amount < 1500 
ORDER BY Amount ASC;
