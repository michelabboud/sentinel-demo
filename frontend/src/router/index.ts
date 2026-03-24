import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/login', component: () => import('../views/LoginView.vue') },
    {
      path: '/dashboard',
      component: () => import('../views/DashboardView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/tasks',
      component: () => import('../views/TasksView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/tasks/:id',
      component: () => import('../views/TaskDetailView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/groups',
      component: () => import('../views/GroupsView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/groups/:id',
      component: () => import('../views/GroupDetailView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/admin/users',
      component: () => import('../views/admin/UsersView.vue'),
      meta: { requiresAuth: true, role: 'admin' },
    },
    {
      path: '/admin/settings',
      component: () => import('../views/admin/SettingsView.vue'),
      meta: { requiresAuth: true, role: 'admin' },
    },
    { path: '/', redirect: '/dashboard' },
  ],
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else if (to.meta.role && localStorage.getItem('userRole') !== to.meta.role) {
    next('/dashboard')
  } else {
    next()
  }
})

export default router
