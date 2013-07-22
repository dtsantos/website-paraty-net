import webapp2
import cgi
from google.appengine.api import users
from google.appengine.api import mail

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.out.write("""
      
<!DOCTYPE HTML>
<html>

<head>
  <title>Paraty.net: Tourism, Hospitality and Culture in Paraty</title>
  <meta name="description" content="Soon the launch of the best website about the city of Paraty with informations about hotels, beaches, islands, day trips and much more..." />
  <meta name="keywords" content="paraty, tourism, hotels, culture, homestays, news, beaches" />
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
  <!-- stylesheets -->
  <link href="css/style.css" rel="stylesheet" type="text/css" />
  <link href="css/dark.css" rel="stylesheet" type="text/css" />
  <!-- modernizr enables HTML5 elements and feature detects -->
  <script type="text/javascript" src="js/modernizr-1.5.min.js"></script>
</head>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-38628760-1']);
  _gaq.push(['_setDomainName', 'paraty.net']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
<body>
  <div id="main">

    <!-- begin header -->
    <header>
      <div id="logo"><h1>Paraty<a href="#">.net</a></h1></div>
      <nav>
        <ul class="sf-menu" id="nav">
          <li><a href="index.en.html">Home</a></li>
          <li class="selected"><a href="contato.en.html">Contact</a></li>
    	  <li><a href="contato.html"><img src="./images/portugues.gif" width="26" height="18" alt="Portugues" /></a></li>   

        </ul>
      </nav>
    </header>    <!-- end header -->
    
    <!-- begin content -->
    <div id="site_content">
      <div id="left_content">
        <h1>Contact</h1>
        <p>Please fill in the form bellow to advertise or to find out more about the upcoming Paraty.net:<br>
        
        <form action="/confirmacao.en.html" method="post">
                <table style="margin-left: 3px" width="50%">
 				<tr>
				  <td align="left"><label for="usr">Name:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="nome" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">Telephone:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="tel" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">E-mail:</label>&nbsp;
				  </td>
  				  <td><input id="usr" type="text" class="txt" name="email" " ></td>
  				</tr>
  				<tr>  
				  <td align="left"><label for="usr">Message:</label>&nbsp;
				  </td>
  				  <td><textarea name="msg" rows="8" cols="40"></textarea></td>
  				
				  <td></td> 
			 	</tr>
			 	<tr>
			 	 <td>
			 	 </td>
			 	 <td align="center"><input type="submit" value="  Enviar  "></td>
			 	</tr>
				</table>
    	</form>
        </p>
        <p><br><strong>Telephones:</strong> (24) 9975-7859 / (24) 3371-0365<br>
        <strong>E-mail:</strong>  davitrindade@gmail.com</p>
        
      </div>
      <div id="right_content">
        <img src="images/solo.jpg" width="450" height="450" title="contact" alt="Contact" />
      </div>
    </div>
    <!-- end content -->

    <!-- begin footer -->
    <footer>
      Paraty.net: Tourism, Hospitality and Culture in Paraty. Launching soon!
      <p><img src="images/facebook.png" alt="facebook" />&nbsp;<img src="images/rss.png" alt="rss" /></p>
    </footer>
    <!-- end footer -->

  </div>
  <!-- javascript at the bottom for fast page loading -->
  <script type="text/javascript" src="js/jquery.min.js"></script>
  <script type="text/javascript" src="js/jquery.easing-sooper.js"></script>
  <script type="text/javascript" src="js/jquery.sooperfish.js"></script>
  <!-- initialise sooperfish menu -->
  <script type="text/javascript">
    $(document).ready(function() {
      $('ul.sf-menu').sooperfish();
    });
  </script>
</body>	
</html>

      """)
      
class Confirmacao(webapp2.RequestHandler):
    def post(self):
    	message = mail.EmailMessage(sender="Davi Trindade <davitrindade@gmail.com>",
                            subject="Enquiry Paraty.net: "+self.request.get('nome'),to="davitrindade@gmail.com",reply_to=" "+self.request.get('nome')+" <"+self.request.get('email')+">",
                            body="Sender: "+self.request.get('nome')+"\nTelephone: "+self.request.get('tel')+"\nEmail: "+self.request.get('email')+"\Message: \n"+self.request.get('msg'))
	message.send()
	
	self.response.out.write("""
      
<!DOCTYPE HTML>
<html>

<head>
  <title>Paraty.net: Tourism, Hospitality and Culture in Paraty</title>
  <meta name="description" content="Soon the launch of the best website about the city of Paraty with informations about hotels, beaches, islands, day trips and much more..." />
  <meta name="keywords" content="paraty, tourism, hotels, culture, homestays, news, beaches" />
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
  <!-- stylesheets -->
  <link href="css/style.css" rel="stylesheet" type="text/css" />
  <link href="css/dark.css" rel="stylesheet" type="text/css" />
  <!-- modernizr enables HTML5 elements and feature detects -->
  <script type="text/javascript" src="js/modernizr-1.5.min.js"></script>
</head>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-38628760-1']);
  _gaq.push(['_setDomainName', 'paraty.net']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
<body>
  <div id="main">

    <!-- begin header -->
    <header>
      <div id="logo"><h1>Paraty<a href="#">.net</a></h1></div>
      <nav>
        <ul class="sf-menu" id="nav">
          <li><a href="index.en.html">Home</a></li>
          <li class="selected"><a href="contato.en.html">Contact</a></li>
    	  <li><a href="contato.html"><img src="./images/portugues.gif" width="26" height="18" alt="Portugues" /></a></li>   

        </ul>
      </nav>
    </header>    <!-- end header -->
    
    <!-- begin content -->
    <div id="site_content">
      <div id="left_content">
        <h1>Confirmation</h1>
        <p>
        <strong>Thank you for your message!</strong>	<br><br>
        We will answer you shortly.<br><br>
        If you prefer please get in touch with us directly:
        </p>
        <p><strong>Telephones:</strong> (24) 9975-7859 / (24) 3371-0365<br>
        <strong>E-mail:</strong>  davitrindade@gmail.com</p>
        
      </div>
      <div id="right_content">
        <img src="images/solo.jpg" width="450" height="450" title="contact" alt="contact" />
      </div>
    </div>
    <!-- end content -->

    <!-- begin footer -->
    <footer>
      Paraty.net: Tourism, Hospitality and Culture in Paraty. Launching soon!
      <p><img src="images/facebook.png" alt="facebook" />&nbsp;<img src="images/rss.png" alt="rss" /></p>
    </footer>
    <!-- end footer -->

  </div>
  <!-- javascript at the bottom for fast page loading -->
  <script type="text/javascript" src="js/jquery.min.js"></script>
  <script type="text/javascript" src="js/jquery.easing-sooper.js"></script>
  <script type="text/javascript" src="js/jquery.sooperfish.js"></script>
  <!-- initialise sooperfish menu -->
  <script type="text/javascript">
    $(document).ready(function() {
      $('ul.sf-menu').sooperfish();
    });
  </script>
</body>	
</html>

      """)
	

      
app = webapp2.WSGIApplication([('/contato.en.html', MainPage),
                              ('/confirmacao.en.html', Confirmacao)],
                              debug=True)