-- Script to create the ComputeAverageWeightedScoreForUser stored procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN in_user_id INT)
BEGIN
    -- Declare variables to hold sums and weighted scores
    DECLARE total_weight INT DEFAULT 0;
    DECLARE weighted_score_sum FLOAT DEFAULT 0.0;

    -- Calculate the total weighted score and total weight for the specified user
    SELECT 
        SUM(c.score * p.weight) INTO weighted_score_sum,
        SUM(p.weight) INTO total_weight
    FROM 
        corrections c
    JOIN 
        projects p ON c.project_id = p.id
    WHERE 
        c.user_id = in_user_id;

    -- Check for division by zero
    IF total_weight = 0 THEN
        SET total_weight = 1; -- Prevent division by zero, alternative handling could be necessary
    END IF;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = (weighted_score_sum / total_weight)
    WHERE id = in_user_id;
END$$

DELIMITER ;
