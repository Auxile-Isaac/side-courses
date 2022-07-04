{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77f6d5ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "#this is a simple calcurator that perfom addition, substraction, multiplication and Division\n",
    "#asking inputs\n",
    "num1, operator, num2 = input(\"What's your operation? \").split()\n",
    "\n",
    "#converting string into integers\n",
    "num1 = int(num1)\n",
    "num2 = int(num2)\n",
    "\n",
    "#calculation logic\n",
    "if operator == \"+\":\n",
    "    print(f\"{num1} + {num2} = {num1 + num2}\")\n",
    "elif operator == \"-\":\n",
    "    print(f\"{num1} - {num2} = {num1 - num2}\")\n",
    "elif operator == \"*\":\n",
    "    print(f\"{num1} * {num2} = {num1 * num2}\")\n",
    "elif operator == \"/\":\n",
    "    print(f\"{num1} / {num2} = {num1 / num2}\")\n",
    "else:\n",
    "    print(\"use either + , - ,* or /\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0130d743",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
