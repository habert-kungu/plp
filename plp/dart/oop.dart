import 'dart:io';
interface

// Interface for BankAccount
abstract class Account {
  void deposit(double amount);
  void withdraw(double amount);
  double getBalance();
}

// BankAccount class implementing the Account interface
class BankAccount implements Account {
  String accountHolderName;
  double balance;

  BankAccount({required this.accountHolderName, required this.balance});

  @override
  void deposit(double amount) {
    balance += amount;
  }

  @override
  void withdraw(double amount) {
    if (amount <= balance) {
      balance -= amount;
    } else {
      print('Insufficient balance');
    }
  }

  @override
  double getBalance() {
    return balance;
  }
}

// SavingsAccount class extending BankAccount
class SavingsAccount extends BankAccount {
  double interestRate;

  SavingsAccount({required String accountHolderName, required double balance, required this.interestRate})
      : super(accountHolderName: accountHolderName, balance: balance);

  // Override deposit method to add interest
  @override
  void deposit(double amount) {
    super.deposit(amount);
    balance += (amount * interestRate);
  }
}

// Method to read data from a file and create BankAccount instance
BankAccount readAccountFromFile(String fileName) {
  List<String> data = File(fileName).readAsLinesSync();
  String accountHolderName = data[0];
  double balance = double.parse(data[1]);
  return BankAccount(accountHolderName: accountHolderName, balance: balance);
}

// Method demonstrating the use of a loop
void printNumbers(int n) {
  for (int i = 1; i <= n; i++) {
    print(i);
  }
}

void main() {
  // Creating a BankAccount instance from a file
  BankAccount myAccount = readAccountFromFile('account_data.txt');
  print('Account holder: ${myAccount.accountHolderName}');
  print('Initial balance: ${myAccount.getBalance()}');

  // Deposit and withdraw operations
  myAccount.deposit(1000);
  myAccount.withdraw(500);

  print('Current balance: ${myAccount.getBalance()}');

  // Creating a SavingsAccount instance
  SavingsAccount mySavings = SavingsAccount(accountHolderName: 'John Doe', balance: 5000, interestRate: 0.05);
  mySavings.deposit(1000);
  print('Savings account balance with interest: ${mySavings.getBalance()}');

  // Demonstrate loop
  printNumbers(5);
}
