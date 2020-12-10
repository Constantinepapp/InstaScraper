import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3

sender_email = "*****"
password = "********"

message = MIMEMultipart("alternative")
message["Subject"] = "Leading pace Running analysis and metrics web app"
message["From"] = sender_email



def select_all_emails():
    conn=sqlite3.connect("profiles.db")
    cur = conn.cursor()
    cur.execute("SELECT email FROM profiles WHERE status='scraped'")
    rows = cur.fetchall()
    conn.close()
    return (rows)

def update(email):
    conn=sqlite3.connect("profiles.db")
    cur=conn.cursor()
    cur.execute("UPDATE profiles SET status='one_sent' WHERE email=?",(email,))
    conn.commit()
    conn.close()
# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
<!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width" name="viewport"/>
<!--[if !mso]><!-->
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<!--<![endif]-->
<title></title>
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css"/>
<!--<![endif]-->
<style type="text/css">
		body {
			margin: 0;
			padding: 0;
		}

		table,
		td,
		tr {
			vertical-align: top;
			border-collapse: collapse;
		}

		* {
			line-height: inherit;
		}

		a[x-apple-data-detectors=true] {
			color: inherit !important;
			text-decoration: none !important;
		}
	</style>
<style id="media-query" type="text/css">
		@media (max-width: 660px) {

			.block-grid,
			.col {
				min-width: 320px !important;
				max-width: 100% !important;
				display: block !important;
			}

			.block-grid {
				width: 100% !important;
			}

			.col {
				width: 100% !important;
			}

			.col_cont {
				margin: 0 auto;
			}

			img.fullwidth,
			img.fullwidthOnMobile {
				max-width: 100% !important;
			}

			.no-stack .col {
				min-width: 0 !important;
				display: table-cell !important;
			}

			.no-stack.two-up .col {
				width: 50% !important;
			}

			.no-stack .col.num2 {
				width: 16.6% !important;
			}

			.no-stack .col.num3 {
				width: 25% !important;
			}

			.no-stack .col.num4 {
				width: 33% !important;
			}

			.no-stack .col.num5 {
				width: 41.6% !important;
			}

			.no-stack .col.num6 {
				width: 50% !important;
			}

			.no-stack .col.num7 {
				width: 58.3% !important;
			}

			.no-stack .col.num8 {
				width: 66.6% !important;
			}

			.no-stack .col.num9 {
				width: 75% !important;
			}

			.no-stack .col.num10 {
				width: 83.3% !important;
			}

			.video-block {
				max-width: none !important;
			}

			.mobile_hide {
				min-height: 0px;
				max-height: 0px;
				max-width: 0px;
				display: none;
				overflow: hidden;
				font-size: 0px;
			}

			.desktop_hide {
				display: block !important;
				max-height: none !important;
			}
		}
	</style>
</head>
<body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #e6e9ec;">
<!--[if IE]><div class="ie-browser"><![endif]-->
<table bgcolor="#e6e9ec" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="table-layout: fixed; vertical-align: top; min-width: 320px; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #e6e9ec; width: 100%;" valign="top" width="100%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td style="word-break: break-word; vertical-align: top;" valign="top">
<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#e6e9ec"><![endif]-->
<div style="background-color:transparent;">
<div class="block-grid" style="min-width: 320px; max-width: 640px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: #10100e;">
<div style="border-collapse: collapse;display: table;width: 100%;background-color:#10100e;background-image:url('https://i.ibb.co/rmgM9Kt/flare.png');background-position:top center;background-repeat:no-repeat">
<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" style="background-color:#10100e"><![endif]-->
<!--[if (mso)|(IE)]><td align="center" width="640" style="background-color:#10100e;width:640px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:0px; padding-bottom:0px;"><![endif]-->
<div class="col num12" style="min-width: 320px; max-width: 640px; display: table-cell; vertical-align: top; width: 640px;">
<div class="col_cont" style="width:100% !important;">
<!--[if (!mso)&(!IE)]><!-->
<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:0px; padding-bottom:0px; padding-right: 0px; padding-left: 0px;">
<!--<![endif]-->
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
<div style="color:#ffffff;font-family:'Roboto', Tahoma, Verdana, Segoe, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
<div style="line-height: 1.2; font-size: 12px; font-family: 'Roboto', Tahoma, Verdana, Segoe, sans-serif; color: #ffffff; mso-line-height-alt: 14px;">
<p style="font-size: 26px; line-height: 1.2; word-break: break-word; text-align: center; font-family: Roboto, Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 31px; margin: 0;"><span style="font-size: 26px;"><strong><span style="color: #e03add;"> </span></strong></span></p>
</div>
</div>
<!--[if mso]></td></tr></table><![endif]-->
<table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
<table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="10" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 10px; width: 100%;" valign="top" width="100%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td height="10" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>




