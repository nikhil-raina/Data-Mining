function HW01_RAINA_Nikhil_mentor()
    file = input('Enter the csv file ', 's');
    data_set = readtable(file);
    BIN_SIZE_HT = 5;
    BIN_SIZE_AGE = 2;
    threshold_age_index = 0;
    threshold_height_index = 0;
    
    % Quantazing the data to get the Height and Age separately
    height_set = floor(data_set.Ht/BIN_SIZE_HT)*BIN_SIZE_HT;
    age_set = floor(data_set.Age/BIN_SIZE_AGE)*BIN_SIZE_AGE;
    
    % Gets the order of the classes in the csv file
    class_data = data_set.Class;
    
    height_edges = min(height_set):BIN_SIZE_HT:max(height_set);
    age_edges = min(age_set):BIN_SIZE_AGE:max(age_set);
    best_threshold_height = inf;
    best_cost_function_height = inf;
    best_threshold_age = inf;
    best_cost_function_age = inf;
    
    num_of_assam = sum(strcmp('Assam', class_data));
    num_of_bhuttan = sum(strcmp('Bhuttan', class_data));
    
    % Evaluating the threshold for the height for the csv file
    for threshold = 1 : length(height_edges)
        % Making the target value as Bhuttan and identifying all the Assams
        % in the lower group.
        false_positive =  strcmp('Assam', class_data(height_set < height_edges(threshold)));
        % Identifies all the Bhuttans in the upper group
        false_negative = strcmp('Bhuttan', class_data(height_set >= height_edges(threshold)));
        % finds the cost function
        cost_function = sum(false_positive) + sum(false_negative);
        false_positive_rate_height(threshold) = sum(false_positive) / (length(height_set) - num_of_bhuttan);
        false_negative_rate_height(threshold) = sum(false_negative) / num_of_bhuttan;
        true_positive_rate_height = 1 - false_negative_rate_height;
        if best_cost_function_height > cost_function
            threshold_height_index = threshold;
            best_threshold_height = height_edges(threshold);
            best_cost_function_height = cost_function;
        end
    end
    
    % Evaluating the threshold for age for the csv file
    for threshold = 1 : length(age_edges)
        % Making the target value as Bhuttan and identifying all the Assams
        % in the lower group.
        false_positive =  sum(strcmp('Bhuttan', class_data(age_set < age_edges(threshold))));
        % Identifies all the Bhuttans in the upper group
        false_negative = sum(strcmp('Assam', class_data(age_set >= age_edges(threshold))));
        % finds the cost function
        cost_function = false_positive + false_negative;
        false_positive_rate_age(threshold) = sum(false_positive) / (length(height_set) - num_of_bhuttan);
        false_negative_rate_age(threshold) = sum(false_negative) / num_of_bhuttan;
        true_positive_rate_age = 1 - false_negative_rate_age;
        if best_cost_function_age > cost_function
            threshold_age_index = threshold;
            best_threshold_age = age_edges(threshold);
            best_cost_function_age = cost_function;
        end
    end
    
    if best_cost_function_age < best_cost_function_height
        write_to_file(best_threshold_age, ' Age', 'The age attribute gives the lowest cost function with ', best_cost_function_age);
    else
        fprintf('The height attribute gives the lowest cost function with %d\n', best_cost_function_height);
        write_to_file(best_threshold_height, ' Height', 'The height attribute gives the lowest cost function with ', best_cost_function_height);
    end
    
    graph_ROC('Age', true_positive_rate_age, false_positive_rate_age, threshold_age_index);
    graph_ROC('Height', true_positive_rate_height, false_positive_rate_height, threshold_height_index);
end

function write_to_file(threshold, class_choice, choice_statement, cost_func)
    file = fopen('HW02_RAINA_Nikhil_trained.m', 'w');
    fprintf(file,'function HW02_RAINA_Nikhil_trained()\n');
    fprintf(file,'    trained_threshold = %d;\n', threshold);
    fprintf(file,'    trainging_data = input(''Enter the training data '', ''s'');\n');
    fprintf(file,'    fprintf(''The chosen class is %s\\n'');\n', class_choice);
    fprintf(file,'    fprintf(''%s%d\\n'');\n', choice_statement, cost_func);
    fprintf(file,'    trainging_data = readtable(trainging_data);\n');
    fprintf(file,'    for age = 1 : length(trainging_data.Age)\n');
    fprintf(file,'        if trainging_data.Age(age) < trained_threshold\n');
    fprintf(file,'            disp(''-1'')\n');
    fprintf(file,'        else\n');
    fprintf(file,'            disp(''+1'')\n');
    fprintf(file,'        end\n');
    fprintf(file,'    end\n');
    fprintf(file,'end\n');
end

% Extra points so I made the ROC curve.
% I made a general function that is called for age and height data and thus
% shows the ROC graph with the true_positive and false_positive as its
% respective axis.
function graph_ROC(title1, true_positive, false_positive, best_threshold)
    figure();
    plot(false_positive, true_positive, '.-');
    hold on;
    plot(false_positive(best_threshold), true_positive(best_threshold), 'o');
    title1 = strcat('ROC Curve for-', title1);
    title(title1, 'FontSize', 18);
    xlabel('False Alarm Rate (False Positive Rate)', 'FontSize', 14);
    ylabel('Correct Hit Rate (True Positive Rate)', 'FontSize', 14);
end
