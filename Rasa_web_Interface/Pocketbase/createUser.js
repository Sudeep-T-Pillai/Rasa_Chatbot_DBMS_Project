// createUser.js
const { authenticateAsAdmin } = require('./adminAuth');

async function createUser() {
  try {
    const pb = await authenticateAsAdmin();
    
    const userData = {
      email: 'newuser@example.com',
      password: 'securepassword123',
      Firstname: 'Newuser',
      address:'newuser in second street taingun',
      Lastname:'usernew',
      username:'cool pinapple',
      userId:'1',
      PreferredPaymentMethod: 'Credit card'
    };

    const createdUser = await pb.collection('users').create(userData);
    console.log('User created:', createdUser);
  } catch (error) {
    console.error('Failed to create user:', error);
  }
}

createUser();