import { create } from 'zustand';
import axios from 'axios';

const useUserStore = create((set) => ({
  users: [],
  isLoading: false,
  error: null,

  fetchUsers: async () => {
    set({ isLoading: true, error: null });
    try {
      const response = await axios.get('https://jsonplaceholder.typicode.com/users');
      set({ users: response.data, isLoading: false });
    } catch (error) {
      console.error('Error fetching users:', error);
      set({ error: 'Hubo un error al cargar los usuarios. Inténtalo de nuevo.', isLoading: false });
    }
  },

  clearUsers: () => set({ users: [], error: null }),
}));

export default useUserStore;
