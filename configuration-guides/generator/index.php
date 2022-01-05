<?php

require 'simple_html_dom.php';
require 'vendor/autoload.php';

use League\HTMLToMarkdown\HtmlConverter;

// DYNAMIC VARIABLES START
$vendor_name = 'Avaya';
$vendor = 'avaya';
$instructions_url = 'https://support.purplewifi.net/en/support/solutions/articles/1000135829-avaya';
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

$converter = new HtmlConverter();
$markdown = $converter->convert($article);
$markdown = $header . "

" . $markdown;

$markdown = str_replace('\\*insert radius\\_server\\_ip here\\*', '{{primary_ip}}', $markdown);
$markdown = str_replace('\\*insert radius\\_secret here\\*', '{{shared_secret}}', $markdown);
$markdown = str_replace('\\*insert radius\\_server2\\_ip here\\*', '{{backup_ip}}', $markdown);
$markdown = str_replace('\\*insert access\\_url here\\*', '{{splash_page_url}}', $markdown);
$markdown = str_replace('\\*insert redirect\\_url here\\*', '{{success_page_url}}', $markdown);
$markdown = str_replace('style="font-size: 13px;"', '', $markdown);
$markdown = str_replace('<span>', '', $markdown);
$markdown = str_replace('</span>', '', $markdown);
$markdown = str_replace('<div>', '', $markdown);
$markdown = str_replace('</div>', '', $markdown);
$markdown = str_replace('<div >', '', $markdown);

file_put_contents('../' . $vendor . '.md', $markdown);

?>
