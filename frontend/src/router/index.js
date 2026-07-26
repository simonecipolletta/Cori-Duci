import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue';
import Contacts from '../views/Contacts.vue';
import Products from '../views/Products.vue';
import Menu from '../views/Menu.vue';



const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home,
            meta: {title: 'Cori Duci'}
        },
        {
            path: '/contatti',
            name: 'contatti',
            component: Contacts,
            meta: {title: 'Contatti | Cori Duci'}
        },
        {
            path: '/prodotti/:category?', // <-- Aggiungi :categoria? qui
            name: 'prodotti',
            component: Products
        },
        {
            path: '/menu',
            name: 'Menu',
            component: Menu,
            meta: {title: 'Menu | Cori Duci'}
        }
    ]
});

export default router;