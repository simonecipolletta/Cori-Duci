<template>

    <div class="products-container" :class="{ 'has-active-category': categoryUrl }">
        <!-- COLONNA SINISTRA (O SCHERMATA PRINCIPALE MOBILE) -->
        <div class="category-list">
            <h3 class="macro-category-showed">Seleziona una categoria</h3>
            <ul class="list-macro-category">
                <li v-for="cat in categories" :key="cat.id">
                    <router-link :to="`/prodotti/${cat.slug}`" exact-active-class="active" class="category-by-card desktop-only" :style="{ backgroundImage: `url(${cat.image})` }">
                        <span>{{ cat.name }}</span>
                    </router-link>
                    <router-link :to="`/prodotti/${cat.slug}`" exact-active-class="active" class="category-icon-card mobile-only">
                        <div class="card-left">
                            <img :src="cat.icon || cat.image" :alt="cat.name" class="cat-icon">
                            <span class="cat-label">{{ cat.name }}</span>
                            <span class="cat-arrow">›</span>
                        </div>
                    </router-link>
                </li>
            </ul>
        </div>

        <!-- COLONNA DESTRA (O SECONDA SCHERMATA MOBILE) -->
        <div class="show-category">
            <Transition name="fade" mode="out-in">
              <div v-if="!categoryUrl" key="no-cat" class="empty-state-desktop">
                  <h2 class="no-category-selected">Nessuna categoria selezionata</h2>
                  <p class="no-category-selected">Seleziona una categoria per scoprire da vicino le nostre dolcezze</p>
              </div>
              <div v-else class="category-showed" :key="categoryUrl">
                  <div class="mobile-back-nav">
                      <router-link to="/prodotti" class="back-button">
                          ← Torna alle categorie
                      </router-link>
                  </div>
                  <h2 class="category-title">{{ titleCategory }}</h2>
                  <div>
                      <ProductSheet v-for="product in showProductsPage" :key="product.id" :info="product"/>
                  </div>
                  <!-- BOTTONI -->
                  <div class="pagination-controls" v-if="totalPages > 1">
                      
                      <button 
                          @click="prevPage" 
                          :disabled="currentPage === 1"
                          class="btn-page btn-nav">
                          &laquo;
                      </button>
                      
                      <button 
                          v-for="page in pageNumbers" 
                          :key="page"
                          @click="goToPage(page)"
                          class="btn-page"
                          :class="{ 'active-page': currentPage === page }">
                          {{ page }}
                      </button>
                      
                      <button 
                          @click="nextPage" 
                          :disabled="currentPage === totalPages"
                          class="btn-page btn-nav">
                          &raquo;
                      </button>
                  </div>
                  <!-- FINE BOTTONI -->
              </div>
            </transition>
        </div>
    </div>
</template>



<script setup>
import {ref, computed, onMounted, watch} from 'vue';
import { useRoute } from 'vue-router';
import ProductSheet from '../components/ProductSheet.vue';

const route = useRoute()
const categories = ref([])
const allProducts = ref([])

onMounted(async ()=> {
    try{
        const response = await fetch('/api/categorie/');
        if(!response.ok) throw new Error('Errore nella risposta del server');
        categories.value = await response.json();

        const prodResponse = await fetch('/api/prodotti/');
        if (!prodResponse.ok) throw new Error('Errore prodotti');
        allProducts.value = await prodResponse.json();

    } catch (error){
        console.error("Errore nel caricamento delle categorie:", error);
    }
});

const categoryUrl = computed (() => route.params.category );

const titleCategory = computed (() => {
    if (categoryUrl.value){
        return categoryUrl.value.replace(/-/g, ' ').toUpperCase();
    }
    return '';
})

const showProducts = computed(() => {
    if (!categoryUrl.value || categories.value.length === 0) {
        return [];
    }
    // A. Troviamo l'oggetto categoria attuale usando lo slug presente nell'URL
    const activeCategory = categories.value.find(cat => cat.slug === categoryUrl.value);
    if (!activeCategory) {
        return [];
    }
    // B. Filtriamo l'array generale dei prodotti per mostrare solo quelli
    // in cui la "category" (l'ID assegnato da Django) coincide con l'ID della categoria attiva
    return allProducts.value.filter(product => product.category === activeCategory.id);
});
// CODICE PER IMPAGINAZIONE CORRETTO

// 2. Uniformati i nomi delle variabili in inglese per farli combaciare con il resto del codice
const currentPage = ref(1);
const itemsPerPage = 6;

const totalPages = computed(() => {
    return Math.ceil(showProducts.value.length / itemsPerPage);
});

const showProductsPage = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    return showProducts.value.slice(start, end);
});

const nextPage = () => {
    if (currentPage.value < totalPages.value) currentPage.value++;
};

const prevPage = () => {
    if (currentPage.value > 1) currentPage.value--;
};
// Genera un array con tutti i numeri delle pagine (es. [1, 2, 3, 4])
const pageNumbers = computed(() => {
    const pages = [];
    for (let i = 1; i <= totalPages.value; i++) {
        pages.push(i);
    }
    return pages;
});

// Funzione per saltare a una pagina specifica quando si clicca il numero
const goToPage = (page) => {
    currentPage.value = page;
};
// 3. Ora 'watch' è importato e funzionerà correttamente usando 'currentPage'
watch(categoryUrl, () => {
    currentPage.value = 1;
});
</script>

<style scoped>

.products-container{
    width:100%;
    max-width: 1200px;
    margin: 0 auto;
    display: block;
    padding: 15px;
}

.products-container:not(.has-active-category) .show-category {
        display: none;
}

