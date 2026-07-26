<template>
<header>
    <router-link to="/" class="logo-container" @click="closeMenu">
        <img src="/coriduci-logo.webp" alt="Logo Cori Duci" class="logo" :class="{ 'animationClass': isLogoMoving, 'logo-hidden': !isLogoVisible }" />
    </router-link>
    <!-- Menu per desktop -->
    <nav class="menu nav-desktop">
        <ul class="menu-list">
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/prodotti">Prodotti</router-link></li>
            <li><router-link to="/contatti">Contatti</router-link></li>
            <li><router-link to="/menu/">Menù</router-link></li>
        </ul>
    </nav>

    <!-- Menu per mobile -->
    <button id="toggle-menu" @click="toggleMenu">☰</button>
    <nav class="menu nav-mobile" :class="{ 'active': isMenuOpen }">
        <div class="left-side" :class="{ 'right-transition': isMenuOpen}">
            <ul class="menu-list">
                <li><router-link to="/" @click="closeMenu">Home</router-link></li>
                <li><router-link to="/prodotti" @click="closeMenu">Prodotti</router-link></li>
                <li><router-link to="/contatti" @click="closeMenu">Contatti</router-link></li>
            </ul>
        </div>
        <div class="right-side" :class="{ 'left-transition': isMenuOpen}">
            <ul class="menu-list">
                <li><p>Cori Duci il segreto è l'amore</p></li>
                <li><router-link to="/menu/" @click="closeMenu">Menu</router-link></li>
            </ul>
        </div>
    </nav>
</header>

<main>
    <router-view></router-view>
</main>

<footer>
    <div class="footer-container">
        <div class="contacts-container">
            <h3>Contatti</h3>
            <div class="flex-footer">
                <div class="img-flex-footer">
                    <img src="/coriduci-logo.webp" alt="Logo Cori Duci" class="footer-logo" />
                </div>
                <div class="p-flex-footer">
                    <p>Via Roma, 123</p>
                    <p>Email: info@coriduci.com</p>
                    <p>Telefono: +39 123 456 7890</p>
                </div>
            </div>
        </div>
        <div class="info-container">
            <h3>Informazioni</h3>
            <a href="https://www.iubenda.com/privacy-policy/59679626" 
            class="iubenda-white iubenda-noiframe iubenda-embed" 
            title="Privacy Policy">
            Privacy Policy
            </a>
            <br>
            <a href="https://www.iubenda.com/privacy-policy/59679626/cookie-policy" 
            class="iubenda-white iubenda-noiframe iubenda-embed" 
            title="Cookie Policy">
            Cookie Policy
            </a>
            <!-- <h3>Informazioni</h3>
                <a href="https://www.iubenda.com/privacy-policy/59679626" 
                class="iubenda-nostyle no-brand iubenda-noiframe iubenda-embed iubenda-noiframe" 
                title="Privacy Policy">
                Privacy Policy
                </a>
                <br>
                
                <a href="https://www.iubenda.com/privacy-policy/59679626/cookie-policy" 
                class="iubenda-nostyle no-brand iubenda-noiframe iubenda-embed iubenda-noiframe" 
                title="Cookie Policy">
                Cookie Policy
                </a> -->
        </div>
        <div class ="social-container">
            <h3>Seguici sui social:</h3>
            <div class="social-icons">
                                <!-- Facebook (Quadrato smussato) -->
                <a href="https://www.facebook.com/profile.php?id=61573258272375#" target="_blank" aria-label="Facebook" class="social-link facebook">
                    <svg class="social-icon-svg" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-3 7h-1.924c-.615 0-1.076.252-1.076.889v1.111h3l-.238 3h-2.762v8h-3v-8h-2v-3h2v-1.923c0-2.022 1.064-3.077 3.461-3.077h2.539v3z"/>
                    </svg>
                </a>
                <!-- Instagram (Quadrato smussato con camera forata) -->
                <a href="https://www.instagram.com/coriduci_pescara/" target="_blank" aria-label="Instagram" class="social-link instagram">
                    <svg class="social-icon-svg" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM12 17.5c-3.038 0-5.5-2.463-5.5-5.5s2.462-5.5 5.5-5.5 5.5 2.463 5.5 5.5-2.462 5.5-5.5 5.5zm4.5-9.5c-.828 0-1.5-.672-1.5-1.5s.672-1.5 1.5-1.5 1.5.672 1.5 1.5-.672 1.5-1.5 1.5zM12 8.5c-1.933 0-3.5 1.567-3.5 3.5s1.567 3.5 3.5 3.5 3.5-1.567 3.5-3.5-1.567-3.5-3.5-3.5z"/>
                    </svg>
                </a>
            </div>
        </div>
    </div>
    <div class="copyright">
        <p>&copy; {{ currentYear }} Cori Duci. Tutti i diritti riservati.</p>
    </div>
</footer>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const isMenuOpen = ref(false);
const currentYear = new Date().getFullYear();
const isLogoVisible = ref(true);
const isLogoMoving = ref(false);

const toggleMenu = () => {
    if (window.innerWidth > 768) return;

    if (isMenuOpen.value) {
        // Se il menu è aperto, chiama la funzione di chiusura
        closeMenu();
    } else {
        // Se il menu è chiuso, fai partire la sequenza di apertura
        isMenuOpen.value = true;
        document.body.classList.add('no-scroll');
        
        isLogoVisible.value = false;
        setTimeout(() => {
            isLogoMoving.value = true;
        }, 400); 
        setTimeout(() => {
            isLogoVisible.value = true;
        }, 700); 
    }
}

const closeMenu = () => {
    // Se il menu è già chiuso (es. clicchi sul logo da desktop), fermati subito e non far lampeggiare niente
    if (!isMenuOpen.value) return; 

    // Altrimenti, fai partire la sequenza di chiusura
    isMenuOpen.value = false;
    document.body.classList.remove('no-scroll');
    
    isLogoVisible.value = false;
    setTimeout(() => {
        isLogoMoving.value = false; // Il cuore torna al suo posto in alto a sinistra
    }, 400); 
    setTimeout(() => {
        isLogoVisible.value = true; // Riaccendi la luce
    }, 700);
}

const handleresize = () => {
    if (window.innerWidth > 768 && isMenuOpen.value) {
        isMenuOpen.value = false;
        document.body.classList.remove('no-scroll');
        isLogoVisible.value = true;
        isLogoMoving.value = false;
    }
}

onMounted(() => {
    window.addEventListener('resize', handleresize);
});
onUnmounted(() => {
    window.removeEventListener('resize', handleresize);
});
</script>


<style>





</style>