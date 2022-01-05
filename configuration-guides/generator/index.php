<?php

require 'simple_html_dom.php';
require 'vendor/autoload.php';

use League\HTMLToMarkdown\HtmlConverter;

$vendor_name = 'Bluesocket';
$vendor = 'bluesocket';
$header = '# **'. $vendor . '**

---

This page explains the configuration of ' . $vendor_name . ' wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **'. $vendor_name . '**

### Access Point Configuration';

$html = file_get_html('https://support.purplewifi.net/en/support/solutions/articles/1000173127-adtran-bluesocket');

$article = '';

foreach($html->find('.markdown') as $element){
		 $article = $article . $element;
}

$converter = new HtmlConverter();
$markdown = $converter->convert($article);
$markdown = $header . '<br><br>' . $markdown;

file_put_contents($vendor . '.md', $markdown);

?>
