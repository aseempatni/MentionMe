<?php
header('Content-type: application/json');

$opts = array(
    'http'=>array(
        'method'=>"GET",
        'header'=>"Accept: application/json\r\n"."Accept-language: en\r\n" .
        "Cookie: foo=bar\r\n"
    )
);

$context = stream_context_create($opts);

$url=$_GET['url'];
$tweet=$_GET['tweet'];
$url= $url.urlencode($tweet);
$json=file_get_contents($url, false, $context);
echo ($json);
?>
