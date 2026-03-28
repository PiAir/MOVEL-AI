<?php
// xapi-proxy.php
// --- STAP 0: endpoint en secret ---
$lrs_endpoint = 'YOUR-LRS-URL';
$lrs_key    = 'YOUR-LRS-KEY';
$lrs_secret = 'YOUR-LRS-SECRET';

// --- STAP 1: CORS & Domein Check ---
$allowed_origins = [
    "YOUR-ORIGIN(s)" 
];

$origin = $_SERVER['HTTP_ORIGIN'] ?? '';

if (in_array($origin, $allowed_origins)) {
    header("Access-Control-Allow-Origin: $origin");
    header("Access-Control-Allow-Methods: POST, OPTIONS");
    header("Access-Control-Allow-Headers: Content-Type, X-Quarto-Proxy-Key");
} else {
    http_response_code(403);
    die("Toegang geweigerd: Origin niet toegestaan.");
}

// Handel 'Preflight' verzoeken van de browser af
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    exit;
}

// --- STAP 2: Extra Check (Optioneel maar aangeraden) ---
// Controleer of een geheime sleutel wordt meegestuurd die alleen jouw build kent
// Deze moet je in je .js meegeven
$proxy_key = "YOUR-PROXY-KEY"; 
if (($_SERVER['HTTP_X_QUARTO_PROXY_KEY'] ?? '') !== $proxy_key) {
    http_response_code(401);
    die("Ongeldige Proxy Key.");
}

// --- STAP 3: Anonimiseren & Doorsturen (zoals eerder) ---
$salt = "LANGE-GEHEIME-SALT-VOOR-HET-HASHEN-VAN-IP-ADRESSEN";
$anonymous_id = hash('sha256', $_SERVER['REMOTE_ADDR'] . $salt);

$json_str = file_get_contents('php://input');
if (!$json_str) {
    http_response_code(400);
    die('Geen data ontvangen');
}
$statement = json_decode($json_str, true);

// Forceer de actor naar de anonieme versie
$statement['actor'] = [
    "account" => [ "homePage" => $origin, "name" => $anonymous_id ],
    "objectType" => "Agent"
];

$payload = json_encode($statement);

// 4. Verstuur naar SQL LRS 
// Initialiseer cURL naar SQL LRS
$ch = curl_init($lrs_endpoint);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'X-Experience-API-Version: 1.0.3',
    'Authorization: Basic ' . base64_encode($lrs_key . ':' . $lrs_secret)
]);

$response = curl_exec($ch);
$status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

http_response_code($status);
echo $response;

?>