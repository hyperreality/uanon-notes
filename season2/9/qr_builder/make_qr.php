<HTML>
<BODY>

<?php

$bits = "000000010111100101111010110000000011111010110000010101101110111110010001010011010110001000110100010010001010001011111001111010100010010001011001011111011000110100010011111010001111100000111010111110000000010101010101010101010000000111111111100101000000010011111111001100011101001110110001011010000111001111111100100011111100011001000110000001111101111010100000001000011110011010110111001111101110001011011110100000101010110101110110100100101011110011100111010011010001010000000011110100001010001100110110100101000111010110001100100101011001001110100000010100110010111111111100100011100111011011110001001001111101011100011010101101000110011010110011001011001100111011001000100010111001110100100000111110111011111111100111011001110000011100000011011110110100001110111110100101010010001110001110001111001001001010100000000001111111111110001100000111101011100001000000011001111000111111010100101011111010011010010010001011101110010001010000100110100001000001110010001011001011000011011010100011010001011110000000110101010101011011111010000101000001000101000111000000010111001000101010010010110";

for ($x = 0; $x <= 32; $x++) {
    for ($y = 0; $y <= 32; $y++) {
        $idx = (33*$y) + $x;

        $ch = substr($bits,$idx,1);
        if ($ch == "0") {
            echo '<IMG SRC="bl.png" WIDTH=8 HEIGHT=8>';
        } elseif ($ch == "1") {
            echo '<IMG SRC="wh.png" WIDTH=8 HEIGHT=8>';
        }
    } 
    echo '<br>';
} 

?>

</BODY>
</HTML>
