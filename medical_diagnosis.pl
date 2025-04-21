symptom(flu, fever).
symptom(flu, cough).
symptom(flu, sore_throat).
symptom(flu, body_ache).

symptom(cold, cough).
symptom(cold, sneezing).
symptom(cold, sore_throat).

symptom(malaria, fever).
symptom(malaria, chills).
symptom(malaria, sweating).
symptom(malaria, headache).

% Ask the user for a symptom
ask(Symptom) :-
	write('Do you have '),
	write(Symptom),
	write('? (yes/no): '),
	read(Response),
	Response = yes.

% Diagnose by going through all symptoms for a disease
diagnose(Disease) :-
	setof(Symptom,
		symptom(Disease, Symptom),
		SymptomList),
	check_symptoms(SymptomList),
	write('Diagnosis is: '),
	write(Disease),
	nl.

% Check each symptom one by one
check_symptoms([]).
check_symptoms([Symptom|Rest]) :-
	ask(Symptom),
	check_symptoms(Rest).
