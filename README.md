# Cedolino (webscraping) downloader
## Informazioni
Questo script Python è progettato per automatizzare il download mensile di un cedolino da un sito web specifico.

Il codice inizia impostando la lingua locale su italiano usando il modulo locale. Successivamente, ottiene la data attuale nel formato 'dd-mm-YYYY' utilizzando il modulo datetime. La data viene quindi divisa in giorno, mese e anno.

Il mese corrente viene verificato: se è luglio, agosto o settembre, lo script termina. In caso contrario, il mese viene ridotto di uno (per ottenere il mese precedente) e vengono gestiti i casi speciali, come gennaio che diventa dicembre.

Il login automatico al sito web specifico avviene mediante il comando wget, che salva i cookie in un file chiamato cookies.txt.

Successivamente, viene utilizzato nuovamente wget per scaricare l'HTML dalla pagina web del mese corrente. Questo HTML viene analizzato utilizzando il modulo BeautifulSoup, consentendo di estrarre il link del cedolino.

Dopodiché, lo script utilizza nuovamente wget per scaricare il cedolino in formato PDF dalla pagina web corrispondente al mese e all'anno correnti, attende 15 secondi per garantire il completamento del download, ed elimina i file temporanei, inclusi i cookie e l'HTML scaricato.

Infine, il link completo al cedolino viene costruito utilizzando le informazioni ottenute dalla data attuale e dallo scraping della pagina HTML.

## Versione ARGV
La versione dello script con ARGV mi permette di dare in input un numero affinché io possa forzare il download di un determinato mese.

## To do
Attualmente sto pianificando la ricerca della Certificazione Unica in modo tale da scaricare e salvare automaticamente anche quella.
