function HW01_RAINA_Nikhil_program()
    data_table = data_analysis();
    Otsu(data_table);
end

function data_table = data_analysis()
    data_table = readtable('Mystery_Data_2195.csv', 'PreserveVariableNames', false);
    % calculates the average of all 40 values
    average = mean(data_table.Measures_MysteryUnits_);
    
    % calculates the standard deviation of all 40 values
    std_deviation = std(data_table.Measures_MysteryUnits_);
    average
    std_deviation
    
    % calculates the average of 39 values excluding the last value
    new_average = mean(data_table.Measures_MysteryUnits_(1:end-1,:));
    
    % calculates the standard deviation of 39 values excluding the last value
    new_std_deviation = std(data_table.Measures_MysteryUnits_(1:end-1,:));
    new_average
    new_std_deviation
end


function Otsu(data_table)
    norm_factor = 100;
    alpha = 1/1000;
    %Otsu's
    
    BIN_SIZE = 3;
    raw_data = data_table(:,1).Variables;
    quantized_data = floor(raw_data/BIN_SIZE)*BIN_SIZE;
    
     % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    %  CREATE AND FORM A HISTOGRAM
    %
    %  Let's form a histogram to see what it looks like:
    edges_for_the_histograms    = (BIN_SIZE/2):BIN_SIZE:50;
    centers_of_each_range       = BIN_SIZE:BIN_SIZE:48;
    [hist_counts,hist_bins]     = histcounts( quantized_data, edges_for_the_histograms );
    
    
    
    best_minimum_mixed_variance_ever = Inf;     
    best_value_yet                   = Inf;
    
    
    for counter = 1 : numel( centers_of_each_range )
        
        % Which value will we split on this time through?
        splitting_weight = centers_of_each_range(counter);

        % Find the indices of the values on the left side:
        %
        % This is a boolean variable that is 1 (or True) if this 
        % data item (i.e. this particular apple) has a weight <= the splitting_weight.
        % 
        % We set this to '1' to indicate that this item would go in the left hand group.
        %
        % Similarly for the right hand values.
        % 
        boolean_indices_of_the_left__hand_values = quantized_data <= splitting_weight;
        boolean_indices_of_the_right_hand_values = quantized_data >  splitting_weight;
        
        % Number of points in the first and second group
        num_pts_left_hand = sum(boolean_indices_of_the_left__hand_values);
        num_pts_right_hand = sum(boolean_indices_of_the_right_hand_values);
        
        % Using those boolean variables,
        % Get the actual values for the data on the left side:
        set_of_left__hand_values     = quantized_data( boolean_indices_of_the_left__hand_values );
        set_of_right_hand_values     = quantized_data( boolean_indices_of_the_right_hand_values );
        
        % What is the fraction of the data in the left hand set?
        % It is the number of elements in the left set, divided by the number of all elements:
        Wleft       = numel( set_of_left__hand_values ) / numel( quantized_data );
        Wright      = numel( set_of_right_hand_values ) / numel( quantized_data );
        
        % How mixed up are each set of data?
        % We use the Variance of the sets as a measure of how mixed up they are.
        VarianceLeft    = var( set_of_left__hand_values );
        VarianceRight   = var( set_of_right_hand_values );
        
        % Evaluate this splitting point by computing the mixed variance:
        MixedVariance(counter) = Wleft * VarianceLeft + Wright * VarianceRight;
        cost_function(counter) = MixedVariance(counter) + ((alpha * abs(num_pts_left_hand + num_pts_right_hand))/norm_factor);
        if ( cost_function(counter) < best_minimum_mixed_variance_ever )
            best_minimum_mixed_variance_ever    = cost_function(counter);
            best_value_yet                      = splitting_weight;
        end     
    end
    best_value_yet
    best_minimum_mixed_variance_ever
    
    counter = (1 : numel( centers_of_each_range ))*3;
    
    plot(counter ,MixedVariance, '-o');
    hold on;
    plot(best_value_yet, best_minimum_mixed_variance_ever, 'o');
    xlabel('Quantized Age');
    ylabel('Mixed Variance');
end