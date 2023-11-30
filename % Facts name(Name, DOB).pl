% Facts representing the database
dob(john, '1990-05-15').
dob(alice, '1985-10-22').
dob(bob, '1992-03-08').
dob(lisa, '1980-12-18').

% Query to retrieve the date of birth for a given name
get_dob(Name, DateOfBirth) :-
    dob(Name, DateOfBirth).