.products-container.has-active-category .category-list {
        display: none;
}

.list-macro-category{
    list-style-type: none;
    height: 100%;
}

.list-macro-category li{
    padding:10px;
}

.macro-category-showed{
    border-right: none;
    border-bottom: 1px solid var(--color-text);
    padding-bottom: 10px;
    text-align: center;
}

.category-showed{
    text-align: center;
}

.category-title{
    padding: 25px;
    border-top: 1px solid var(--color-text);
    border-bottom: 1px solid var(--color-text);
    overflow-wrap: break-word;
    hyphens: auto;
}

.no-category-selected{
    padding: 20px;
    text-align: center;
}

h2.no-category-selected {
    border-top: 1px solid var(--color-text);
    border-bottom: 1px solid var(--color-text);
}

/* Nascondiamo il tasto indietro su Desktop */
.mobile-back-nav {
    display: block;
    text-align: left;
    margin-bottom: 20px;
}

.back-button {
    display: inline-block;
    padding: 10px 15px;
    background-color: #f0f0f0; /* Modifica coi tuoi colori */
    text-decoration: none;
    color: var(--color-text);
    border-radius: 5px;
    font-weight: bold;
}

/* testo macrocategoria da sistemare in alto */
.category-icon-card{
    aspect-ratio: 3 / 1;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    border-radius: 9px;
    border: 1px solid var(--color-text);

    /* ANGOLI E OMBRA 3D */
    border-radius: 15px; /* Angoli più dolci */
    border: none; /* Rimuoviamo il bordo duro! */
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.60); /* L'ombra morbida che crea il 3D */
}

/* (Opzionale) Se l'utente tocca la card, si "schiaccia" leggermente */
.category-icon-card:active {
    transform: translateY(2px);
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
}
.category-by-card span{
    color:var(--color-text);
    font-weight: bold;
}

.card-left{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    gap: 10px;
    padding: 10px 15px;
    box-sizing: border-box;
}

.cat-icon {
    width: clamp(30px, 12vw, 100px);
    object-fit: contain;
    flex-shrink: 0;
}

.cat-label {
    /* LA MAGIA: Permette al testo di restringersi all'infinito senza rompere il contenitore */
    min-width: 0;
    /* Se lo spazio è minuscolo, manda a capo la parola spezzandola pur di non uscire fuori */
    overflow-wrap: break-word;
    hyphens: auto; /* Aggiunge il trattino se spezza la parola (es. Pastic-ceria) */
    font-weight: bold;
    text-align: left;
    line-height: 1.2;
}

.cat-arrow {
    flex-shrink: 0; /* Vieta alla freccia di schiacciarsi */
    font-size: 1.5rem;
    padding-left: 5px;
}

/* DI BASE (Cioè per i telefoni): Nascondiamo il design Desktop */
.desktop-only {
    display: none;
}

/* Mostriamo normalmente il design Mobile (le tue card bianche con icona) */
.mobile-only {
    display: flex; /* O il display che serve alla tua card */
}
/* --- PAGINAZIONE --- */
.pagination-controls {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px; /* Spazio tra i bottoni */
    margin-top: 40px;
    margin-bottom: 20px;
    padding-top: 20px;
    /* border-top: 1px solid var(--color-text); */
}

.btn-page {
    background-color: transparent;
    color: var(--color-text);
    border: 1px solid var(--color-text);
    border-radius: 6px;
    padding: 8px 14px;
    cursor: pointer;
    font-family: inherit;
    font-weight: bold;
    font-size: 1rem;
    transition: all 0.3s ease;
}

/* Effetto Hover sui bottoni cliccabili */
.btn-page:hover:not(:disabled) {
    background-color: var(--color-text);
    color: #fff; /* Puoi sostituire #fff col colore di sfondo del tuo sito */
}

/* Stile per la pagina attualmente attiva */
.btn-page.active-page {
    background-color: var(--color-text); 
    color: #fff;
    pointer-events: none; /* Impedisce di cliccare di nuovo la pagina su cui sei */
}

/* Stile per le frecce Avanti/Indietro disabilitate */
.btn-page:disabled {
    opacity: 0.3;
    cursor: not-allowed;
    border-color: transparent; /* Nasconde il bordo per renderli più discreti */
}

/* --- EFFETTO FADE DELLA TRANSIZIONE --- */
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease; /* Durata dell'effetto: 0.3 secondi */
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0; /* Quando entra o esce, parte o diventa completamente invisibile */
}
/* Nascondiamo il messaggio iniziale sui cellulari per evitare il glitch dell'animazione */
.empty-state-desktop {
    display: none;
}

@media (min-width: 480px){
    .category-icon-card{
        aspect-ratio: 4 / 1;
    }
}

@media (min-width: 768px) {
    .empty-state-desktop {
        display: block; /* Lo mostriamo solo da tablet in su */
    }
    .products-container {
        display:grid;
        grid-template-columns: 400px 1fr;
        gap:40px;
        padding:25px;
    }

    .category-by-card{
        height: 100px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-position: left;
        background-repeat: no-repeat;
        background-size: cover;
        border-radius: 9px;
        border: 1px solid var(--color-text);
    }

    .list-macro-category {
        border-right:1px solid var(--color-text);
    }

    .macro-category-showed{
        border-right: 1px solid var(--color-text);
        text-align: center;
    }

    .products-container:not(.has-active-category) .show-category {
        display: block;
    }

    .products-container.has-active-category .category-list {
        display: block;
    }

    .mobile-back-nav {
        display: none;
    }

    .mobile-only {
        display: none !important;
    }

    .desktop-only{
        display:flex;
    }
}

</style>