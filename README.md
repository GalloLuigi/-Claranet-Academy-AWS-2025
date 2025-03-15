# Soluzioni Esercizi Claranet 2025

Questo repository contiene le soluzioni agli esercizi proposti in "Esercizi Claranet 2025.pdf".

## Contenuti

Questo repository include le soluzioni per i seguenti esercizi:

*   **Esercizio 1:** Scrittura di uno script bash o python per contare il numero di file eseguibili contenuti in una directory, raggruppandoli in base all'interprete specificato nello shebang.
    *   L'esercizio richiedeva uno script che, data una directory, producesse un output simile al seguente esempio:
        ```
        $ contaScript /usr/bin
        81 #!/usr/bin/perl
        52 #!/usr/bin/perl5.18
        47 #!/bin/sh
        44 #!/usr/bin/perl5.28
        22 #!/usr/sbin/dtrace -s
        ...
        ```
        
*   **Esercizio 2:** Scrittura di una stringa crontab per creare un backup della cartella `/home/user` ogni domenica notte e inviarlo a un server remoto raggiungibile tramite SSH all'indirizzo `user@192.168.1.100`.
    *   La stringa crontab per l'Esercizio 2 dovrebbe essere aggiunta al file crontab dell'utente sulla macchina locale utilizzando il comando `crontab -e`.
    *   Per gestire l'autenticazione sul server remoto, potrebbe essere necessario configurare l'autenticazione basata su chiavi SSH per evitare l'inserimento manuale della password. Questo implica la generazione di una coppia di chiavi SSH (pubblica e privata) sulla macchina locale, e l'aggiunta della chiave pubblica al file authorized_keys dell'utente user sul server remoto 192.168.1.100.

## Outcome

Come richiesto, questo repository Git pubblico è stato creato per caricare le soluzioni degli esercizi.

## Scadenza

Gli esercizi dovevano essere completati entro due giorni dalla consegna della traccia.
