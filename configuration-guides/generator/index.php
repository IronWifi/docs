<?php

require 'simple_html_dom.php';
require 'vendor/autoload.php';

use League\HTMLToMarkdown\HtmlConverter;

// DYNAMIC VARIABLES START
$vendor_name = 'Bluesocket';
$vendor = 'bluesocket';
$instructions_url = 'https://support.purplewifi.net/en/support/solutions/articles/1000173127-adtran-bluesocket';
// DYNAMIC VARIABLES END

$header = '# **'. $vendor_name . '**

---

This page explains the configuration of ' . $vendor_name . ' wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **'. $vendor_name . '**

### Access Point Configuration';

$html = file_get_html($instructions_url);

$article = '';

foreach($html->find('.markdown') as $element){
					$article = $article . $element;
}

$article = str_replace('<div class="article__body markdown" itemprop="articleBody">', '', $article);
$article = str_replace('</div>', '', $article);

$article = str_replace('*insert radius_server_ip here*', '{{primary_ip}}', $article);
$article = str_replace('*insert radius_secret here*', '{{shared_secret}}', $article);
$article = str_replace('*insert radius_server2_ip here*', '{{backup_ip}}', $article);
$article = str_replace('*insert access_url here*', '{{splash_page_url}}', $article);
$article = str_replace('*insert redirect_url here*', '{{success_page_url}}', $article);

$converter = new HtmlConverter();
$markdown = $converter->convert($article);
$markdown = $header . "

" . $markdown;

file_put_contents('../' . $vendor . '.md', $markdown);

?>
