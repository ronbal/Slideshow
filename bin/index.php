<?php

require_once 'Config/Lite.php';

$config = new Config_Lite('/home/pi/app/settings.ini');

$TMDELAY           = $config->get('slideshow_settings', 'TMDELAY');
$FADE_TM           = $config->get('slideshow_settings', 'FADE_TM');
$NEWDELAY          = $config->get('slideshow_settings', 'NEWDELAY');
$ADDELAY           = $config->get('slideshow_settings', 'ADDELAY');
$Advertisment      = $config->get('slideshow_settings', 'Advertisment');
$AdCounter         = $config->get('slideshow_settings', 'AdCounter');
$ForceAdvertisment = $config->get('slideshow_settings', 'ForceAdvertisment');
$Skip_IP_Check     = $config->get('startup_setting', 'Skip_IP_Check');
$Ignore_USB_Stick  = $config->get('startup_setting', 'Ignore_USB_Stick');


   if(isset($_POST['BtnSubmit']))   
   {  
      $TMDELAY=$_POST['TMDELAY'];
      $FADE_TM=$_POST['FADE_TM'];
      $NEWDELAY=$_POST['NEWDELAY'];
      $ADDELAY=$_POST['ADDELAY'];
      $AdCounter=$_POST['AdCounter'];
      $Skip_IP_Check=$_POST['Skip_IP_Check'];
      if(isset($Skip_IP_Check) === false){$Skip_IP_Check = "False";}else{$Skip_IP_Check="True";}
      $Ignore_USB_Stick=$_POST['Ignore_USB_Stick'];
      if(isset($Ignore_USB_Stick) === false){$Ignore_USB_Stick = "False";}else{$Ignore_USB_Stick="True";}
      $Advertisment=$_POST['Advertisment'];
      if(isset($Advertisment) === false){$Advertisment = "False";}else{$Advertisment="True";}
      $ForceAdvertisment=$_POST['ForceAdvertisment'];
      if(isset($ForceAdvertisment) === false){$ForceAdvertisment = "False";}else{$ForceAdvertisment="True";}
      $config->set('slideshow_settings', 'TMDELAY', $TMDELAY);
      $config->set('slideshow_settings', 'FADE_TM', $FADE_TM);
      $config->set('slideshow_settings', 'NEWDELAY', $NEWDELAY);
      $config->set('slideshow_settings', 'ADDELAY', $ADDELAY);
      $config->set('slideshow_settings', 'AdCounter', $AdCounter);
      $config->set('slideshow_settings', 'Advertisment', $Advertisment);
      $config->set('slideshow_settings', 'ForceAdvertisment', $ForceAdvertisment);
      $config->set('startup_setting', 'Skip_IP_Check', $Skip_IP_Check);
      $config->set('startup_setting', 'Ignore_USB_Stick', $Ignore_USB_Stick);
      $config->save();
      header("Refresh:0");
   }

?>




<h2>External Slideshow Settings</h2>

<form name="UserInformationForm" method="POST" action="#">
<h3>Time settings</h3>

      Picture playback time:
      <input name="TMDELAY" type="number" style="width: 50px" value="<?php echo $TMDELAY; ?>"><br/><br/>
      Picture fade time:
      <input name="FADE_TM" type="number" style="width: 50px" value="<?php echo $FADE_TM; ?>"><br/><br/>
      New picture additional delay:
      <input name="NEWDELAY" type="number" style="width: 50px" value="<?php echo $NEWDELAY; ?>"><br/><br/>
      Advertisment additional delay:
      <input name="ADDELAY" type="number" style="width: 50px" value="<?php echo $ADDELAY; ?>"><br/><br/>
<hr>  
<h3>
      Advertisment settings</h3>
      <input name="Advertisment" type="checkbox" value="1" <?php if ($Advertisment == 1){?> checked="checked" <?php } ?>/>
      Show Advertisments    
      <br>
      <input name="ForceAdvertisment" type="checkbox" value="1" <?php if ($ForceAdvertisment == 1){?> checked="checked" <?php } ?>/>
      Force Advertisments over new pictures
      <br>
      Number of pictures until ad is shown:
      <input name="AdCounter" type="number" style="width: 50px" value="<?php echo $AdCounter; ?>"><br/><br/> 
<hr>
<h3>Advanced settings</h3>
   Reboot of pi required to apply changes<br>
<br>
      <input name="Skip_IP_Check" type="checkbox" value="1" <?php if ($Skip_IP_Check == 1){?> checked="checked" <?php } ?>/>
      Skip IP check on startup
      <br>
      <input name="Ignore_USB_Stick" type="checkbox" value="1" <?php if ($Ignore_USB_Stick == 1){?> checked="checked" <?php } ?>/>
      Skip USB-Stick check<br>
      <br>
      <hr>
      <input name="BtnSubmit" type="submit" value="Submit">
      <br/>
</form>
