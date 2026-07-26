<template>
    <div class="cardproduct-container">
        <div class="titlesheet">
            <h3 class="titlesheet">{{ info.name }}</h3>
        </div>
        <div class="imagesheet">
            <img :src="info.image" :alt="info.name" class="info-card-image">
        </div>
        <!-- Blocco 1: Solo la descrizione (a destra) -->
        <div v-if="info.description" class="desc-sheet">
            <p class="info-card-style"><strong>Descrizione: </strong>{{ info.description }}</p>
        </div>
        <!-- Blocco 2: Allergeni e Prezzi (sotto tutto) -->
        <div class="meta-sheet">
            
            <!-- NUOVO BLOCCO VARIANTI -->
            <div v-if="info.variants" class="info-card-style variants-wrapper">
                <strong>Varianti disponibili:</strong>
                <ul class="variants-list">
                    <li v-for="(variante, index) in info.variants.split(',')" :key="index">
                        {{ variante.trim() }}
                    </li>
                </ul>
            </div>
            <p v-if="info.allergens" class="info-card-style"><strong>Allergeni: </strong>{{ info.allergens }}</p>
            <p  v-if="info.price" class="info-card-style"><strong>Prezzo: </strong>{{ formattaPrezzo(info.price) }}</p>
            <p v-if="info.smallprice" class="info-card-style"><strong>Prezzo formato piccolo: </strong>{{ formattaPrezzo(info.smallprice) }}</p>            
            <p v-if="info.pricePorKilo" class="info-card-style"><strong>Prezzo per Kg: </strong>{{ formattaPrezzo(info.pricePorKilo) }}</p>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';
defineProps({
    info:Object
})
// NUOVA COMPUTED: Taglia la descrizione in due parti
const descrizioneDivisa = computed(() => {
    const testoCompleto = props.info.description || '';
    
    // Cerca l'indice in cui inizia il tag HTML della lista
    const indiceLista = testoCompleto.indexOf('<ul');
    
    // Se non trova nessuna lista nel testo, restituisce tutto normale
    if (indiceLista === -1) {
        return { testoPrincipale: testoCompleto, listaVarianti: '' };
    }
    
    // Se trova la lista, spezza la stringa in quel punto esatto
    return {
        testoPrincipale: testoCompleto.substring(0, indiceLista),
        listaVarianti: testoCompleto.substring(indiceLista)
    };
});
const formattaPrezzo = (numero) => {
    if (!numero) return '€ 0,00';
    return new Intl.NumberFormat('it-IT',{
        style:'currency',
        currency: 'EUR'
    }).format(numero);
}
</script>

<style scoped>
.cardproduct-container {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-areas:
        "titolo"
        "immagine"
        "descrizione"
        "meta";  
    gap: 0 20px;
    padding: 20px 0;
    border-bottom: 1px solid var(--color-text);
    text-align: left;
}

.info-card-image{
    width: 100%;
    aspect-ratio: 4/3;
    object-fit: cover;
    object-position: center;
    border-radius: 8px;
}

.imagesheet {
    grid-area: immagine;
}

.titlesheet {
    grid-area: titolo;
    margin: 0; /* Rimuove lo spazio extra del tag h3 */
    font-family: var(--font-title);
    font-size: clamp(1.75rem, 3vw + 1rem, 2rem);
}

.psheet {
    grid-area: descrizione;
}

.titlesheet, .psheet {
    min-width: 0;
    overflow-wrap: break-word;
}

.info-card-style strong{
    color:var(--color-accent);
}

.info-card-style{
    padding-top: 15px;
    padding-bottom:10px;
}

/* --- STILI PER LE VARIANTI INIETTATE --- */

/* Crea il giusto distacco tra le varianti e gli allergeni sottostanti */
.variants-wrapper {
    margin-bottom: 15px; 
}

/* Sistema l'allineamento dei pallini della lista */
.variants-list{
    margin-top: 8px;
    margin-bottom: 0;
    padding-left: 20px; /* Spinge i pallini per allinearli col testo */
    list-style-type: disc;
}

/* Dà respiro tra le singole voci della lista (Salsiccia, Ragù, ecc.) */
.variants-list{
    margin-bottom: 6px;
    line-height: 1.4;
    color: var(--color-text);
}
.variants-list li {
    margin-bottom: 6px;
    line-height: 1.4;
    color: var(--color-text);
}

/* --- LAYOUT MOBILE (Piccoli schermi) --- */
@media (min-width: 1280px) {
    .info-card-image{
        aspect-ratio: 4/4;
    }
    .info-card-style{
        padding-top: 0;
    }
    .cardproduct-container {
        grid-template-columns: 250px 1fr;
        grid-template-rows: auto 1fr;
        grid-template-areas:
            "immagine titolo"
            "immagine desc-sheet"
            "meta meta";
    }
    .desc-sheet { grid-area: desc-sheet; }
    .meta-sheet { 
        grid-area: meta; 
        display: flex; /* Opzionale: per affiancare prezzi e allergeni se vuoi */
        flex-direction: column;
        margin-top: 15px; /* Dà un po' di respiro sotto l'immagine */
    }
}
</style>