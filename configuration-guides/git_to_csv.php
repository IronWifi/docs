<?php

$dir = '/Users/peterutekal/Documents/IronWifi/docs/configuration-guides';

if(!is_dir($dir)){
				exit('Invalid Directory');
}


$files = array();

foreach(scandir($dir) as $file){
				if($file !== '.' && $file !== '..'){
								$files[] = $file;
				}
}

var_dump($files);

?>
