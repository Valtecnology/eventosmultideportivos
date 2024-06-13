
select id_participante, edad, genero, nombre_disciplina from participante inner join disciplina_deportiva on participante.id_Participante = disciplina_deportiva.id_disciplina where genero = "hombre" limit 2

select * from eventos

select * from participante where edad between 10 and 50