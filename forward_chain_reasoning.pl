% --- Knowledge base of diseases and their associated symptoms ---

rule(flu, [fever, cough, sore_throat, body_ache]).
rule(cold, [cough, sneezing, sore_throat]).
rule(malaria, [fever, chills, sweating, headache]).
rule(typhoid, [fever, headache, abdominal_pain, constipation]).
rule(dengue, [fever, rash, joint_pain, headache]).

% --- Entry point for diagnosis ---

start_diagnosis :-
	write('Enter your symptoms as a list (e.g. [fever, cough]): '),
	nl,
	read(Symptoms),
	(find_diagnosis(Symptoms) ->
	true;
	write('No exact match found in the knowledge base.'),
		nl).

% --- Forward Chaining reasoning:
% Check each rule, if all its symptoms are present in user's symptoms, confirm disease ---

find_diagnosis(Symptoms) :-
	rule(Disease, DiseaseSymptoms),
	all_symptoms_present(DiseaseSymptoms, Symptoms),
	write('Diagnosis: '),
	write(Disease),
	nl.

% --- Utility predicate: check if all symptoms in DiseaseSymptoms exist in UserSymptoms ---

all_symptoms_present([], _).
all_symptoms_present([Symptom|Rest], UserSymptoms) :-
	member(Symptom, UserSymptoms),
	all_symptoms_present(Rest, UserSymptoms).
