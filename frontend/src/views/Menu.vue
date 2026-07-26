<template>
    <div class="menu-page">
        <!-- Questo div centrale conterrà tutte le scritte del menu -->
        <section class="menu-content">
            <h1>Il Nostro Menu</h1>
            <div class="menu-items">
                
                <h2 class="style-title-menu">Le Nostre Proposte</h2>

                <div class="menu-item-row">
                    <span class="item-name">Pallotte Cacio e Ove</span>
                    <span class="dots"></span>
                    <span class="item-price">6,00€</span>
                </div>
                
                <div class="menu-item-row">
                    <span class="item-name">Cous Cous</span>
                    <span class="dots"></span>
                    <span class="item-price">6,00€</span>
                </div>
                <p class="style-menu-desc">(Mozzarelline, peperoni, pomodori, basilico, tonno)</p>
                
                <div class="menu-item-row">
                    <span class="item-name">Timballo</span>
                    <span class="dots"></span>
                    <span class="item-price">7,00€</span>
                </div>
                
                <div class="menu-item-row">
                    <span class="item-name">Parmigiana</span>
                    <span class="dots"></span>
                    <span class="item-price">6,00€</span>
                </div>
                
                <div class="menu-item-row">
                    <span class="item-name">Insalata di Farro</span>
                    <span class="dots"></span>
                    <span class="item-price">6,00€</span>
                </div>
                
                <div class="menu-item-row">
                    <span class="item-name">Lasagna</span>
                    <span class="dots"></span>
                    <span class="item-price">7,00€</span>
                </div>
                
                <h2 class="style-title-menu combo-title">Combo</h2>
                
                <div class="menu-item-row">
                    <span class="item-name">Arancino + Birra (0.2)</span>
                    <span class="dots"></span>
                    <span class="item-price">5,00€</span>
                </div>
            </div>
        </section>
    </div>
</template>

<script setup>


</script>


<style scoped>

/* =================================== SFONDO CON MAIOLICHE =================================== */

.menu-page {
    background-image: url('../assets/maiolica.webp');
    background-repeat: repeat;
    background-size: 200px auto;
    /* Il padding alto serve a non far finire il menu sotto la navbar */
    flex: 1;
    
    padding: 120px 20px 40px 20px;
    display: flex;
    justify-content: center;
    /* LA MAGIA È QUI: Invece di flex-start, usiamo center */
    align-items: center;
}

/* =================================== CONTENUTO CENTRALE =================================== */

.menu-content {
    width: 100%;
    max-width: 800px; /* Impedisce al testo di allargarsi troppo e coprire le maioliche */
    /* Sfondo per far risaltare il testo. Puoi usare un bianco semi-trasparente o solido */
    background-color: rgba(255, 255, 255, 0.95);
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15); /* Leggera ombra per staccarlo dallo sfondo */
    /* Assicura che il contenitore stia sempre "sopra" lo sfondo */
    position: relative;
    z-index: 10;
}

h1 {
    text-align: center;
    color: var(--color-primary);
    margin-bottom: 30px;
}

.menu-items{
    text-align: center;
}

.style-title-menu {
    font-size: clamp(2rem, 4vw + 1rem, 2.5rem);
    font-family: var(--font-title);
    margin-bottom: 15px;
}

.combo-title {
    margin-top: 40px;
}
/* =================================== ALLINEAMENTO VOCI E PREZZI =================================== */

.menu-item-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline; /* Allinea il testo sulla stessa linea di base */
    width: 100%;
    max-width: 500px; /* Stringe leggermente la riga per renderla più elegante */
    margin: 15px auto; /* auto sui lati serve a centrare il blocco dentro a .menu-items */
}

.item-name, .item-price {
    color: var(--color-text);
    font-size: 1.1rem;
    white-space: nowrap; /* Impedisce che il nome o il prezzo vadano a capo per errore */
}

.dots {
    flex-grow: 1; /* Occupa tutto lo spazio disponibile tra nome e prezzo */
    border-bottom: 2px dotted var(--color-text, #333);
    margin: 0 15px; /* Dà aria tra il testo e i puntini */
    opacity: 0.6; /* Rende i puntini leggermente più tenui rispetto al testo */
}

.style-menu-desc {
    font-size: 0.9rem;
    color: var(--color-text);
    margin-top: -10px; /* Avvicina la descrizione (es. gli ingredienti del cous cous) al nome del piatto */
    margin-bottom: 20px;
}
/* =================================== MOBILE =================================== */
@media (min-width: 768px) {
    .menu-page {
        background-size: 320px auto;
        padding: 60px 20px;
    }

    .menu-content {
        padding: 40px;
        /* Lasciamo i margini esatti della grandezza della maiolica (40px) per non accavallarci */
        /* margin-left: 35px;
        margin-right: 35px; */
    }
}

</style>

