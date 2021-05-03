<?php
    if (isset($_POST['data'])) {
        
        $new_data = json_decode($_POST['data']);
        //var_dump($new_data);
        // echo $arr['A'];

        $file_name = "../files/schedule.json";

        $json_contents = file_get_contents($file_name);

        if (!$json_contents) {
            // no file exist
            echo 'not exist';

            $schedule_arr = array();
            $schedule_arr[] = $new_data;
            $schedule_arr_json = json_encode($schedule_arr);
        }
        else {
            echo 'exist';

            $previous_schedule_arr = json_decode($json_contents);

            $previous_schedule_arr[] = $new_data;

            $schedule_arr_json = json_encode($previous_schedule_arr);
        }


        $bytes = file_put_contents($file_name, $schedule_arr_json); 
        echo "The number of bytes written are $bytes.";
    }
    
?>