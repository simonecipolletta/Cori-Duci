<template>
    <div class="contact-page-bg">
        <div class="contact-hero-banner">
            <h1>Contatti</h1>
        </div>
        <div class="contact-wrapper">
            <div class="contact-info">
                <h2 id="information">Informazioni di contatto</h2>
                <p><strong>Indirizzo:</strong> Via dei Bastioni, 57, 65128 Pescara (PE)</p>
                <p><strong>Telefono:</strong><a href="tel:+390854217580"> 085 421 7580</a></p>
                <p><strong>Orari di apertura:</strong> Tutti i gioorni 6:30 - 21:00</p>
                <div class="contact-map-wrapper">
                    <iframe
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2943.488052436552!2d14.209347612641693!3d42.45990762866597!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1331a7a984f3403b%3A0x18db02c4c866758!2sCori%20Duci!5e0!3m2!1sit!2sit!4v1781371952657!5m2!1sit!2sit"
                        allowfullscreen=""
                        loading="lazy"
                        referrerpolicy="strict-origin-when-cross-origin"
                        title="Mappa della sede del commercialista Riccioni">
                    </iframe>
                </div>
            </div>  
            <div class="contact-form">
                <h2 class="contact-hero-title">Scrivici un messaggio</h2>
                <p>Compila il modulo qui sotto e ti ricontatteremo al più presto.</p>
                <form @submit.prevent="submit">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="name">Nome</label>
                            <input type="text" id="name" name="name" v-model="form.name" class="form-control" autocomplete="given-name" required>
                        </div>
                        <div class="form-group">
                            <label for="surname">Cognome</label>
                            <input type="text" id="surname" name="surname" v-model="form.surname" class="form-control" autocomplete="family-name" required>
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" v-model="form.email" class="form-control" autocomplete="email" required>
                        </div>
                        <div class="form-group">
                            <label for="telephone">Telefono</label>
                            <input type="tel" id="telephone" name="telephone" v-model="form.telephone" class="form-control" autocomplete="tel" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="message">Messaggio</label>
                        <textarea id="message" name="message" v-model="form.message" class="form-control" rows="5" autocomplete="on" required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="privacy" class="checkbox-label">
                            <input type="checkbox" id="privacy" name="privacy" v-model="form.privacy" required>
                            <span>Acconsento al trattamento dei dati personali ai sensi della <a href="/privacy-policy" target="_blank" rel="noopener noreferrer">Privacy Policy</a>.</span>
                        </label>
                    </div>
                    <p class="recaptcha-disclaimer"> Questo sito è protetto da reCAPTCHA e si applicano la
                        <a href="https://policies.google.com/privacy" target="_blank"rel="noopener noreferrer">Privacy Policy</a> e i
                        <a href="https://policies.google.com/terms" target="_blank"rel="noopener noreferrer">Termini di Servizio</a> di Google.
                    </p>
                    <button type="submit" class="contact-btn">INVIA</button>
                </form>
                <div id="risultato" v-if="messaggio">{{ messaggio }}</div>
            </div>
        </div>
    </div>
</template>

<script setup>
import {ref, reactive } from 'vue';
const messaggio = ref('')

const form = reactive({
    name: '',
    surname: '',
    email: '',
    telephone: '',
    message: '',
    privacy: false,
    recaptcha_token: ''
})

