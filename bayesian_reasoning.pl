% Prior probabilities for weather conditions
prior(sunny, 0.5).
prior(rainy, 0.3).
prior(cloudy, 0.2).

% Conditional probabilities of evidence given weather condition
evidence_prob(cloudy, sunny, 0.2).
evidence_prob(cloudy, rainy, 0.7).
evidence_prob(cloudy, cloudy, 0.9).
evidence_prob(humidity, sunny, 0.3).
evidence_prob(humidity, rainy, 0.8).
evidence_prob(humidity, cloudy, 0.6).

% Bayesian inference for weather prediction
bayes(Weather, Evidence, Posterior) :-
    prior(Weather, Prior),
    evidence_prob(Evidence, Weather, GivenProb),
    Posterior is Prior * GivenProb.

% Initialization directive
:- initialization(main).

main :-
    bayes(sunny, cloudy, P),
    write('Posterior probability: '), write(P), nl.
