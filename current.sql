-- 0) Reusable domains for consistency
CREATE DOMAIN phone_number AS VARCHAR(16)
  CHECK ( VALUE ~ '^\+[1-9]\d{1,14}$' );

CREATE DOMAIN card_number AS CHAR(16)
  CHECK ( VALUE ~ '^\d{13,16}$' );

CREATE DOMAIN card_type AS VARCHAR(10)
  CHECK ( VALUE IN ('Visa','MasterCard','Amex','Discover') );

-------------------------------------------------------------------------------
CREATE TABLE Users (
  email      VARCHAR(100) PRIMARY KEY,
  name       VARCHAR(100) NOT NULL,
  user_type  VARCHAR(6)   NOT NULL
               CHECK (user_type IN ('AGENT','RENTER'))
);

-------------------------------------------------------------------------------
CREATE TABLE Agent (
  agent_email   VARCHAR(100) PRIMARY KEY
                   REFERENCES Users(email)
                   ON DELETE CASCADE,
  job_title     VARCHAR(100) NOT NULL,
  agency        VARCHAR(100) NOT NULL,
  phone_number  phone_number   NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE Renter (
  renter_email          VARCHAR(100) PRIMARY KEY
                           REFERENCES Users(email)
                           ON DELETE CASCADE,
  desired_move_in_date  DATE         NOT NULL,
  preferred_location    VARCHAR(100) NOT NULL,
  budget                DECIMAL(12,2),
  reward_points         INT          NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE Address (
  address_id  SERIAL PRIMARY KEY,
  user_email  VARCHAR(100) UNIQUE NOT NULL
                REFERENCES Users(email)
                ON DELETE CASCADE,
  city        VARCHAR(50)  NOT NULL,
  state       VARCHAR(50)  NOT NULL,
  zip         VARCHAR(10)  NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE Credit_Card (
  card_id            SERIAL PRIMARY KEY,
  user_email         VARCHAR(100) NOT NULL
                       REFERENCES Users(email)
                       ON DELETE CASCADE,
  billing_address_id INT         NOT NULL
                       REFERENCES Address(address_id)
                       ON DELETE SET NULL,
  card_number        card_number NOT NULL UNIQUE,
  expiration_date    DATE        NOT NULL,
  card_type          card_type   NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE Neighborhood (
  neighborhood_id  SERIAL PRIMARY KEY,
  name             VARCHAR(100) NOT NULL,
  crime_rate       DECIMAL(4,2) NOT NULL,
  nearby_schools   INT          NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE Property (
  property_id     SERIAL PRIMARY KEY,
  agent_email     VARCHAR(100)
                   REFERENCES Agent(agent_email)
                   ON DELETE SET NULL,
  address_id      INT       NOT NULL
                   REFERENCES Address(address_id)
                   ON DELETE RESTRICT,
  neighborhood_id INT
                   REFERENCES Neighborhood(neighborhood_id)
                   ON DELETE SET NULL,
  rental_price    DECIMAL(12,2),
  description     TEXT,
  availability    BOOLEAN  NOT NULL DEFAULT TRUE,
  sq_footage      INT      NOT NULL,
  property_type   VARCHAR(30) NOT NULL
                   CHECK (property_type IN (
                     'House','Apartment',
                     'Commercial_Building',
                     'Vacation_Home','Land'
                   ))
);

-------------------------------------------------------------------------------
CREATE TABLE House (
  property_id  INT PRIMARY KEY
                  REFERENCES Property(property_id)
                  ON DELETE CASCADE,
  num_rooms    INT NOT NULL
);

CREATE TABLE Apartment (
  property_id   INT PRIMARY KEY
                   REFERENCES Property(property_id)
                   ON DELETE CASCADE,
  num_rooms     INT NOT NULL,
  building_type VARCHAR(100) NOT NULL
);

CREATE TABLE Commercial_Building (
  property_id   INT PRIMARY KEY
                   REFERENCES Property(property_id)
                   ON DELETE CASCADE,
  business_type VARCHAR(100) NOT NULL
);

CREATE TABLE Vacation_Home (
  property_id   INT PRIMARY KEY
                   REFERENCES Property(property_id)
                   ON DELETE CASCADE,
  max_occupancy INT NOT NULL
);

CREATE TABLE Land (
  property_id   INT PRIMARY KEY
                   REFERENCES Property(property_id)
                   ON DELETE CASCADE,
  zoning_type   VARCHAR(100) NOT NULL
);

-------------------------------------------------------------------------------
CREATE TABLE Booking (
  booking_id     SERIAL PRIMARY KEY,
  booking_date   DATE        NOT NULL,
  property_id    INT         NOT NULL
                   REFERENCES Property(property_id)
                   ON DELETE CASCADE,
  renter_email   VARCHAR(100) NOT NULL
                   REFERENCES Renter(renter_email)
                   ON DELETE CASCADE,
  card_id        INT         NOT NULL
                   REFERENCES Credit_Card(card_id)
                   ON DELETE RESTRICT
);











