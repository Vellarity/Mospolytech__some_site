import { createRouter, createWebHistory } from 'vue-router'
import ShopView from '../views/ShopView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'shop',
      component: ShopView
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    },
    {
      path:'/login',
      name:'login',
      components: () => import('../views/LoginView.vue')
    },
    {
      path:"/shop/:itemID",
      name:"itemInfo",
      component: () => import("../views/ItemView.vue")
    },
  ]
})

export default router