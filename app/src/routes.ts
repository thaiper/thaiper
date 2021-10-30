export default  [
    { path: '/', component: () => import('./pages/index.vue') },
    { path: '/abugida', component: () => import('./pages/abugida.vue') },
    { path: '/keyboard-trainer', component: () => import('./pages/keyboard-trainer.vue') },
]
