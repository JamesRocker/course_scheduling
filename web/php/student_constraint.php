<?php
        
        if (isset($_POST['constraints_data'])) {
            $new_data_json = $_POST['constraints_data'];

    
            $file_name = "../files/student_constraint.json";

            $bytes = file_put_contents($file_name, $new_data_json); 
            echo "The number of bytes written are $bytes.";
        }
        else {
            $file_name = "../files/schedule.json";

            $json_contents = file_get_contents($file_name);

            if (!$json_contents) {
                echo "error";
            }
            else {
                echo $json_contents;
            }
        }

?>
