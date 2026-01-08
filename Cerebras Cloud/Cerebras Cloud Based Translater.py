from cerebras.cloud.sdk import Cerebras

zin = 'Im Sommer, wenn es richtig heiß ist, bekommt man  (Sehnsucht)  nach einem Eis.'

Words = """der Zweck:het doel
        die Welle:de golf
        etwas verpassen:iets missen
        sich kümmern um:zorgen voor
        seinerzeit:destijds
        quatschen:kletsen
        sogar:zelfs
        ausbleiben:uitblijven
        sich prügeln:met elkaar vechten
        das Vergnügen:het plezier
        die Öffentlichkeit:de openbaarheid
        rechtzeitig:op tijd
        die Spende:de donatie
        vergnügen:amuseren
        fehlen:ontbreken
        die Unterhaltung:amusement
        recht haben:gelijk hebben
        die Auswahl:de keuze
        einzigartig:uniek
        unbedingt:per se
        verfügen über:beschikken over
        erweitern:uitbreiden
        schmutzig:vies
        verstecken:verstoppen
        die Führung:de rondleiding
        der Termin:de afspraak
        der Vorschlag:het voorstel
        die Verabredung:de afspraak
        die Ermäßigung:de korting
        die Lösung:de oplossing
        die Zeit:de tijd
        die Verspätung:de vertraging
        das Geschenk:het cadeau
        sich verabreden:afspreken
        absagen:afzeggen
        gespannt sein auf:benieuwd zijn naar
        sich entscheiden:sich entscheiden
        schenken:cadeau geven
        dauern:duren
        eine Nachricht schicken:een bericht sturen
        sich treffen:elkaar ontmoeten
        es gibt:er is, er zijn
        recht haben:gelijk hebben
        sich etwas anschauen:iets bekijken
        gucken:kijken
        bekommen:krijgen
        vorbeigehen:langsgaan
        verpassen:missen
        nachdenken:nadenken
        anrufen:opbellen
        stattfinden:plaatsvinden
        einfallen:te binnen schieten
        sich ausruhen:uitrusten
        ausfallen:uitvallen
        halten von:vinden van
        vorschlagen:voorstellen
        fragen:vragen
        warten:wachten
        Lust haben auf:zin hebben in
        angesagt:helemaal in
        anstrengend:inspannen, vermoeiend
        schwierig:moeilijk, lastig
        überraschend:verrassend
        anschließend:aansluitend
        falls:als, in het geval dat
        trotzdem:desondanks, toch
        allerdings:echter
        mal:eens
        keine Ahnung:geen idee
        etwas:iets
        auf keinen Fall:in geen geval
        auf jeden Fall:in ieder geval
        (es ist) egal:maakt niet uit
        monatlich:maandelijks
        einfach:makkelijk; gewoon
        sofort:meteen
        ermäßigt:met korting
        kaum:nauwelijks
        entweder … oder:of … of
        pünktlich:stipt
        schließlich:tenslotte, uiteindelijk
        es sei denn:tenzij
        doch:toch
        vor Kurzem:kortgeleden
        wöchentlich:wekelijks
        der Schlagzeuger:de drummer
        der Gitarrist:de gitarist
        der Künstler:de kunstenaar
        der Roman:de roman
        der Verfasser:de schrijver
        der Zuschauer:de toeschouwer
        der Schauspieler:de toneelspeler, acteur
        die Skulptur:het beeld, de sculptuur
        die Bedeutung:de betekenis
        die Geschichte:de geschiedenis
        die Schlagzeile:de (kranten)kop
        die Kritik:de kritiek
        die Bühne:het podium
        die Rezension:de recensie
        die Stimmung:de sfeer
        die Grafik:de tekening
        die Ausstellung:de tentoonstelling
        die Erzählung:het verhaal, de vertelling
        das Kapitel:het hoofdstuk
        das Gemälde:het schilderij
        empfehlen:aanbevelen
        begründen:beargumenteren
        verstehen:begrijpen
        behandeln:behandelen
        kritisieren:bekritiseren
        bedeuten:betekenen
        begeistert sein von:enthousiast zijn over
        zustimmen:instemmen, het ermee eens zijn
        zeigen:laten zien
        sich überlegen:nadenken
        erscheinen:verschijnen
        erzählen:vertellen
        nachvollziehen:volgen, begrijpen
        hinweisen auf:wijzen op
        sagen:zeggen
        begabt:begaafd, talentvol
        großartig:geweldig
        beeindruckend:indrukwekkend
        bunt:kleurrijk
        kritisch:kritisch
        ähnlich:net zoals, vergelijkbaar
        unentschieden:onbeslist, gelijkspel
        unglaublich:ongelooflijk
        ungewöhnlich:ongewoon
        bewegend:ontroerend
        überzeugend:overtuigend
        spannend:spannend
        schrecklich:verschrikkelijk
        furchtbar:vreselijk
        aufgeregt:zenuwachtig
        kitschig:zoetsappig
        Einverstanden!:Eens!
        einigermaßen:enigszins
        ganz:heel, helemaal
        überhaupt nicht:helemaal niet
        im Prinzip:in principe
        besonders:met name, vooral
        pausenlos:onafgebroken
        neulich:onlangs
        zwar:weliswaar
        zeitgemäß:modern
        erheblich:aanzienlijk
        ausgestattet sein mit:uitgerust zijn met
        verzichten auf:afstand doen van
        die Sehnsucht:het verlangen
        auslösen:veroorzaken
        neidisch:jaloers
        vermitteln:overdragen
        die Bezeichnung:de benaming
        ähneln:lijkt op
        die Geschwindigkeit:de snelheid
        per Funk:per radio
        die Voraussetzung:de voorwaarde
        in der Lage sein:in staat zijn
        der Versuch:de poging
        aufmerksam:alert
        mittlerweile:inmiddels
        damals:toen
        betonen:benadrukken
        der Hintergrund:de achtergrond
        außergewöhnlich:buitengewoon
        vor Kurzem:onlangs
        ablehnen:afwijzen
        überlegen:erover nadenken
        abwechslungsreich:afwisselend
        je nachdem:afhankelijk van
        zurzeit:op het ogenblik
        anwenden:toepassen
        selbstverständlich:vanzelfsprekend
        sich ergeben:voortvloeien
        geeignet:geschikt
        das Seminar:het werkcollege
        die Leidenschaft:de hartstocht, de passie
        der Aufsatz:het opstel
        sich verlassen auf:vertrouwen op
        zunächst:aanvankelijk, in het begin
        die Anregung:de inspiratie
        das Geräusch:het geluid
        rutschen:afzakken, glijden
        die Forderung:de eis
        der Anspruch:de eis
        dennoch:toch
        sich fürchten vor:bang zijn voor
        betrachten:observeren, bekijken
        der Mangel:het gebrek
        schätzen:waarderen
        enttäuschen:teleurstellen
        der Anwalt:de advocaat
        der Job:de baan
        der Betrieb:het bedrijf
        der Beruf:het beroep
        der Berufsberater:de decaan, de loopbaanadviseur
        der Programmierer:de programmeur
        der Dolmetscher:de tolk
        der Unterschied:het verschil
        die Entscheidung:de beslissing
        die Prüfung:het examen
        die Firma:de firma
        die Fachhochschule:het hbo
        die Ausbildung:de opleiding
        die Stärke:het sterke punt
        die Zukunft:de toekomst
        die Auszeit:het tussenjaar
        die Fremdsprache:de vreemde taal
        das Handwerk:het ambacht
        das Ausland:het buitenland
        das Abitur:het eindexamen (vwo)
        das Büro:het kantoor
        das Praktikum:de stage
        das Studium:de studie
        Architektur:architectuur
        Betriebswirtschaft:bedrijfseconomie
        Medizin:geneeskunde
        Informatik:informatica
        Maschinenbau:machinebouw
        Pädagogik:pedagogiek
        Psychologie:psychologie
        Jura:rechten
        erfahren:horen, vernemen
        sich entscheiden für:kiezen voor
        leiten:leiden
        merken:merken
        unterstützen:ondersteunen
        forschen:onderzoeken
        herausfinden:ontdekken
        gründen:oprichten
        passen zu:passen bij
        sich anmelden:zich aanmelden
        sich beraten lassen:zich laten adviseren
        sich leisten:zich veroorloven
        überwiegen:zwaarder wegen, de doorslag geven
        kreativ:creatief
        praktisch:praktisch
        technisch:technisch
        theoretisch:theoretisch
        gefragt:veelgevraagd
        verschiedene:verschillende
        andererseits:aan de andere kant
        einerseits:aan de ene kant
        dabei:daarbij
        dadurch:daardoor
        erst mal:eerst
        genügend:genoeg, voldoende
        während:tijdens, terwijl
        sowohl ... als auch:zowel ... als ook
        der Lebenslauf:het CV (curriculum vitae)
        der Mitarbeiter:de medewerker
        der Ausbildungsplatz:de opleidingsplaats
        der Praktikant:de stagiair
        der Techniker:de technicus
        der Ferienjob:de vakantiebaan
        die Anzeige:de advertentie
        die Abwechslung:de afwisseling
        die Stelle:de baan
        die Note:het cijfer
        die Erfahrung:de ervaring
        die Unterstützung:de ondersteuning
        die Bewerbung:de sollicitatie
        die Herausforderung:de uitdaging
        die Fähigkeit:de vaardigheid
        die Stellenanzeige:de vacature
        die Voraussetzung:de voorwaarde
        die Arbeitszeit:de werktijd
        das Unternehmen:het bedrijf, de onderneming
        das Ziel:het doel
        das Gehalt:het salaris
        das Beispiel:het voorbeeld
        die Unterlagen:de documenten
        die Daten:de gegevens
        die Kenntnisse:de kennis
        kommunizieren:communiceren
        herunterladen:downloaden
        dauern:duren
        Interesse haben an:geïnteresseerd zijn in
        bestehen:halen, met goed gevolg afleggen
        leichtfallen:makkelijk afgaan
        schwerfallen:moeilijk afgaan, niet meevallen
        entwickeln:ontwikkelen
        herstellen:produceren
        sich bewerben um:solliciteren
        tätig sein:werkzaam zijn
        zuverlässig:betrouwbaar
        teamfähig:in staat om in een team te werken
        niedrig:laag
        neugierig:nieuwsgierig
        kontaktfreudig:op contact met anderen gesteld
        tolerant:tolerant
        verantwortungsbewusst:verantwoordelijk
        selbstständig:zelfstandig
        Teilzeit:deeltijd
        zunächst:eerst, aanvankelijk
        hoch:hoog
        gleich:meteen
        unter anderem:onder andere
        auf diese Weise:op deze manier
        auf diesem Gebiet:op dit gebied
        erst:pas
        im Voraus:van tevoren, bij voorbaat
        laut:volgens
        nach Vereinbarung:volgens afspraak
        Vollzeit:voltijd"""


client = Cerebras(
    api_key="csk-tt9d5p8rext8yp6n56em4pxct32nvfmxe655tw2hy3pf32hr",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"""{zin} Vertaal alleen het woord tussen haakjes naar het Nederlands en geef alleen het antwoord. 
                Gebruik de volgende lijst met woorden en hun vertalingen: {Words}. 
                Let op: voeg een Nederlands lidwoord alleen toe als er in de haakjes een Duits lidwoord (der, die, das) staat. 
                Als er geen lidwoord in de haakjes staat, geef alleen het woord. Geef echt alleen het antwoord, niets anders."""
        }
],
    model="gpt-oss-120b",
)

translation = chat_completion.choices[0].message.content

print(translation)  