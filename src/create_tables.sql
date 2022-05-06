CREATE TABLE VEHICLE( 
VIN integer PRIMARY KEY, 
Name varchar(50), 
Vehi_type varchar(50), 
Fuel_type varchar(50), 
Mileage_yr integer
);

CREATE TABLE COST( 
VIN integer PRIMARY KEY, 
Capital integer, 
Depreciation integer, 
Fuel integer, 
Maintenance integer, 
Repair integer, 
Tire integer, 
Battery integer, 
Insurance integer, 
FOREIGN KEY (VIN) 
REFERENCES VEHICLE (VIN) MATCH FULL
);

CREATE TABLE FIN_INCENT( 
VIN integer PRIMARY KEY, 
Financial_incentives integer, 
FOREIGN KEY (VIN) 
REFERENCES VEHICLE (VIN) MATCH FULL
);

CREATE TABLE POLLUTANT( 
PVIN integer PRIMARY KEY,
Name varchar(50), 
Amount integer, 
FOREIGN KEY (PVIN) 
REFERENCES VEHICLE (VIN) MATCH FULL
);
