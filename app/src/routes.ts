export default  [
    { path: '/', component: () => import('./pages/index.vue') },
    { path: '/character-list', component: () => import('./pages/character-list.vue') },
]