const submit = async () => {
// FASE A: Chiediamo il gettone a Google prima di fare qualsiasi cosa
    window.grecaptcha.ready(() => {
        // Sostituisci LA_TUA_CHIAVE_PUBBLICA_QUI con la vera Site Key
        window.grecaptcha.execute('6Le0cBwtAAAAANTaNQe2Xjuq_lFwGo7dPV56w90O', {action: 'submit'}).then(async (token) => {    
            form.recaptcha_token = token;
            try{
                const response = await fetch('/api/contatti/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(form)
                });

                if (!response.ok) {
                    // Estraiamo la vera risposta di Django
                    const errorData = await response.json(); 
                    console.error("Dettagli errore da Django:", errorData);
                    // Lanciamo l'errore usando la frase esatta di Django
                    throw new Error(errorData.error || 'Errore nella richiesta'); 
                }
                messaggio.value = "Messaggio inviato con successo!";
                form.name = '';
                form.surname = '';
                form.email = '';
                form.telephone = '';
                form.message = '';
                form.privacy = false;
            } catch(error) {
                console.error('Errore:' , error);
                messaggio.value = 'Si è verificato un errore. Riprova'
            } finally {
                setTimeout(() => {
                    messaggio.value = '';
                }, 3000);
            }
        });
    });
};

// Qui andrà la logica della pagina (chiamate API, variabili, ecc.)
</script>

<style scoped>

.contact-page-bg {
    /* Spazio interno per far respirare i box */
    flex: 1;
    padding-top: 40px; 
    padding-bottom: 40px;
    /* Inserisci qui il percorso della tua immagine WebP */
    background-image: url('../assets/coriducicontact.webp');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    /* IL TRUCCO MAGICO: mantiene lo sfondo fermo mentre scorri la pagina */
    background-attachment: fixed;
}

.contact-hero-banner {
    height: 150px;
    width: 100%;
    /* background-image: url('/images/heroimage.webp'); */
    background-size: cover;
    background-position: top;
    background-repeat: no-repeat;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
}

.contact-wrapper{
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 20px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));
    gap: 40px;
}

.contact-form{
    background-color: rgba(255,255,255,0.7);
    padding:25px;
    border:1px solid var(--color-text);
    border-radius: 9px;
}

.contact-form p {
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 20px;
}

.form-control {
    width: 100%;
    padding: 10px;
    border: 1px solid var(--color-primary);
    border-radius: 5px;
    font-size: 1.2rem; /* Più grande per una migliore usabilità */
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: 600;
}

.contact-btn {
    padding: 12px 26px;
    border: 1px solid var(--color-text);
    background: var(--color-primary);
    color: var(--color-text);
    border-radius: 6px;
    font-weight: 600;
    transition: 0.25s ease;
    cursor: pointer;
}
#information{
    text-decoration: underline;
}
.contact-map-wrapper {
    margin-top: 40px;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 18px rgba(0,0,0,0.12);
    aspect-ratio: 16 / 9;
    width: 100%;
}

.contact-map-wrapper iframe {
    width: 100%;
    height: 100%;
    display: block;
    border: none;
}

.form-row {
    display: grid;
    grid-template-columns: 1fr; /* Una singola colonna per i telefoni */
    gap: 0px; /* Nessun gap extra, ci pensa il margin-bottom di form-group */
}

/* Gestione specifica per la riga della privacy */
.checkbox-label {
    display: flex;
    align-items: flex-start; /* Allinea la spunta alla prima riga di testo */
    font-weight: normal; /* Togliamo il grassetto per rendere il testo più leggibile */
    gap: 10px; /* Crea uno spazietto preciso tra il quadratino e la frase */
    cursor: pointer;
}

/* Assicuriamoci che il quadratino abbia dimensioni naturali */
.checkbox-label input[type="checkbox"] {
    width: auto;
    margin-top: 4px; /* Un piccolo ritocco per centrarlo con l'altezza della lettera A */
}

@media (min-width: 768px) {
    .form-row {
        grid-template-columns: 1fr 1fr; /* Due colonne di uguale larghezza */
        gap: 20px; /* Spazio orizzontale tra le due colonne */
    }
    /* Rimuoviamo il margine inferiore del primo elemento per allinearli perfettamente */
    .form-row .form-group {
        margin-bottom: 0;
    }
    /* Manteniamo uno spazio sotto l'intera riga */
    .form-row {
        margin-bottom: 20px;
    }
}

@media (min-width: 1024px) {
    .contact-btn:hover {
        color: var(--color-primary);
        background: var(--color-accent);
    }
}    

</style>