<div align="center" class="img-container center fixedwidth" style="padding-right: 0px;padding-left: 0px;">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]--><img align="center" alt="Alternate text" border="0" class="center fixedwidth" src="https://i.ibb.co/TH7z4y6/logo2.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 480px; display: block;" title="Alternate text" width="480"/>
<!--[if mso]></td></tr></table><![endif]-->
</div>
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
<!--[if mso]></td></tr></table><![endif]-->
<div align="center" class="img-container center fixedwidth" style="padding-right: 0px;padding-left: 0px; margin-top: 10px;">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]--><a href="leadingpace.netlify.app" style="outline:none" tabindex="-1" target="_blank"> <img align="center" alt="Alternate text" border="0" class="center fixedwidth" src="https://i.ibb.co/ykxzm2p/2020-10-25-4-1.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 512px; display: block;" title="Alternate text" width="512"/></a>
<!--[if mso]></td></tr></table><![endif]-->
</div>
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 20px; padding-bottom: 10px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
<div style="color:#ffffff;font-family:'Roboto', Tahoma, Verdana, Segoe, sans-serif;line-height:1.2;padding-top:20px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
<div style="line-height: 1.2; font-size: 12px; font-family: 'Roboto', Tahoma, Verdana, Segoe, sans-serif; color: #ffffff; mso-line-height-alt: 14px;">
<p style="font-size: 30px; line-height: 1.2; word-break: break-word; text-align: center; font-family: Roboto, Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 36px; margin: 0;"><span style="font-size: 30px;"><strong>It's Free, sign up today!</strong></span></p>
</div>
</div>
<!--[if mso]></td></tr></table><![endif]-->
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 25px; padding-left: 25px; padding-top: 10px; padding-bottom: 20px; font-family: Arial, sans-serif"><![endif]-->
<div style="color:#555555;font-family:Nunito, Arial, Helvetica Neue, Helvetica, sans-serif;line-height:1.5;padding-top:10px;padding-right:25px;padding-bottom:20px;padding-left:25px;">
<div style="line-height: 1.5; font-size: 12px; color: #555555; font-family: Nunito, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 18px;">
<p style="font-size: 16px; line-height: 1.5; word-break: break-word; text-align: center; mso-line-height-alt: 24px; margin: 0;"><span style="color: #ffffff; font-size: 16px;">Leading pace is a running analytics web app, Estimates your aerobic fitness and generates a 100% free personalized program for you</span></p>
</div>
</div>
<!--[if mso]></td></tr></table><![endif]-->
<div align="center" class="button-container" style="padding-top:10px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-top: 10px; padding-right: 10px; padding-bottom: 20px; padding-left: 10px" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="leadingpace.netlify.app" style="height:46.5pt; width:156.75pt; v-text-anchor:middle;" arcsize="18%" stroke="false" fillcolor="#303030"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:Arial, sans-serif; font-size:24px"><![endif]--><a href="leadingpace.netlify.app" style="-webkit-text-size-adjust: none; text-decoration: none; display: inline-block; color: #ffffff; background-color: #303030; border-radius: 11px; -webkit-border-radius: 11px; -moz-border-radius: 11px; width: auto; width: auto; border-top: 0px solid #2B79A6; border-right: 0px solid #2B79A6; border-bottom: 4px solid #7F7F7F; border-left: 0px solid #2B79A6; padding-top: 5px; padding-bottom: 5px; font-family: Nunito, Arial, Helvetica Neue, Helvetica, sans-serif; text-align: center; mso-border-alt: none; word-break: keep-all;" target="_blank"><span style="padding-left:20px;padding-right:20px;font-size:24px;display:inline-block;"><span style="font-size: 16px; line-height: 2; word-break: break-word; mso-line-height-alt: 32px;"><strong><span data-mce-style="font-size: 24px; line-height: 48px;" style="font-size: 24px; line-height: 48px;">Learn More</span></strong></span></span></a>
<!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->
</div>
<!--[if (!mso)&(!IE)]><!-->
</div>
<!--<![endif]-->
</div>
</div>
<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
<!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
</div>
</div>
</div>
<div style="background-color:transparent;">
<div class="block-grid four-up" style="min-width: 320px; max-width: 640px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: #0f0f0f;">
<div style="border-collapse: collapse;display: table;width: 100%;background-color:#0f0f0f;">
<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" style="background-color:#0f0f0f"><![endif]-->
<!--[if (mso)|(IE)]><td align="center" width="160" style="background-color:#0f0f0f;width:160px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
<div class="col num3" style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 159px; width: 160px;">
<div class="col_cont" style="width:100% !important;">
<!--[if (!mso)&(!IE)]><!-->
<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
<!--<![endif]-->
<div align="center" class="img-container center fixedwidth" style="padding-right: 0px;padding-left: 0px;">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]-->
<div style="font-size:1px;line-height:15px"> </div><img align="center" alt="Alternate text" border="0" class="center fixedwidth" src="https://i.ibb.co/sw6pz1H/medical-report.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 88px; display: block;" title="Alternate text" width="88"/>
<!--[if mso]></td></tr></table><![endif]-->
</div>
<table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
<table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #DCDCDC; width: 70%;" valign="top" width="70%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 5px; padding-bottom: 20px; font-family: Arial, sans-serif"><![endif]-->
<div style="color:#ffffff;font-family:Nunito, Arial, Helvetica Neue, Helvetica, sans-serif;line-height:1.5;padding-top:5px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
<div style="line-height: 1.5; font-size: 12px; color: #ffffff; font-family: Nunito, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 18px;">
<p style="font-size: 12px; line-height: 1.5; word-break: break-word; text-align: center; mso-line-height-alt: 18px; margin: 0;"><span style="color: #999999; font-size: 12px;">Training Zones</span></p>
</div>
</div>
<!--[if mso]></td></tr></table><![endif]-->
<!--[if (!mso)&(!IE)]><!-->
</div>
<!--<![endif]-->
</div>
</div>
<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
<!--[if (mso)|(IE)]></td><td align="center" width="160" style="background-color:#0f0f0f;width:160px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
<div class="col num3" style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 159px; width: 160px;">
<div class="col_cont" style="width:100% !important;">
<!--[if (!mso)&(!IE)]><!-->
<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
<!--<![endif]-->
<div align="center" class="img-container center fixedwidth" style="padding-right: 0px;padding-left: 0px;">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]-->
<div style="font-size:1px;line-height:15px"> </div><img align="center" alt="Alternate text" border="0" class="center fixedwidth" src="https://i.ibb.co/tQP0KF9/graph.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 96px; display: block;" title="Alternate text" width="96"/>
<!--[if mso]></td></tr></table><![endif]-->
</div>
<table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
<table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #DCDCDC; width: 70%;" valign="top" width="70%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 5px; padding-bottom: 20px; font-family: Arial, sans-serif"><![endif]-->
<div style="color:#e0e5eb;font-family:Nunito, Arial, Helvetica Neue, Helvetica, sans-serif;line-height:1.5;padding-top:5px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
<div style="line-height: 1.5; font-size: 12px; color: #e0e5eb; font-family: Nunito, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 18px;">
<p style="font-size: 12px; line-height: 1.5; word-break: break-word; text-align: center; mso-line-height-alt: 18px; margin: 0;"><span style="color: #999999; font-size: 12px;">Analytics: VO2max, Mileage, Fitness,Fatigue curve</span></p>
</div>
</div>
<!--[if mso]></td></tr></table><![endif]-->
<!--[if (!mso)&(!IE)]><!-->
</div>
<!--<![endif]-->
</div>
</div>
<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
<!--[if (mso)|(IE)]></td><td align="center" width="160" style="background-color:#0f0f0f;width:160px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
<div class="col num3" style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 159px; width: 160px;">
<div class="col_cont" style="width:100% !important;">
<!--[if (!mso)&(!IE)]><!-->
<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
<!--<![endif]-->
<div align="center" class="img-container center fixedwidth" style="padding-right: 0px;padding-left: 0px;">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]-->
<div style="font-size:1px;line-height:15px"> </div><img align="center" alt="Alternate text" border="0" class="center fixedwidth" src="https://i.ibb.co/FHrY4Dz/calendar.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 96px; display: block;" title="Alternate text" width="96"/>
<!--[if mso]></td></tr></table><![endif]-->
</div>
<table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
<table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #DCDCDC; width: 70%;" valign="top" width="70%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 5px; padding-bottom: 20px; font-family: Arial, sans-serif"><![endif]-->
<div style="color:#e0e5eb;font-family:Nunito, Arial, Helvetica Neue, Helvetica, sans-serif;line-height:1.5;padding-top:5px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
<div style="line-height: 1.5; font-size: 12px; color: #e0e5eb; font-family: Nunito, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 18px;">
<p style="font-size: 12px; line-height: 1.5; word-break: break-word; text-align: center; mso-line-height-alt: 18px; margin: 0;"><span style="color: #999999; font-size: 12px;">Personalized running program telling you exactly how far and fast to run</span></p>
</div>
</div>
<!--[if mso]></td></tr></table><![endif]-->
<!--[if (!mso)&(!IE)]><!-->
</div>
<!--<![endif]-->
</div>
</div>
<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
<!--[if (mso)|(IE)]></td><td align="center" width="160" style="background-color:#0f0f0f;width:160px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
<div class="col num3" style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 159px; width: 160px;">
<div class="col_cont" style="width:100% !important;">
<!--[if (!mso)&(!IE)]><!-->
<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
<!--<![endif]-->
<div align="center" class="img-container center fixedwidth" style="padding-right: 0px;padding-left: 0px;">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]-->
<div style="font-size:1px;line-height:15px"> </div><img align="center" alt="Alternate text" border="0" class="center fixedwidth" src="https://i.ibb.co/HdKL7Y0/pnghut-strava-icon-strava-com-rectangle-logo-k-Y6z-ZLJy6-Z.png" alt="pnghut-strava-icon-strava-com-rectangle-logo-k-Y6z-ZLJy6-Z" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 104px; display: block;" title="Alternate text" width="104"/>
<!--[if mso]></td></tr></table><![endif]-->
</div>
<table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
<table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #DCDCDC; width: 70%;" valign="top" width="70%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 5px; padding-bottom: 20px; font-family: Arial, sans-serif"><![endif]-->
<div style="color:#e0e5eb;font-family:Nunito, Arial, Helvetica Neue, Helvetica, sans-serif;line-height:1.5;padding-top:5px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
<div style="line-height: 1.5; font-size: 12px; color: #e0e5eb; font-family: Nunito, Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 18px;">
<p style="font-size: 12px; line-height: 1.5; word-break: break-word; text-align: center; mso-line-height-alt: 18px; margin: 0;"><span style="color: #999999; font-size: 12px;">Import From Strava,csv or manual</span></p>
</div>
</div>
<!--[if mso]></td></tr></table><![endif]-->
<!--[if (!mso)&(!IE)]><!-->
</div>
<!--<![endif]-->
</div>
</div>
<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
<!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
</div>
</div>
</div>
<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
</td>
</tr>
</tbody>
</table>
<!--[if (IE)]></div><![endif]-->
</body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

emails= select_all_emails() 
emails = [mail for (mail,) in emails]

mailTarget = int(input("how many mails to send?  :"))


noMails = 0
# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    for mail in emails:
        if len(mail)>4:
            try:
                
                if noMails<mailTarget:
                    server.sendmail(
                        sender_email, mail, message.as_string()
                    )
                    update(mail)
                    noMails = noMails + 1
                    print(noMails,"----",mail)
                else:
                    print("done")
                    break
            except:
                print("something went wrong with",mail)