import PocketBase from 'pocketbase';

const pb = new PocketBase('http://23.21.225.129:8090');


const user = await pb.collection('users').getFirstListItem({
  filter: 'email = "test@example.com"'
});
const userId = user.id;  // Ensure the userId is correct
console.log(userId);
const schema = await pb.collection('PaymentMethods').getSchema();
console.log(schema);

// example create data
const data = {
  UserId: '1',           // Use the user's ID created earlier
  CardType: 'Visa',
  last4digits: '1234',
  ExpiryDate: '12/25',
  PaymentMethodId: 'Test'
};

const record = await pb.collection('Payment_Method_Table').create(data);
  