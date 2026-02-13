{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d11a718-ba73-4fed-b19c-529f6a7ca8f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your 4-digit PIN:  Deepika@10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Login successful!\n",
      "\n",
      "\n",
      "----- ATM MENU -----\n",
      "1. Check Balance\n",
      "2. Deposit Money\n",
      "3. Withdraw Money\n",
      "4. Change PIN\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your current balance is: 10000\n",
      "\n",
      "----- ATM MENU -----\n",
      "1. Check Balance\n",
      "2. Deposit Money\n",
      "3. Withdraw Money\n",
      "4. Change PIN\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  2\n",
      "Enter deposit amount:  300\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Amount deposited successfully!\n",
      "\n",
      "----- ATM MENU -----\n",
      "1. Check Balance\n",
      "2. Deposit Money\n",
      "3. Withdraw Money\n",
      "4. Change PIN\n",
      "5. Exit\n"
     ]
    }
   ],
   "source": [
    "correct_pin = \"Deepika@10\"\n",
    "balance = 10000\n",
    "attempts = 3\n",
    "\n",
    "while attempts > 0:\n",
    "    pin = input(\"Enter your 4-digit PIN: \")\n",
    "    \n",
    "    if pin == correct_pin:\n",
    "        print(\"Login successful!\\n\")\n",
    "        break\n",
    "    else:\n",
    "        attempts -= 1\n",
    "        print(\"Wrong PIN! Attempts left:\", attempts)\n",
    "\n",
    "if attempts == 0:\n",
    "    print(\"Card blocked! Too many wrong attempts.\")\n",
    "    exit()\n",
    "\n",
    "while True:\n",
    "    print(\"\\n----- ATM MENU -----\")\n",
    "    print(\"1. Check Balance\")\n",
    "    print(\"2. Deposit Money\")\n",
    "    print(\"3. Withdraw Money\")\n",
    "    print(\"4. Change PIN\")\n",
    "    print(\"5. Exit\")\n",
    "\n",
    "    choice = input(\"Enter your choice: \")\n",
    "\n",
    "    if choice == '1':\n",
    "        print(\"Your current balance is:\", balance)\n",
    "\n",
    "    elif choice == '2':\n",
    "        amount = float(input(\"Enter deposit amount: \"))\n",
    "        balance += amount\n",
    "        print(\"Amount deposited successfully!\")\n",
    "\n",
    "    elif choice == '3':\n",
    "        amount = float(input(\"Enter withdrawal amount: \"))\n",
    "        if amount <= balance:\n",
    "            balance -= amount\n",
    "            print(\"Please collect your cash\")\n",
    "        else:\n",
    "            print(\"Insufficient balance!\")\n",
    "\n",
    "    elif choice == '4':\n",
    "        new_pin = input(\"Enter new 4-digit PIN: \")\n",
    "        correct_pin = new_pin\n",
    "        print(\"PIN changed successfully!\")\n",
    "\n",
    "    elif choice == '5':\n",
    "        print(\"Thank you for using ATM\")\n",
    "        break\n",
    "\n",
    "    else:\n",
    "        print(\"Invalid choice!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f626d973-7dd2-49bf-b350-8fa66c4ccf10",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
