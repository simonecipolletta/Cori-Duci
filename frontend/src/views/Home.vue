<template>
    <section class="hero-section">
        <div class="hero-overlay"></div>
        <div class="hero-container">
            <div class="hero-text">
                <h1 class="hero-text">Cori Duci</h1>
                <p class="hero-text cta-p">Dalla colazione all'aperitivo, prepariamo ogni giorno specialità dolci e salate siciliane con ingredienti genuini e tanta passione.</p>
            </div>
            <div class="hero-cta">
                <router-link to="/prodotti/" class="hero-text btn-primary">Cosa Gustare</router-link>
            </div>
        </div>
    </section>

    <section class="products">
        <h2 class="product-title-home">I Nostri Prodotti</h2>
        <div class="products-wrapper">
            <div class="product-card" v-for="product in products_category" :key="product.id">
                <router-link :to="`/prodotti/${product.slug}`">
                    <div class="image-wrap">
                        <img v-if="product.iconMinimal" :src="product.iconMinimal" :alt="product.name" class="product-image-home">
                    </div>
                    <div class="overlay-black">
                        <span>{{ product.name }}</span>
                    </div>
                </router-link>
            </div>
        </div>
    </section>

    <section class="about-me">
        <div class="about-wrapper">
                <div class="titolare">
                    <img src="/images/SalvatoreParatore.webp" alt="Salvatore Paratore" class="img-titolare">
                    <h3>Salvatore Paratore</h3>
                    <p>Titolare di Cori Duci</p>
                </div>
                <div class="location">
                    <div class="elegant-glass-frame">
                        <img src="/images/coriduci.webp" alt="Negozio Cori Duci" class="company-storefront">
                    </div>
                </div>
            <div class="about-us">
                <h3>Cori Duci </h3>
                <p>Cori Duci, tradotto dal dialetto siciliano significa <strong>"Cuore Dolce"</strong>. Nasce con una missione semplice e autentica: trasformare ogni giorno ingredienti genuini in momenti di felicità. Crediamo nella pasticceria fatta con il cuore, dove tradizione e creatività si incontrano per dare vita a dolci che raccontano una storia di passione, cura e artigianalità. Ogni prodotto è pensato per offrire un’esperienza che profuma di casa, accoglienza e qualità, perché per noi la dolcezza non è solo un sapore, ma un modo di prendersi cura delle persone.</p>
            </div>
        </div>
    </section>

    <section class="google-review">
        <div class="reviews-header">
            <h2>Dicono di noi</h2>
            <!-- Sostituisci questo con un logo ufficiale di Google se vuoi -->
            <p class="google-subtitle">
                Scelto dai nostri clienti su 
                <strong class="google-logo-text">
                    <span style="color: #4285F4;">G</span><span style="color: #EA4335;">o</span><span style="color: #FBBC05;">o</span><span style="color: #4285F4;">g</span><span style="color: #34A853;">l</span><span style="color: #EA4335;">e</span>
                </strong>
            </p>
            <a href="https://g.page/r/CVhnhkwssI0BEAE/review" target="_blank" rel="noopener noreferrer" class="btn-review">
            Lascia una recensione
            </a>
        </div>
        <div class="reviews-wrapper">
            <div class="review-card" v-for="review in reviews" :key="review.id">
                <div class="reviewer-info">
                    <!-- Pallino colorato con l'iniziale del nome -->
                    <div class="avatar" :style="{ backgroundColor: review.avatarColor }">{{ review.initial }}</div>
                    <div class="reviewer-details">
                        <span class="reviewer-name">{{ review.author_name }}</span>
                        <span class="review-time">{{ calcolaTempoTrascorso(review.date) }}</span>
                    </div>
                </div>
                <!-- Stelline (Usa le emoji o un'icona SVG/FontAwesome) -->
                <div class="stars">⭐⭐⭐⭐⭐</div>
                <div class="review-text">
                    <p>{{ review.text }}</p>
                </div>
            </div>
        </div>
    </section>
</template>



<script setup>
    import {ref, onMounted} from 'vue'
    const products_category = ref([])

    const fetchProductsCategory = async () => {
        try{
            const response = await fetch('api/categorie/')
            const datiJson = await response.json()
            products_category.value = datiJson
        } catch (error){
            console.error('Errore nel recupero dei dati:', error)
        }
    }

    onMounted (() => {
        fetchProductsCategory()
    })

    const reviews = ref([

    {
        id: 1,
        author_name: "Roberto D'ALESSANDRO",
        initial: "M",
        avatarColor: "#e91e63", // Rosa scuro/Magenta
        date: "2026-06-07",
        text: "Bar di relativa recente apertura che si presenta in maniera elegante e che offre prodotti salati e dolci che oltre a essere buonissimi sono anche piccole opere d’arte grazie alla sapiente arte di uno chef “rodato”. Ho più volte assaggiato il bombolone e l’ho sempre trovato pieno di crema. Personale disponibile e cortese e servizio rapido. Ne abbiamo usufruito più volte e ne siamo rimasti sempre soddisfatti. Lo consiglio vivamente!",
        rating: 5
    },
    {
        id: 2,
        author_name: "Tomx TRF",
        initial: "T",
        avatarColor: "#ff9800", // Arancione
        date: "2026-05-28",
        text: "Personale simpatico e accogliente, salati e pasticcini ottimi, arancini allucinanti. In poche visite ci hanno già fatto sentire di casa, con piccole attenzioni spontanee che altri bar della zona, frequentati da 6 anni quotidianamente, non hanno mai avuto.",
        rating: 5
    },
    {
        id: 3,
        author_name: "Marco",
        initial: "M",
        avatarColor: "#34a853", // Verde Google
        date: "2026-04-28",
        text: "Aperto da poco, offre pasticceria siciliana. Arredamento elegante e sobrio è un piacere visitarlo Il caffè è ottimo come pure buonissimi i dolci. C'è anche qualcosa di salato tipo arancinini ma non ho ancora assaggiato Per Pasqua ho trovato anche delle originali idee da regalare. Che dire, è entrato nella mia top five a Pescara e veleggia verso il primo posto...",
        rating: 5
    }
])

// 2. Funzione che calcola il tempo trascorso dinamicamente
const calcolaTempoTrascorso = (dataRecensione) => {
    const dataInizio = new Date(dataRecensione);
    const dataOggi = new Date();

    // Calcola la differenza in millisecondi e trasformala in giorni
    const differenzaMs = dataOggi - dataInizio;
    const giorni = Math.floor(differenzaMs / (1000 * 60 * 60 * 24));

    if (giorni === 0) return "Oggi";
    if (giorni === 1) return "Ieri";
    if (giorni < 7) return `${giorni} giorni fa`;

    const settimane = Math.floor(giorni / 7);
    if (settimane === 1) return "1 settimana fa";
    if (settimane < 4) return `${settimane} settimane fa`;

    const mesi = Math.floor(giorni / 30);
    if (mesi === 1) return "1 mese fa";
    if (mesi < 12) return `${mesi} mesi fa`;

    const anni = Math.floor(giorni / 365);
    if (anni === 1) return "1 anno fa";
    return `${anni} anni fa`;
}

</script>

<style scoped>
/* =================================== SEZIONE HERO =================================== */

.hero-section{
    position: relative;
    width: 100%;
    min-height: 40vh;
    display: flex;
    align-items: center;
    background-image: url('/images/hero/coriduci.webp?v=1');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.hero-overlay{
    position: absolute;
    top:0;
    left:0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1;
}

.hero-container{
    position: relative;
    z-index: 2;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
    padding: 40px 20px;
    display: flex;
    justify-content: space-around;
    flex-direction: column;
    gap: 30px;
}

.hero-text {
    color: #ffffff; /* Testo bianco per contrastare l'overlay scuro */
}
.cta-p {
    width: 100%;
    max-width: 600px; /* Evita che diventi troppo largo su desktop e resta fluida su mobile */
}
/* STILE DEL BOTTONE (Call To Action) */
.btn-primary {
    display: inline-block;
    padding: 12px 24px;
    background-color: var(--color-secondary); /* Usa il tuo colore principale (es. Rosso o Oro) */
    color: var(--color-text);
    text-align: center;
    text-decoration: none;
    border-radius: 8px;
    font-weight: bold;
    font-size: 1.1rem;
    transition: background-color 0.3s ease, transform 0.2s ease;

    /* LE DUE REGOLE FONDAMENTALI PER EVITARE L'A CAPO: */
    white-space: nowrap; 
    min-width: max-content; /* Forza il bottone ad allargarsi in base al testo */
}

@media (min-width:768px){
    .hero-section{
        min-height: 60vh;
    }
    .hero-container{
        flex-direction: row;
        align-items: center;
    }
}

@media (min-width: 1024px){
    .btn-primary:hover {
        background-color: var(--color-accent);
        color: var(--color-background);
        transform: scale(1.05);
    }
}

/* =================================== SEZIONE DEI PRODOTTI =================================== */

.products{
        max-width: 1200px;
        margin:0 auto;
}

.product-title-home{
    text-align: center;
    padding:15px;
}

.products-wrapper{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap:30px;
    padding: 20px;
}

.product-card{
    width: 340px;
    height:120px;
    border-radius:12px;    
    position: relative;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    overflow: hidden;
    cursor: pointer;
    display: flex;
    flex-direction: row;
    align-items: center;
    background-color: var(--color-accent);
}

.image-wrap {
    width: 120px;
    height: 120px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: var(--color-accent);
    flex-shrink: 0;
    padding:15px 15px 15px 0;
}

.product-image-home{
    width: 100%;
    height: 100%;
    object-fit: contain;
}

.overlay-black{
    position:absolute;
    top:0;
    left:0;
    width: 100%;
    height: 100%;
    /* background-color: rgba(0, 0, 0, 0.3); */
    display: flex;
    justify-content: center;
    align-items: center;
}

.overlay-black span{
    color:var(--color-background);
    text-transform: uppercase;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 5.5);
    position: relative; /* Fondamentale: rende lo span il punto di riferimento per before/after */
    padding: 10px 0;    /* Spazio per far respirare le linee sopra e sotto */
    display: inline-block;
    font-weight: bold;
    white-space: normal;     /* Forza il testo ad andare a capo alla fine dello spazio disponibile */
    word-break: break-word;
    border-top: 3px solid var(--color-primary);
    border-bottom: 3px solid var(--color-primary);
}

/* =================================== SEZIONE ABOUT ME =================================== */

.about-me{
    width:100%;
    background-color: var(--color-secondary);
}

.about-wrapper{
    width:100%;
    max-width: 1200px;
    margin:0 auto;
    display: grid;
    grid-template-columns: 1fr;
    align-items: center;
    padding:40px 20px;
    gap:20px;
}

.titolare{
    text-align: center;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    pointer-events: none;
}

.img-titolare{
    width: 180px;
    height: 180px;
    object-fit: cover;
    border-radius: 50%;
    border: 5px solid var(--color-secondary);
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    margin-bottom: 15px;
}

.titolare h3{
    border-bottom: 2px solid var(--color-text);
}

.titolare h3, .titolare p {
    padding:5px;
}

.location {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 30px; /* Vitale per non far tagliare la cornice dal container padre */
}

/* =================================== CORNICE ELEGANTE VETRINA =================================== */

/* CONTENITORE: Crea la cornice di vetro */
.elegant-glass-frame {
    position: relative;
    display: inline-block;
    margin: 0 auto;
    max-width: 500px;
}

/* PSEUDO-ELEMENTO: Crea la cornice decorativa sovrapposta */
.elegant-glass-frame::after {
    position: absolute;
    content: '';
    display: block;
    
    /* Coordinate di posizionamento */
    top: -90px;
    left: -70px;
    right: -70px;
    bottom: -90px;
    
    /* Spessore fisico del bordo */
    border-style: solid;
    border-width: 100px; 
    
    border-color: transparent;
    
    /* Immagine della cornice */
    border-image-source: url('/images/cornice.png');
    
    /* IL VALORE CORRETTO TROVATO */
    border-image-slice: 320; 
    
    pointer-events: none;
    z-index: 2;
}

/* L'IMMAGINE INTERNA */
.company-storefront {
    display: block;
    width: 100%;
    height: auto;
    object-fit: cover;
    border-radius: 4px; 
}
.about-us h3{
    text-align: center;
    padding:10px 0;
}

.about-us{
    text-align: justify;
}

/* TABLET */

@media (min-width: 768px) {
    .about-wrapper {
        grid-template-columns: repeat(2, 1fr);
        align-items: start;
    }

    .titolare{
        justify-self:start;
    }

    .about-us h3{
        text-align: left;
    }

    .about-us {
        grid-column: span 2;
        margin: 0 auto;
    }

    .titolare {
        transform: translateY(-80px);
    }
}
@media (min-width:1024px){

}

/* =================================== SEZIONE RECENSIONI =================================== */

.google-review {
    width: 100%;
    padding: 60px 20px;
    background-color: var(--color-background); /* Assicurati che stacchi dal colore della sezione precedente */
}

.reviews-header {
    text-align: center;
    margin-bottom: 40px;
}

.google-subtitle {
    color: #5f6368; /* Colore grigio tipico di Google */
    font-size: 0.9rem;
}

/* La griglia per le card */
.reviews-wrapper {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr; /* 1 colonna su mobile */
    gap: 20px;
}

/* Stile della singola card stile "Google" */
.review-card {
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    gap: 12px;
}

/* Intestazione della recensione (Foto + Nome) */
.reviewer-info {
    display: flex;
    align-items: center;
    gap: 15px;
}

.avatar {
    width: 40px;
    height: 40px;
    /* background-color: #1a73e8; rimossa in quanto la passo fisicamente a ogni recensione con avatarColor */
    color: white;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    font-size: 1.2rem;
}

.reviewer-details {
    display: flex;
    flex-direction: column;
}

.reviewer-name {
    font-weight: bold;
    color: #202124;
}

.review-time {
    font-size: 0.8rem;
    color: #70757a;
}

/* Corpo della recensione */
.review-text p {
    color: #3c4043;
    line-height: 1.5;
    font-size: 0.95rem;
}

/* Stile del bottone Recensioni */
.btn-review {
    display: inline-block;
    margin-top: 15px;
    padding: 12px 25px;
    background-color: #1a73e8; /* Colore Blu Google */
    color: #ffffff;
    text-decoration: none;
    border-radius: 25px; /* Bordi molto arrotondati, stile moderno */
    font-weight: bold;
    font-size: 0.95rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
}

.btn-review:hover {
    background-color: #1557b0; /* Blu leggermente più scuro al passaggio del mouse */
    transform: translateY(-2px); /* Effetto sollevamento */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.google-logo-text {
    font-family: 'Product Sans', Arial, sans-serif;
    letter-spacing: -0.5px; /* Avvicina leggermente le lettere */
    font-size: 1.1em;
}

/* MEDIA QUERIES per Tablet e Desktop */
@media (min-width: 768px) {
    .reviews-wrapper {
        grid-template-columns: repeat(2, 1fr); /* 2 colonne su tablet */
    }
    /* Centra la terza recensione in modo simmetrico */
    .review-card:nth-child(3):last-child {
        grid-column: span 2; /* Fai in modo che questa card occupi entrambe le colonne */
        justify-self: center; /* Centrala orizzontalmente */
        width: calc(50% - 10px); /* Dalle esattamente la larghezza delle card superiori (50% meno metà del gap di 20px) */
    }
}

@media (min-width: 1024px) {
    .reviews-wrapper {
        grid-template-columns: repeat(3, 1fr); /* 3 colonne su desktop */
    }
    /* Resetta la regola precedente quando lo schermo è grande (torna a 3 colonne in fila) */
    .review-card:nth-child(3):last-child {
        grid-column: span 1; 
        width: 100%; 
    }
}

</style>