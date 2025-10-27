SELECT id,
       name,
       status,
       species,
       type,
       gender,
       origin_name,
       location_name,
       image,
       url,
       created
FROM public.characters
LIMIT 1000;