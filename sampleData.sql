-- sample_data.sql
BEGIN;

-- 1) Users (agents and renters)
INSERT INTO Users (email, name, user_type) VALUES
  ('agent1@example.com', 'Alice Agent', 'AGENT'),
  ('agent2@example.com', 'Bob Broker', 'AGENT'),
  ('renter1@example.com','Carol Renter','RENTER'),
  ('renter2@example.com','Dave Tenant','RENTER');

-- 2) Agent profiles
INSERT INTO Agent (agent_email, job_title, agency, phone_number) VALUES
  ('agent1@example.com','Senior Agent','Acme Realty','+14155550001'),
  ('agent2@example.com','Leasing Broker','Best Homes','+14155550002');

-- 3) Renter profiles
INSERT INTO Renter (renter_email, desired_move_in_date, preferred_location, budget, reward_points) VALUES
  ('renter1@example.com','2025-06-01','Downtown', 2500.00, 100),
  ('renter2@example.com','2025-07-15','Suburb',    1800.00,  50);

-- 4) Addresses (one per user)
INSERT INTO Address (user_email, city, state, zip) VALUES
  ('agent1@example.com','Chicago','IL','60601'),
  ('agent2@example.com','Evanston','IL','60201'),
  ('renter1@example.com','Chicago','IL','60602'),
  ('renter2@example.com','Skokie', 'IL','60077');

-- 5) Credit Cards (one per renter)
INSERT INTO Credit_Card (user_email, billing_address_id, card_number, expiration_date, card_type) VALUES
  ('renter1@example.com', 3, '4111111111111111', '2026-05-31', 'Visa'),
  ('renter2@example.com', 4, '5500000000000004', '2027-11-30', 'MasterCard');

-- 6) Neighborhoods
INSERT INTO Neighborhood (name, crime_rate, nearby_schools) VALUES
  ('Downtown',   5.00, 12),
  ('Suburb Hills',2.50,  5);

-- 7) Properties (with all five subtypes)

-- 7a) House
INSERT INTO Property (agent_email, address_id, neighborhood_id, rental_price, description, sq_footage, property_type)
VALUES ('agent1@example.com', 1, 1, 3200.00, 'Sunny 3-bed house','1,800','House');
INSERT INTO House    (property_id, num_rooms)
VALUES (CURRVAL('property_property_id_seq'), 3);

-- 7b) Apartment
INSERT INTO Property (agent_email, address_id, neighborhood_id, rental_price, description, sq_footage, property_type)
VALUES ('agent1@example.com', 1, 1, 2100.00, 'Modern loft apartment','1,200','Apartment');
INSERT INTO Apartment (property_id, num_rooms, building_type)
VALUES (CURRVAL('property_property_id_seq'), 2, 'Loft');

-- 7c) Commercial Building
INSERT INTO Property (agent_email, address_id, neighborhood_id, rental_price, description, sq_footage, property_type)
VALUES ('agent2@example.com', 2, 2, 5000.00, 'Downtown retail space','2,500','Commercial_Building');
INSERT INTO Commercial_Building (property_id, business_type)
VALUES (CURRVAL('property_property_id_seq'), 'Retail');

-- 7d) Vacation Home
INSERT INTO Property (agent_email, address_id, neighborhood_id, rental_price, description, sq_footage, property_type)
VALUES ('agent2@example.com', 2, 2, 4500.00, 'Lakefront cabin retreat','1,600','Vacation_Home');
INSERT INTO Vacation_Home   (property_id, max_occupancy)
VALUES (CURRVAL('property_property_id_seq'), 8);

-- 7e) Land
INSERT INTO Property (agent_email, address_id, neighborhood_id, rental_price, description, sq_footage, property_type)
VALUES ('agent1@example.com', 1, 2,   800.00, 'Undeveloped lot','10,000','Land');
INSERT INTO Land          (property_id, zoning_type)
VALUES (CURRVAL('property_property_id_seq'), 'Agricultural');

-- 8) Bookings (renter1 books the first house)
INSERT INTO Booking (booking_date, property_id, renter_email, card_id)
VALUES  (CURRENT_DATE, 1, 'renter1@example.com', 1);

COMMIT;

