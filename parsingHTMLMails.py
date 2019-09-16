# parsing of html using email.mime

from email.mime.text import MIMEText as Text
from email.mime.multipart import MIMEMultipart

plain ="Hello im plain text"
html = "<html><h1>Helllo im html text</h1></html>"

plain_txt = Text(plain,"plain")
html_txt =Text(html, "html")

parse = MIMEMultipart("alternative")
parse["Subject"]="Hello there"
parse["From"]="ssajah@gamjds"
parse["To"]="afdadjf@dkajfkd"



parse.attach(plain_txt)
parse.attach(html_txt)

print(parse.as_string())
