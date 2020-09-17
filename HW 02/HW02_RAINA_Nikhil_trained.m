function HW02_RAINA_Nikhil_trained()
    trained_threshold = 44;
    trainging_data = input('Enter the training data ', 's');
    fprintf('The chosen class is  Age\n');
    fprintf('The age attribute gives the lowest cost function with 170\n');
    trainging_data = readtable(trainging_data);
    for age = 1 : length(trainging_data.Age)
        if trainging_data.Age(age) < trained_threshold
            disp('-1')
        else
            disp('+1')
        end
    end
end
