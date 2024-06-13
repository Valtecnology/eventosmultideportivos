INSERT INTO participante (nombre, apellido, edad, genero) VALUES ('mario', 'valonza', 19, 'hombre');
INSERT INTO participante (nombre, apellido, edad, genero) VALUES ('beatriz', 'doroa', 64, "mujer");

INSERT INTO evento (nombre_evento, fecha_inicio, fecha_cierre ) VALUES ('los oros', '2024-04-02', '2024-04-03');
INSERT INTO evento (nombre_evento, fecha_inicio, fecha_cierre) VALUES ('los bronce', '2023-04-02', '2023-04-03');

INSERT INTO encuentro (fecha_encuentro, hora_encuentro,`FK_Evento_id`) VALUES ('2025-11-14', '14:30:00', 2);
INSERT INTO encuentro (fecha_encuentro, hora_encuentro,`FK_Evento_id`) VALUES ('2025-12-14', '15:30:00', 2);

INSERT INTO disciplina_deportiva (nombre_disciplina, descripcion) VALUES ('tenis', 'redes y raquetas');
INSERT INTO disciplina_deportiva (nombre_disciplina, descripcion) VALUES ('futbol', 'arcos y pelotas');

select id_participante, edad, genero, nombre_disciplina from participante inner join disciplina_deportiva on participante.id_Participante = disciplina_deportiva.id_disciplina where genero = "hombre" limit 2
