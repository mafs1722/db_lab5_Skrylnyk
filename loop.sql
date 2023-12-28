DO $$
BEGIN
    FOR i IN 1..10 LOOP
    	INSERT INTO ProductionStudios (StudioID, StudioName, Country, YearFounded) VALUES (i, 'StudioName' || i, 'Country' || i, '2023.12.28');
    END LOOP;
END $$;

-- select * from ProductionStudios;
-- delete from ProductionStudios;
-- select * from ProductionStudios;